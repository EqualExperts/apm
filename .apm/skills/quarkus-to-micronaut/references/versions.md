# Version selection

Documentation snapshot checked 2026-11-15:

| Component | Observed stable release | Official evidence |
| --- | --- | --- |
| Micronaut platform (target) | 5.2.6 | [Release announcement](https://micronaut.io/2026/11/11/micronaut-framework-5-2-6/) and [platform matrix](https://micronaut-projects.github.io/micronaut-platform/latest/guide/) |
| Quarkus (source reference) | 3.40.1.2, 3.40 LTS line | [Release history](https://quarkus.io/releases/) |

Recheck [Micronaut release announcements](https://micronaut.io/category/release-announcements/) and the platform matrix at invocation. Use the latest stable target unless the user selects another line. Exclude previews and snapshots; record the retrieval date, source URLs and resolved versions. Offline use must identify this as a dated snapshot. Use the application's actual Quarkus version for source analysis; upgrading the source first is not required.

Micronaut platform, Core, module and build-plugin versions are independent. Follow platform dependency management and the selected plugin's documentation; verify resolution through the project's repositories and wrapper. Never apply the platform version to every artifact.

The [Micronaut 5 Core guide](https://docs.micronaut.io/5.2.x/core/) specifies JDK 25. Align compiler, CI, runtime images and native toolchain. Platform 5 does not support Kotlin/Maven; resolve that constraint with the user through a Gradle migration or an explicitly selected older target. Java/Maven remains a supported combination.

Check platform breaking changes and JSON engine selection. Quarkus serializers and Jackson customizations need separate review for the target's Jackson 3 or Micronaut Serialization integration. A resolved build alone does not prove wire compatibility.

This is a researched target, not an executed migration or compatibility certification.
