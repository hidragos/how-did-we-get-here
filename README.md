# 🇺🇸🇪🇺 How did we get here?

A small bilingual static page with a language switch. The English and Romanian text live in separate Markdown files under `content/`.

## Edit the text

- English: `content/en.md`
- Romanian: `content/ro.md`

The page is generated from those Markdown files during deployment. The browser gets a self-contained HTML page with no external runtime dependencies.

## Publish with GitHub Pages

1. Add this folder’s contents to the root of a GitHub repository.
2. In **Settings → Pages**, choose **GitHub Actions** as the build and deployment source.
3. Push to the `main` branch. The included workflow converts both Markdown files and publishes the page.

The workflow can also be started manually from the Actions tab.
