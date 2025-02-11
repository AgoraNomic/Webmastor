---
layout: puremd
---

# Webmastors' Workflows

## Creating a new Officer page

1. Via GitHub, create a repository using the [officer template](<https://github.com/AgoraNomic/officer-template/>). Make sure to include all branches.
2. Create a GitHub role for that office, if one does not already exist, and give the role `maintain` permission over the repository.
3. Perform the setup steps outlined in `officer-template/gh-pages/index.md`.

## Updating existing Officer repos...

(All of the following use the Webmastor as a stand-in for the interested office, and assumes the default branch is `main`.)

### ...with an existing gh-pages branch.

```sh
git clone git@github.com:AgoraNomic/Webmastor.git
cd Webmastor/
git checkout gh-pages

git remote add template git@github.com:AgoraNomic/officer-template.git
git fetch --all
git merge template/gh-pages --allow-unrelated-histories
# Prefer template's `_data`, `_layouts`, and `_includes`.
# Discard or integrate the rest.

# Update any pages to use the `default` and `puremd` layouts.
git push
```

### ...with pages to include and no gh-pages branch.

```sh
git clone git@github.com:AgoraNomic/Webmastor.git
cd Webmastor/
git checkout -b gh-pages

# Clean up files used for automation/that shouldn't be accessed.
# Commit files to retain.
git push --set-upstream origin gh-pages

git remote add template git@github.com:AgoraNomic/officer-template.git
git fetch --all
git merge template/gh-pages --allow-unrelated-histories

# Update any pages to use the `default` and `puremd` layouts.
git push
```

### ...with no pages to preserve/update and no gh-pages branch.

```sh
git clone git@github.com:AgoraNomic/Webmastor.git
cd Webmastor/
git checkout --orphan gh-pages

rm -rf * .gitmodules
git commit --allow-empty -m "Create gh-pages branch"
git push --set-upstream origin gh-pages

git remote add template git@github.com:AgoraNomic/officer-template.git
git fetch --all
git merge template/gh-pages --allow-unrelated-histories

# Update any pages to use the `default` and `puremd` layouts.
git push
```

## Update Officer pages to template

If you have not already, you'll need to add the template as a remote:

```sh
git remote add template git@github.com:AgoraNomic/officer-template.git
```

Then, each time you wish to update:

```sh
git fetch --all
git merge template/gh-pages gh-pages --allow-unrelated-histories
# Resolve merge and commit.
git push
```

If you wish to update the [main website](<https://github.com/AgoraNomic/agoranomic.github.io>), you'll need to target the `master` branch instead.
