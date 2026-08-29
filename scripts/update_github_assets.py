import os
import re
import json
import urllib.request
from pathlib import Path

USERNAME = os.environ.get("GITHUB_USERNAME", "alisanan0604")
TOKEN = os.environ.get("GITHUB_TOKEN")

REST_HEADERS = {
    "User-Agent": "github-readme-updater",
    "Accept": "application/vnd.github+json",
}

GRAPHQL_HEADERS = {
    "User-Agent": "github-readme-updater",
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

if not TOKEN:
    raise RuntimeError("GITHUB_TOKEN is required")


def rest_get(url):
    request = urllib.request.Request(url, headers=REST_HEADERS)

    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode())


def graphql(query, variables):
    payload = json.dumps({
        "query": query,
        "variables": variables
    }).encode("utf-8")

    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers=GRAPHQL_HEADERS,
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode())

    if "errors" in result:
        raise RuntimeError(json.dumps(result["errors"], indent=2))

    return result["data"]


# --------------------------------------------------
# GitHub profile data
# --------------------------------------------------

user = rest_get(f"https://api.github.com/users/{USERNAME}")

repositories = user.get("public_repos", 0)
followers = user.get("followers", 0)
following = user.get("following", 0)

repos_data = rest_get(
    f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
)

stars = sum(
    repo.get("stargazers_count", 0)
    for repo in repos_data
)


# --------------------------------------------------
# GitHub contribution data
# --------------------------------------------------

query = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
            color
          }
        }
      }
    }
  }
}
"""

data = graphql(query, {"login": USERNAME})

contributions = data["user"]["contributionsCollection"]

commits = contributions["totalCommitContributions"]
issues = contributions["totalIssueContributions"]
pull_requests = contributions["totalPullRequestContributions"]

calendar = contributions["contributionCalendar"]


# --------------------------------------------------
# Update stats.svg
# --------------------------------------------------

stats_path = Path("assets/stats.svg")

if stats_path.exists():

    svg = stats_path.read_text(encoding="utf-8")

    replacements = {
        "Repositories": repositories,
        "Stars": stars,
        "Followers": followers,
        "Following": following,
        "Commits": commits,
        "Pull Requests": pull_requests,
        "Issues": issues,
    }

    for label, value in replacements.items():

        pattern = (
            rf'(<tspan[^>]*font-weight="bold">{re.escape(label)}</tspan>'
            rf'\s*<tspan[^>]*>)[^<]*(</tspan>)'
        )

        svg = re.sub(
            pattern,
            rf'\g<1>{value}\g<2>',
            svg,
            count=1
        )

    stats_path.write_text(svg, encoding="utf-8")


# --------------------------------------------------
# Generate heatmap
# --------------------------------------------------

heatmap_path = Path("assets/heatmap.svg")

if heatmap_path.exists():

    svg = heatmap_path.read_text(encoding="utf-8")

    cells = []

    # GitHub contribution calendar:
    # 53 weeks × 7 days

    start_x = 42
    start_y = 120

    cell_size = 10
    gap = 3

    for week_index, week in enumerate(calendar["weeks"]):

        x = start_x + week_index * (cell_size + gap)

        for day_index, day in enumerate(week["contributionDays"]):

            y = start_y + day_index * (cell_size + gap)

            color = day.get("color", "#161b22")

            cells.append(
                f'<rect x="{x}" y="{y}" '
                f'width="{cell_size}" height="{cell_size}" '
                f'rx="2" fill="{color}"/>'
            )

    heatmap_content = "\n    ".join(cells)

    svg = re.sub(
        r'<g id="heatmap">.*?</g>',
        f'<g id="heatmap">\n    {heatmap_content}\n  </g>',
        svg,
        flags=re.DOTALL
    )

    # Update total contribution count
    total = calendar["totalContributions"]

    svg = re.sub(
        r'Contribution activity • Last 12 months',
        f'Contribution activity • {total} contributions in the last year',
        svg
    )

    heatmap_path.write_text(svg, encoding="utf-8")


# --------------------------------------------------
# Output
# --------------------------------------------------

print("GitHub profile updated")
print(f"Repositories: {repositories}")
print(f"Stars: {stars}")
print(f"Followers: {followers}")
print(f"Following: {following}")
print(f"Commits: {commits}")
print(f"Pull Requests: {pull_requests}")
print(f"Issues: {issues}")
print(f"Contributions: {calendar['totalContributions']}")