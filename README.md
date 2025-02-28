# Webmastor Report

This repository branch holds the input and scripts for the Webmastor office.

## Dependencies

The scripts require the following dependencies:
- [Nu shell](<https://nushell.sh>), used to merge the YAML inputs into a single JSON file.
- [`jinja2-cli`](<https://github.com/mattrobenolt/jinja2-cli>), used to generate the output from 
- [Just](<https://just.systems/>), which holds build scripts.

With access to the Nix package manager, you can start a development shell to install all dependencies:

```bash
nix develop
```

Alternatively, you can use a `nix-shell`:

```bash
nix-shell -p nushell jinja2-cli just
```

Refer to the projects for installation without the Nix package manager.

## Inputs

We use five inputs:

- `Directory.yaml`, which contains the directory in [YAML](<https://en.wikipedia.org/wiki/YAML>) format.
- `Warnings.yaml`, which contains the warnings.
- `Errors.yaml`, which contains the errors.
- `Changelog.yaml`, which contains the changelog.
- `lang.yaml`, which is used for "repeated" text.

## Compiling the Report

Using `just`, you can just build the report:

```bash
just build
```

This writes to the file `report.txt`.
