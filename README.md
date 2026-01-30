# Robina Li's Technical Blog

A technical blog focused on algorithms, data structures, and software engineering insights. Powered by Jekyll and GitHub Pages.

## Features

- Clean, responsive design
- Markdown-based blog posts
- Automatic GitHub Pages deployment
- RSS feed support
- Social media integration
- Syntax highlighting for code blocks

## Getting Started

### Prerequisites

- Ruby (version 3.1 or higher)
- Bundler gem

### Local Development

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd blog_leetcode
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Build the site (optional, to check for errors):
   ```bash
   bundle exec jekyll build
   ```

4. Serve the site locally on port 4000:
   ```bash
   bundle exec jekyll serve --host 0.0.0.0 --port 4000
   ```
   
   Or with live reload and incremental build (recommended for development):
   ```bash
   bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload --incremental
   ```

5. Open your browser to:
   - Local access: `http://localhost:4000/blog_leetcode/`
   - Network access: `http://0.0.0.0:4000/blog_leetcode/`

### Local Testing Commands

**Basic serve:**
```bash
bundle exec jekyll serve
```

**Serve on specific host and port:**
```bash
bundle exec jekyll serve --host 0.0.0.0 --port 4000
```

**Serve with live reload (auto-refresh on file changes):**
```bash
bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload
```

**Serve with incremental build (faster rebuilds):**
```bash
bundle exec jekyll serve --host 0.0.0.0 --port 4000 --incremental
```

**Serve with all features (recommended for development):**
```bash
bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload --incremental
```

**Build for production:**
```bash
JEKYLL_ENV=production bundle exec jekyll build
```

**Check for build errors:**
```bash
bundle exec jekyll build --trace
```

**Clean and rebuild:**
```bash
bundle exec jekyll clean && bundle exec jekyll build
```

**Stop the server:**
Press `Ctrl+C` in the terminal where Jekyll is running

### Quick Start Script

For convenience, a bash script is provided to automate the local testing process:

```bash
./local-test.sh
```

This script will:
- Check for required dependencies
- Install/update bundle dependencies if needed
- Clean previous builds
- Build the site
- Start the Jekyll server on port 4000 with live reload
- Automatically open your browser to the local site

**Note:** Make sure the script is executable:
```bash
chmod +x local-test.sh
```

### Adding New Posts

1. Create a new file in the `_posts` directory
2. Name it with the format: `YYYY-MM-DD-your-post-title.md`
3. Add front matter at the top:
   ```yaml
   ---
   layout: post
   title: "Your Post Title"
   date: YYYY-MM-DD HH:MM:SS -0000
   categories: category1 category2
   ---
   ```
4. Write your content in Markdown below the front matter

### Deployment

This blog is automatically deployed to GitHub Pages when you push changes to the `main` branch. The deployment is handled by GitHub Actions.

**Repository**: `blog_leetcode`  
**Live URL**: `https://robinali34.github.io/blog_leetcode/`

## Customization

### Site Configuration

Edit `_config.yml` to customize:
- Site title and description
- Author information
- Social media links
- Plugins and themes

### Styling

- Main stylesheet: `assets/main.scss`
- Layouts: `_layouts/`
- Includes: `_includes/`

### Pages

Create new pages by adding `.md` files to the root directory with front matter:
```yaml
---
layout: page
title: "Page Title"
permalink: /page-url/
---
```

## License

This project is open source and available under the [MIT License](LICENSE).
