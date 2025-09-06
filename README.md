# Data Analysis Projects Repository

This repository contains data analysis based projects. Each project is organized in its own subdirectory.

## Getting Started

This project uses [uv](https://github.com/astral-sh/uv) for Python project and package management. You can install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Usage

To run a project or script, navigate to its directory and execute a script. For example:

```bash
cd texas-holdem
uv run main.py
```

### Managing Dependencies

- Add a new package:
	```bash
	uv add <package-name>
	```
- Remove a package:
	```bash
	uv remove <package-name>
	```
- Much more...

### UV's Documentation

uv's documentation is available at [docs.astral.sh/uv](https://docs.astral.sh/uv/).
