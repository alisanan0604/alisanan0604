import os
import re
import urllib.request
import json
from pathlib import Path

USERNAME = os.environ.get("GITHUB_USERNAME", "alisanan0604")
TOKEN = os.environ.get("GITHUB_TOKEN")

API_URL = f"https://api.github.com/users/{USERNAME}"

headers = {
    "User-Agent": "github-readme-updater",
    "Accept": "application/vnd.github+json",
}

if TOKEN:
    headers["Authorization"] = f"Bearer {TOKEN}"


def github_get(url):
    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode())


user = github_get(API_URL)

repos = user.get("public_repos", 0)
followers = user.get("followers", 0)
following = user.get("following", 0)

repos_data = github_get(
    f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
)

stars = sum(repo.get("stargazers_count", 0) for repo in repos_data)

stats_path = Path("assets/stats.svg")

if stats_path.exists():
    svg = stats_path.read_text(encoding="utf-8")

    replacements = {
        r'(<tspan fill="#2dd4bf" font-weight="bold">Repositories</tspan>\s*<tspan x="190" fill="#e6edf3">)[^<]*':
            rf'\g<1>{repos}',

        r'(<tspan fill="#2dd4bf" font-weight="bold">Stars</tspan>\s*<tspan x="190" fill="#e6edf3">)[^<]*':
            rf'\g<1>{stars}',

        r'(<tspan fill="#2dd4bf" font-weight="bold">Followers</tspan>\s*<tspan x="190" fill="#e6edf3">)[^<]*':
            rf'\g<1>{followers}',

        r'(<tspan fill="#2dd4bf" font-weight="bold">Following</tspan>\s*<tspan x="190" fill="#e6edf3">)[^<]*':
            rf'\g<1>{following}',
    }

    for pattern, replacement in replacements.items():
        svg = re.sub(pattern, replacement, svg)

    stats_path.write_text(svg, encoding="utf-8")

print(f"Repositories: {repos}")
print(f"Stars: {stars}")
print(f"Followers: {followers}")
print(f"Following: {following}")