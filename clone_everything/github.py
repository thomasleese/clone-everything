import re
import requests


URL_REGEX = re.compile(r'https?://(?:www.)?github.com/(?P<account>[^\s]+)')


def matches_url(url):
    """Check with a URL matches a GitHub account URL."""
    return bool(URL_REGEX.match(url))


def get_repos(url, oauth_token=None):
    """Get a list of repo clone URLs."""
    match = URL_REGEX.match(url)
    if match is None:
        raise ValueError('Not a GitHub URL.')

    account = match.group('account')

    url = 'https://api.github.com/users/{0}/repos'.format(account)
    if oauth_token:
        url = 'https://api.github.com/user/repos?type=owner'
    headers = {'User-Agent': 'https://github.com/tomleese/clone-everything'}
    auth = (oauth_token, 'x-oauth-basic') if oauth_token is not None else None
    req = requests.get(url, headers=headers, auth=auth)

    for repo in req.json():
        yield repo['name'], repo['ssh_url']
