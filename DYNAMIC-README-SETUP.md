# Dynamic GitHub README setup

1. Copy `README.md` and the entire `assets/` folder into the root of the profile repository.
2. Copy `scripts/update_github_assets.py` into `scripts/`.
3. Add a GitHub Actions workflow that runs the script on a schedule and on push.
4. The script updates `stats.svg` and `heatmap.svg` from current public GitHub data, then commits changed assets.

The SVGs intentionally contain no GitSkins branding or editor-only “visuals” labels.
