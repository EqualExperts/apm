"""Catalogue build contracts and invalid publication inputs."""
import json
from pathlib import Path
import tempfile
import unittest
from scripts.build_site import catalogue, build


class CatalogueTests(unittest.TestCase):
    def fixture(self, root):
        skill = root / '.apm/skills/example'
        skill.mkdir(parents=True)
        (skill / 'SKILL.md').write_text('# Example', encoding='utf-8')
        (root / 'catalogue/stacks').mkdir(parents=True)
        manifest = {'name': 'test', 'plugins': [{'name': 'example', 'description': 'Example', 'source': './.apm/skills/example'}]}
        (root / 'marketplace.json').write_text(json.dumps(manifest), encoding='utf-8')
        return manifest

    def test_build_contains_real_packages_and_no_template_tokens(self):
        with tempfile.TemporaryDirectory() as directory:
            build(Path(directory))
            page = (Path(directory) / 'index.html').read_text(encoding='utf-8')
            self.assertNotIn('__CATALOGUE__', page)
            self.assertNotIn('__FALLBACK__', page)
            for entry in catalogue()['entries']:
                self.assertIn(entry['name'], page)
            self.assertTrue((Path(directory) / 'style.css').is_file())

    def test_rejects_missing_and_outside_package_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self.fixture(root)
            for source in ('./missing', '../outside'):
                manifest['plugins'][0]['source'] = source
                (root / 'marketplace.json').write_text(json.dumps(manifest), encoding='utf-8')
                with self.assertRaises(ValueError):
                    catalogue(root)

    def test_stack_members_resolve(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            path = root / 'catalogue/stacks/example.json'
            stack = {'name': 'example', 'title': 'Example stack', 'description': 'A selection', 'packages': ['missing']}
            path.write_text(json.dumps(stack), encoding='utf-8')
            with self.assertRaises(ValueError):
                catalogue(root)
            stack['packages'] = ['example']
            path.write_text(json.dumps(stack), encoding='utf-8')
            self.assertEqual(catalogue(root)['stacks'][0]['packages'], ['example'])

    def test_frontmatter_description_formats_and_fallback(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            skill = root / '.apm/skills/example/SKILL.md'
            for value, expected in [('"Build: useful skills"', 'Build: useful skills'),
                                    ('>\n  Build useful\n  skills together.', 'Build useful skills together.'),
                                    ('|\n  First line\n  Second line', 'First line\nSecond line')]:
                skill.write_text(f'---\nname: example\ndescription: {value}\n---\n# Body', encoding='utf-8')
                entry = catalogue(root)['entries'][0]
                self.assertEqual(entry['description'], expected)
                self.assertEqual(entry['marketplaceDescription'], 'Example')
            skill.write_text('# No metadata', encoding='utf-8')
            self.assertEqual(catalogue(root)['entries'][0]['description'], 'Example')
            skill.write_text('---\ndescription: [invalid, list]\n---', encoding='utf-8')
            with self.assertRaises(ValueError):
                catalogue(root)


if __name__ == '__main__':
    unittest.main()
