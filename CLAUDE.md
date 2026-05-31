# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A tiny Flask web application used as the practice playground for the
**Code2College Applied AI Cohort**. It's intentionally incomplete — each
task in `tasks/` walks the student through fixing or adding one piece.

## Stack

- Python 3.10+, Flask 3.x, pytest, Jinja2 templates, vanilla HTML/CSS

## Commands

```bash
python app.py               # Run the app → http://localhost:5000
pytest                      # Run all tests
pytest tests/test_task_01.py  # Run tests for a single task
```

## Architecture

`app.py` exports a `create_app()` factory that returns a configured Flask instance. Notes are stored in `app.notes` (an in-memory list of `{"title": str, "body": str}` dicts) — this resets on every restart by design.

Routes live inside `create_app()`:
- `GET /` → renders `templates/home.html` with all notes
- `GET/POST /notes/new` → form page; validates and appends to `app.notes`
- (Task 02) `POST /notes/<idx>/delete` → removes note by index

Templates (`templates/`) use Jinja2 and share inline CSS (system-ui, max-width 720px). Each template has placeholder comments marking where task work goes.

Tests use two fixtures from `tests/conftest.py`: `app` (factory with `TESTING=True`) and `client` (`app.test_client()`). `pyproject.toml` sets `pythonpath = ["."]` so pytest can import `app.py` from the repo root.

## Conventions

- A task is "done" when `tests/test_task_NN.py` passes — read that file first, it is the spec.
- Never edit `tests/` to make them pass — change `app.py` / `templates/` instead.
- Keep changes scoped to the task. Don't refactor unrelated files.
- Always read the task file before writing code; plan before implementing.
- If Claude proposes editing a test to "make it pass," push back.
