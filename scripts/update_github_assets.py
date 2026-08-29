#!/usr/bin/env python3
import json
import re
import urllib.request
from datetime import date, timedelta
from pathlib import Path

USERNAME = "alisanan0604"
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def get_json(url):
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "alisanan0604-github-readme-updater",
            "X-GitHub-Api-Version": "2026-03-10",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def github_user():
    return get_json(f"https://api.github.com/users/{USERNAME}")


def github_repos():
    repos = []
    page = 1
    while True:
        batch = get_json(
            f"https://api.github.com/users/{USERNAME}/repos?per_page=100&page={page}&type=owner"
        )
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def contribution_data():
    # Public contribution data, used only by the scheduled GitHub Action.
    return get_json(
        f"https://github-contributions-api.jogruber.de/v4/{USERNAME}?y=last"
    )


def replace_once(text, pattern, replacement):
    new, n = re.subn(pattern, replacement, text, count=1)
    if n != 1:
        raise RuntimeError(f"Could not find expected SVG field: {pattern}")
    return new


def update_stats(user, repos, contributions):
    path = ASSETS / "stats.svg"
    text = path.read_text(encoding="utf-8")

    stars = sum(int(r.get("stargazers_count") or 0) for r in repos)
    repo_count = int(user.get("public_repos") or len(repos))
    followers = int(user.get("followers") or 0)
    following = int(user.get("following") or 0)

    lang_counts = {}
    for r in repos:
        lang = r.get("language")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1
    top_lang = max(lang_counts, key=lang_counts.get) if lang_counts else "—"

    total = contributions.get("total", {})
    activity = total.get("lastYear")
    if activity is None:
        activity = sum(int(c.get("count", 0)) for c in contributions.get("contributions", []))

    # Keep the existing terminal design; only replace the data values.
    text = replace_once(text, r'(<tspan fill="#2dd4bf" font-weight="bold">Stars</tspan><tspan dx="12" fill="#e6edf3">)\d+(</tspan>)', rf'\g<1>{stars}\g<2>')
    text = replace_once(text, r'(<tspan fill="#2dd4bf" font-weight="bold">Repos</tspan><tspan dx="12" fill="#e6edf3">)\d+(</tspan>)', rf'\g<1>{repo_count}\g<2>')
    text = replace_once(text, r'(<tspan fill="#2dd4bf" font-weight="bold">Followers</tspan><tspan dx="12" fill="#e6edf3">)\d+(</tspan>)', rf'\g<1>{followers}\g<2>')
    text = replace_once(text, r'(<tspan fill="#2dd4bf" font-weight="bold">Following</tspan><tspan dx="12" fill="#e6edf3">)\d+(</tspan>)', rf'\g<1>{following}\g<2>') if "Following" in text else text
    text = replace_once(text, r'(<tspan fill="#2dd4bf" font-weight="bold">Top Lang</tspan><tspan dx="12" fill="#e6edf3">)[^<]*(</tspan>)', rf'\g<1>{top_lang}\g<2>')
    text = replace_once(text, r'(<tspan fill="#2dd4bf" font-weight="bold">Activity</tspan><tspan dx="12" fill="#e6edf3">)\d+ contributions(</tspan>)', rf'\g<1>{activity} contributions\g<2>')

    path.write_text(text, encoding="utf-8")
    return stars, repo_count, followers, following, top_lang, activity


def update_heatmap(contributions):
    path = ASSETS / "heatmap.svg"
    text = path.read_text(encoding="utf-8")

    raw = {c["date"]: c for c in contributions.get("contributions", [])}
    # Render 52 complete Sunday->Saturday columns, matching the existing 52x7 SVG.
    # The window ends on the next/current Saturday, so the right edge always represents
    # the current GitHub contribution week. Future days are zero.
    today = date.today()
    days_until_saturday = 6 - ((today.weekday() + 1) % 7)
    end = today + timedelta(days=days_until_saturday)
    start = end - timedelta(days=363)
    items = []
    for offset in range(364):
        d = start + timedelta(days=offset)
        items.append(raw.get(d.isoformat(), {"date": d.isoformat(), "count": 0, "level": 0}))

    colors = {
        0: "#161b22",
        1: "#0e4429",
        2: "#006d32",
        3: "#26a641",
        4: "#39d353",
    }

    cells = re.findall(
        r'<rect x="[0-9.]+" y="(?:120|134|148|162|176|190|204)" width="11" height="11" rx="2" fill="#[0-9a-fA-F]{6}"/>',
        text,
    )
    if len(cells) != 364:
        raise RuntimeError(f"Expected 364 heatmap cells, found {len(cells)}")

    idx = 0
    def repl(_):
        nonlocal idx
        level = int(items[idx].get("level", 0))
        color = colors.get(level, colors[0])
        original = cells[idx]
        idx += 1
        return re.sub(r'fill="#[0-9a-fA-F]{6}"', f'fill="{color}"', original)

    text = re.sub(
        r'<rect x="[0-9.]+" y="(?:120|134|148|162|176|190|204)" width="11" height="11" rx="2" fill="#[0-9a-fA-F]{6}"/>',
        repl,
        text,
    )

    total = contributions.get("total", {}).get("lastYear")
    if total is not None:
        text = re.sub(
            r'(<text x="40" y="[0-9.]+"[^>]*>)[^<]*(</text>)',
            lambda m: m.group(1) + f"{total} contributions in the last year" + m.group(2),
            text,
            count=1,
        )

    path.write_text(text, encoding="utf-8")


def main():
    user = github_user()
    repos = github_repos()
    contributions = contribution_data()
    stats = update_stats(user, repos, contributions)
    update_heatmap(contributions)
    print(
        "Updated GitHub README assets:",
        f"stars={stats[0]}", f"repos={stats[1]}", f"followers={stats[2]}",
        f"following={stats[3]}", f"top_lang={stats[4]}", f"last_year_contributions={stats[5]}"
    )


if __name__ == "__main__":
    main()
