# terminology

## core git terminology

- version control: a system that records changes to files over time so you can go back to specific version later
- repository (repo): a storage space for project's files and its entire history of changes
- working tree: the actual files you see and edit in your project folder -> contents of the HEAD commit's tree + any local changes made but haven't committed yet
- branch: a separate line of development with its own commits, lets you work on changes without affecting the main line
- HEAD: a pointer to either the specified branch or commit -> when it points to a branch, git doesn't complain, but when you checkout a commit, it switches into a "detached HEAD" state
- tag: a permanent bookmark for a specific commit, used to mark release points or important milestones
- commit: a saved snapshot of changes, with a unique ID (SHA-1 hash)

## git workflows

- centralized workflow: everyone works on a single central branch
- feature branch workflow: each feature or fix gets its own branch, then is merged into `main` after review
- forking workflow: instead of branching in the same repo, you make a full copy of the repo in your account, then submit changes back
- gitflow workflow: a branching model with specific roles for branches (`main`, `develop`, `features/*`, `release/*`, `hotfix/*`)

## collaboration & automation

- pull request (PR): a proposal to merge a set of changes from one branch into another branch, often with review & automated checks
- merge: combines the histories of both branches
- rebase: moves/rewrites commits so work is based different branch's latest commits
- hook: a script that runs automatically at certain git events (`pre-commit`, `pre-push`, etc) -> customize git's behavior and automate tasks like code formatting or testing

## extra terms

- clone: copies a remote repo to your machine
- staging area (index): a space to prepare the changes that will be reflected on the next commit
- origin: default name for the remote repo you cloned from
- remote: a version of the repo hosted elsewhere (GitHub, GitLab, Bitbucket)
- detached HEAD: when HEAD points to a commit directly, not to a branch
- conflict: happens when git can't automatically merge changes
- diff: shows changes between two commits, branches or files
- bare repository: a repo without working tree, used mainly as a central hub for collaboration (often stored on a server or Git hosting services like GitHub) -> create with `git init --bare`

# git commands

## setup & configuration

- `git init`: create a new local repository
- `git clone <url>`: copy a remote repository to your machine
- `git config --global user.name "Name"`: set your username for commits
- `git config --global user.email "you@example.com"`: set your email for commits
- `git config --list`: view git configuration

## track changes

- `git status`: show changes in working tree & staging area
- `git add <file>` -stage changes for the next commit
- `git add .`: stage all changes in current folder
- `git restore <file>`: discard changes in working directory (before staging)
- `git reset <file>`: unstage a file (keep changes in working directory)
- `git stash`: puts your work in a temporary "drawer" so you can come back to it later without committing it

## saving work

- `git commit -m 'msg'`: commit saved changes with a message
- `git commit -am 'msg'`: stage and commit all tracked file changes
- `git commit --amend`: modify the last commit (add new file or edit the commit message)

## branching & merging

- `git branch`: list branches
- `git branch <name>`: create a branch
- `git branch -d <name>`: delete a branch
- `git checkout <branch>`: switch between branches + restore working tree files -> `git switch` + `git restore`
- `git switch <branch>`: switch between branches
- `git merge <branch>`: merge another branch into current
- `git rebase <branch>`: reapply commits on top of another branch

## viewing history

- `git log`: view commit history
- `git log --oneline --graph`: compact history with branch graph
- `git reflog`: provide an even more detailed view by tracking updates to branch tips, allowing you to recover changes even if they're no longer referenced by and branch or tag
- `git diff`: show unstaged changes
- `git diff --staged`: show staged changes
- `git show`: lets you inspect exactly what happened in that commit (or tag, branch, etc)
- `git blame`: explores the history of specific code and answer questions about what, how, and why the code was added

## working with remotes

- `git remote -v`: view remote repositories
- `git remote add origin <url>`: add a remote
- `git fetch`: get changes from remote but don't merge
- `git pull`: fetch and merge changes from remote
- `git push`: upload commits to remote
- `git push -u origin <branch>`: push a branch and set upstream tracking (git then knows what to do when you `git fetch|pull|push` in future)

## tags

- `git tag`: list tags
- `git tag <name>`: create a lightweight tag
- `git tag -a <name> -m 'msg'`: create an annotated tag
- `git push origin <tag>`: push a tag to remote

## undo & cleanup

- `git reset --soft <commit>`: move HEAD, keep staged changes
- `git reset --hard <commit>`: move HEAD and discard changes
- `git clean -fd`: remove untracked files and directories
- `git revert <commit>`: create a new commit that undoes changes

# git flow

git flow is a branching model for managing features, releases, and hotfixes in a structured way

2 permanent branches:
- `main` -> production-ready code
- `develop` -> integration brach for features

other branches are temporary and have special purposes

## create a branch for a new feature

- purpose: isolate new work until it's ready to be integrated
- flow:
    ```bash
    # start from develop
    git checkout develop
    git pull origin develop

    # create feature branch
    git checkout -b feature/feature-name
    ```
    - naming convention: `feature/<name>`
    - when done:
        ```bash
        git checkout develop
        git merge feature/feature-name
        git push origin develop
        git branch -d feature/feature-name
        git push origin -d feature/feature-name
        ```
- rule: feature branches are always based on `develop`, never on `main`

## create a branch for a release

- purpose: prepare a production release without blocking `develop` for new features
- flow:
    ```bash
    # start from develop
    git checkout develop
    git pull origin develop

    # create release branch
    git checkout -b release/1.0.0
    ```
    - naming convention: `release/<version>`
    - in the release branch, you:
        - fix bugs
        - update documentation
        - bump version numbers
    - when done:
        ```bash
        git checkout main
        git merge release/1.0.0
        git tag -a v1.0.0 -m "Release 1.0.0"  # mark release

        git checkout develop
        git merge release/1.0.0  # sync fixes into develop
        ```
- rule: release branches are based on `develop` and merged into both `main` and `develop`

## create a branch for a hotfix (urgent production fix)

- purpose: patch a live production issue quickly
- flow:
    ```bash
    # start from main
    git checkout main
    git pull origin main

    # create hotfix branch
    git checkout -b release/1.0.1
    ```
    - naming convention: `hotfix/<version`
    - in the release branch, you:
        - apply the fix
        - update version number if needed
    - when done:
        ```bash
        git checkout main
        git merge hotfix/1.0.1
        git tag -a v1.0.0 -m "Hotfix 1.0.1"

        git checkout develop
        git merge hotfix/1.0.1
        ```
- rule: hotfix branches are based on `main` and merged back into both `main` and `develop`
