# Trails End Campground

This repository contains documentation files for the Trails End campground project.

## Setup

After cloning this repository, install the pre-commit hooks:

```bash
# Install pre-commit framework (if not already installed)
pip install pre-commit

# Install the git hooks
pre-commit install

# (Optional) Test the hooks on all files
pre-commit run --all-files
```

The pre-commit hooks will automatically:

- Fix markdown formatting issues using markdownlint

Config file location search order:

1. `.markdownlint.json` in project (version controlled, everyone uses same rules)
2. `~/.markdownlint.json` (fallback, not used if project config exists)
3. Markdownlint defaults (fallback)

## Projects

1. [Vision Signs](vision_signs/README.md) - Inspirational signage system that encourages, educates, and guides campground visitors
   - [Project Details](vision_signs/PROJECT.md) - Complete project coordination and context

## Background Information

- [Wild Areas](source/wild_areas.md) - Natural environment, ecology, and wildlife
- [Cultivated Areas](source/cultivated_areas.md) - Farm fields, orchards, and growing spaces
- [Infrastructure](source/infrastructure.md) - Built systems, trails, and facilities
- [Residential Areas](source/residential_areas.md) - Living spaces from tents to seasonal homes
- [Work Spaces](source/work_spaces.md) - Productive areas from farm work to remote work
- [Recreational Areas](source/recreational_areas.md) - Trails, events, and outdoor activities

## Contents

This repository includes various documentation files in Markdown (.md) and text (.txt) formats.

## Links

<https://docs.google.com/document/d/1NTVBj8sWz2zjSuP2zwNYhZ1wlJE6_B5ElQEXfsjIj1I/edit?usp=sharing>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
