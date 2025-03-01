# Compiles the Webmastor report.
build:
    #!/usr/bin/env nu
    {
        directory: (cat ./Directory.yaml | from yaml),
        changelog: (cat ./Changelog.yaml | from yaml),
        warnings: (cat ./Warnings.yaml | from yaml),
        errors: (cat ./Errors.yaml | from yaml),
        lang: (cat ./lang.yaml | from yaml),
    } | to json | jinja2 ./report.txt.jinja | save report.txt --force
