# CamGW Website

Website for the Cambridge Gravitational Waves (CamGW) Initiative.

## About

This is a GitHub Pages website for CamGW, a collaborative initiative bringing together researchers from various departments at the University of Cambridge working on gravitational wave science.

## Structure

The website includes the following pages:

- **Home** (`index.md`) - Landing page with links to various departments
- **Meetings** (`meetings.md`) - Meeting schedules and materials from past meetings
- **Students** (`students.md`) - Information for students interested in gravitational wave research
- **People** (`people.md`) - Directory of CamGW members
- **Research** (`research.md`) - Research themes and activities
- **News** (`news.md`) - News and announcements
- **Publications** (`publications.md`) - Recent publications by CamGW members

## Assets

Static assets (images, meeting materials, documents) are stored in the `assets/` directory:

- `assets/images/` - Images
- `assets/meetings/` - Meeting materials organized by year
- `assets/documents/` - Other documents

## Local Development

To run the site locally:

1. Install Jekyll and dependencies:
   ```bash
   gem install bundler jekyll
   ```

2. Create a Gemfile (if not present) with:
   ```ruby
   source "https://rubygems.org"
   gem "github-pages", group: :jekyll_plugins
   ```

3. Install dependencies:
   ```bash
   bundle install
   ```

4. Serve the site:
   ```bash
   bundle exec jekyll serve
   ```

5. View at `http://localhost:4000`

Full install stack:

```bash
# Check current Ruby version and location
ruby -v && which ruby

# Check for existing Ruby version managers
which rbenv || echo "rbenv not found" && which rvm || echo "rvm not found"

# Verify Homebrew is available
which brew

# Install rbenv and ruby-build via Homebrew
brew install rbenv ruby-build

# Add rbenv to shell configuration
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(rbenv init -)"' >> ~/.zshrc

# Initialize rbenv and check available Ruby versions
export PATH="$HOME/.rbenv/bin:$PATH" && eval "$(rbenv init -)" && rbenv install --list | grep -E "^\s*[0-9]+\.[0-9]+\.[0-9]+$" | tail -5

# Install latest Ruby version (3.4.6)
export PATH="$HOME/.rbenv/bin:$PATH" && eval "$(rbenv init -)" && rbenv install 3.4.6

# Set as global default and verify
export PATH="$HOME/.rbenv/bin:$PATH" && eval "$(rbenv init -)" && rbenv global 3.4.6 && rbenv version

# Install Bundler
export PATH="$HOME/.rbenv/bin:$PATH" && eval "$(rbenv init -)" && gem install bundler

# Install Jekyll
export PATH="$HOME/.rbenv/bin:$PATH" && eval "$(rbenv init -)" && gem install jekyll

# Verify all installations
export PATH="$HOME/.rbenv/bin:$PATH" && eval "$(rbenv init -)" && ruby -v && bundler -v && jekyll -v

# Navigate to existing Jekyll site (your camgw-web directory)
cd /Users/james/Dropbox/JimDex/50-59\ Career/52\ Cambridge/52.25\ CamGW/website/camgw-web

# Check site contents
ls -la

# Create GitHub Pages compatible Gemfile
# (File was created via tool - see Gemfile content below)

# Install GitHub Pages dependencies
export PATH="$HOME/.rbenv/bin:$PATH" && eval "$(rbenv init -)" && bundle install

# Serve site locally with live reloading
export PATH="$HOME/.rbenv/bin:$PATH" && eval "$(rbenv init -)" && bundle exec jekyll serve --watch --incremental

# Install rbenv and ruby-build via Homebrew
brew install rbenv ruby-build

# Add rbenv to shell configuration
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(rbenv init -)"' >> ~/.zshrc


# Gemfile
source "https://rubygems.org"

# GitHub Pages gem
gem "github-pages", group: :jekyll_plugins

# If you have any plugins, add them here:
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

# Start development server
export PATH="$HOME/.rbenv/bin:$PATH" && eval "$(rbenv init -)" && bundle exec jekyll serve --watch --incremental

# Or if you restart your terminal (rbenv will be in PATH):
bundle exec jekyll serve --watch --incremental
```

## Deployment

This site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

## Contributing

To add or update content:

1. Edit the relevant markdown files
2. Add images or documents to the appropriate directories in `assets/`
3. Commit and push changes
4. GitHub Pages will automatically rebuild the site

## License

MIT License - see LICENSE file for details.
