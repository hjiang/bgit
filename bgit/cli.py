#!/usr/bin/env python3

import argparse
import git
import sys

exit_code = 0


def read_repo_paths():
    return ["~/bin", "~/org", "~/.config", "~/.doom.d"]


def show_status():
    for path in read_repo_paths():
        try:
            repo = git.Repo(path)
            if repo.is_dirty(untracked_files=True):
                print(path, "(dirty)")
                for item in repo.index.diff(None):
                    print("  *\t", item.a_path)
                for item in repo.untracked_files:
                    print("\t", item)
            else:
                print(path, "(clean)")
        except git.exc.InvalidGitRepositoryError:
            print(path, "(invalid)", file=sys.stderr)
            exit_code = 1


def pull():
    for path in read_repo_paths():
        try:
            repo = git.Repo(path)
            g = repo.git
            g.pull()
            print("Finished processing: ", path)
        except:
            print("Error processing: ", path, file=sys.stderr)
            exit_code = 1


def push():
    for path in read_repo_paths():
        try:
            repo = git.Repo(path)
            g = repo.git
            g.push()
            print("Finished processing: ", path)
        except:
            print("Error processing: ", path, file=sys.stderr)
            exit_code = 1


def main():
    argp = argparse.ArgumentParser(description="Manage multiple git repos")
    argp.add_argument("command", nargs="?", help="action to take", default="help")
    args = argp.parse_args()
    action = {"status": show_status, "pull": pull, "push": push}.get(
        args.command, argp.print_help
    )
    action()
    exit(exit_code)


if __name__ == "__main__":
    main()
