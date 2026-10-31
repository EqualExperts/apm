"""Check a locally served catalogue. Requires Playwright and Microsoft Edge."""
import argparse
import json
from pathlib import Path
from playwright.sync_api import sync_playwright, expect


def check(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel='msedge', headless=True)
        context = browser.new_context(viewport={'width': 1440, 'height': 1100}, permissions=['clipboard-read', 'clipboard-write'])
        page = context.new_page()
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(url)
        data = json.loads(page.locator('#data').text_content())
        total = len(data['entries']) + len(data['stacks'])
        expect(page.locator('.card')).to_have_count(total)
        assert page.locator('.card').first.bounding_box()['width'] == 270
        page.locator('#search').fill('when a user requests a reusable skill')
        expect(page.locator('.card')).to_have_count(1)
        expect(page.locator('.card p')).to_contain_text('when a user requests a reusable skill')
        page.locator('#search').fill('Validate APM skill structure')
        expect(page.locator('.card')).to_have_count(1)
        page.reload()
        expect(page.locator('.card')).to_have_count(1)
        page.get_by_role('button', name='View capability').click()
        expect(page.locator('#detail')).to_be_visible()
        page.locator('#target').select_option('claude')
        expect(page.locator('#install-command')).to_contain_text('apm-skill-validator@equal-experts-apm --target claude')
        page.locator('[data-copy="install-command"]').click()
        assert '--target claude' in page.evaluate('navigator.clipboard.readText()')
        page.keyboard.press('Escape')
        expect(page.locator('#detail')).not_to_be_visible()
        page.locator('#search').fill('')
        page.get_by_role('button', name='Stacks', exact=True).click()
        expect(page.locator('.card')).to_have_count(len(data['stacks']))
        if data['stacks']:
            stack = data['stacks'][0]
            page.get_by_role('checkbox', name='Select ' + stack['title'], exact=True).check()
            expect(page.locator('#selection-count')).to_have_text(str(len(stack['packages'])) + ' selected')
            page.locator('#clear-selection').click()
        page.get_by_role('button', name='Everything', exact=True).click()
        expect(page.locator('.card')).to_have_count(total)
        Path('dist').mkdir(exist_ok=True)
        expect(page.locator('#copy-selection')).to_be_disabled()
        page.get_by_role('checkbox', name='Select Skill Creator', exact=True).check()
        page.get_by_role('checkbox', name='Select Skill Validator', exact=True).check()
        expect(page.locator('#selection-count')).to_have_text('2 selected')
        page.locator('#selection-target').select_option('copilot')
        page.locator('#search').fill('nothing-matches-this')
        expect(page.locator('#selection-count')).to_have_text('2 selected')
        page.locator('#copy-selection').click()
        script = page.evaluate('navigator.clipboard.readText()')
        assert script.count('apm marketplace add EqualExperts/apm') == 1
        assert script.count('apm install ') == 2
        assert script.count('--target copilot') == 2
        page.locator('#search').fill('')
        expect(page.get_by_role('checkbox', name='Select Skill Creator', exact=True)).to_be_checked()
        page.locator('h1').click()
        page.screenshot(path='dist/desktop-preview.png', full_page=True)
        page.set_viewport_size({'width': 390, 'height': 844})
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), 'Mobile horizontal overflow'
        page.locator('.card button').first.click()
        expect(page.locator('#detail')).to_be_visible()
        page.keyboard.press('Escape')
        page.locator('h1').click()
        page.screenshot(path='dist/mobile-preview.png', full_page=True)
        page.get_by_role('button', name='Remove Skill Creator', exact=True).click()
        expect(page.get_by_role('checkbox', name='Select Skill Creator', exact=True)).not_to_be_checked()
        expect(page.locator('#selection-count')).to_have_text('1 selected')
        page.locator('#clear-selection').click()
        expect(page.locator('#copy-selection')).to_be_disabled()
        expect(page.locator('#selection-script')).not_to_contain_text('apm install')
        assert not errors, errors
        browser.close()
        print('Browser checks passed: search, URL state, details, target, clipboard, stacks, mobile overflow; no page errors.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', default='http://localhost:8000')
    check(parser.parse_args().url)
