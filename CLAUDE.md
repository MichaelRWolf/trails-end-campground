# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Trails End Campground documentation repository. Main focus: Vision Signs project (inspirational signage system for campground).

**Structure:**

- `source/` -- shared background information (wild areas, cultivated areas, infrastructure, residential, work spaces, recreational)
- `vision_signs/` -- main project (signage design, style guide, prototypes)
- `geology/` -- supplementary research
- Root level: logos, project organization docs

**Key constraint:** Max 3 levels nesting; lowercase-with-hyphens filenames; cross-project links to `source/` for consistency.

## Commands

### Linting and Validation

```bash
# Fix markdown formatting issues
markdownlint --fix --config ~/.markdownlint.json

# Install pre-commit hooks (run once after cloning)
make setup-hooks

# Test all hooks on all files
pre-commit run --all-files
```

**Pre-commit hooks configured:** markdownlint (auto-fix), markdown-table-formatter, check-added-large-files, texthooks.

### Project Structure

Store per-project files in project-specific directories (e.g., `vision_signs/plan.md`, `vision_signs/PROJECT.md`). Keep all source information in `source/` for reuse across projects.

## Markdown Conventions

- **No line-length rule (MD013)** -- ignored
- **Hard-wrap disabled** -- paragraphs are single long lines; editor handles display wrapping
- **markdownlint config:** `.markdownlint.json` (project-level; overrides user config)
- **prettier:** configured to respect existing line structure (see .pre-commit-config.yaml)

## Notes

- Repo tracks logos and images (`.webp`, `.png`, `.jpeg` marked binary)
- Google Drive integration available (see Makefile: `install` target syncs testimonials)
- MIT licensed
