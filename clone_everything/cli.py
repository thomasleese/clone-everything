from argparse import ArgumentParser
import os
from subprocess import check_call
import sys

from . import github


def clone(name, url):
    """Clone a repo to a location."""
    print('{name} -> {url}'.format(name=name, url=url))
    if os.path.exists(name):
        print(' - Already exists; skipping.')
    else:
        check_call(['git', 'clone', url, '-o', name])


def main():
    """CLI entry point."""
    parser = ArgumentParser()
    parser.add_argument('repos')
    parser.add_argument('--github-oauth-token')
    args = parser.parse_args()

    if github.matches_url(args.repos):
        repos = github.get_repos(args.repos, args.github_oauth_token)
    else:
        print("Unknown 'repos' format.")
        sys.exit(1)

    for name, clone_url in repos:
        clone(name, clone_url)
