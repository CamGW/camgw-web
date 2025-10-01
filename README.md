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
