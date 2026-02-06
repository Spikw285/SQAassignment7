# SQAassignment7 — API Tests

## Overview
This project contains automated API tests (pytest + BDD features) for several public demo APIs.  
Note: Some previously used APIs (ReqRes, DummyAPI) were archived due to access and availability issues. The original HTML report was preserved in `reports/` as is.
## Project structure

```
SQAassignment7/
├── .gitignore
├── config.py
├── conftest.py
├── pytest.ini
├── README.md
├── requirements.txt
├── run_tests.bat
├── run_tests.sh
└── tests/
    ├── bdd/
    │   ├── conftest.py
    │   ├── features/
    │   │   ├── comments.feature
    │   │   ├── posts.feature
    │   │   └── users.feature
    │   └── step_defs/
    │       ├── test_comments_steps.py
    │       ├── test_posts_steps.py
    │       └── test_users_steps.py
    ├── test_api.py
    └── test_dummyapi.py
```
## Active APIs (current)
- **JSONPlaceholder** – the main API used for CRUD tests and BDD features (no auth required).

## Archived APIs
- **ReqRes** — archived due to intermittent 403 errors / access restrictions.
- **DummyAPI** — archived due to the service being unavailable (after repeated attempts of signing in, there were no visible changes)/ missing legal pages and endpoints.

## Requirements
- Python 3.9+
- `pip install -r requirements.txt`

## Environment
No API keys are required for active APIs. If you later (somehow) re-enable DummyAPI, use:
```
export DUMMYAPI_ADD_ID=your_app_id
```


## Run tests
Generate a new HTML report:
```bash
pytest -v --html=reports/report.html --self-contained-html
```
- - -
The project preserves evidence of attempts to test ReqRes and DummyAPI. They were archived after repeated 403 / availability issues. This is documented to explain why replacements were chosen.