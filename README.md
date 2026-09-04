# Automated REST API Test Suite & CI/CD Framework

A production-grade, code-based API Test Automation Framework built with Python, Pytest, and Requests. Designed to replace manual Postman collection-based testing with a scalable Data-Driven Testing (DDT) model and integrated CI/CD pipelines via GitHub Actions.

## Framework Highlights
* **Authentication & Session Management:** Session-scoped fixtures in `conftest.py` handling cookie persistence across multi-step workflows.
* **Data-Driven Testing (DDT):** `@pytest.mark.parametrize` driven by external JSON and CSV datasets.
* **Continuous Integration:** GitHub Actions pipeline configured for automated test runs on push and pull requests.
* **Visual Reporting:** Automated HTML execution report generation using `pytest-html`.

## Tech Stack
* **Language:** Python 3.11+
* **Test Runner:** Pytest
* **HTTP Client:** Requests
* **Reporting:** Pytest-HTML
* **CI/CD:** GitHub Actions

## Directory Structure
```text
.
├── .github/workflows/   # CI/CD Pipeline Definition
├── data/               # External JSON & CSV Test Data
├── tests/              # Pytest Test Suites & Fixtures
├── .gitignore          # Git Ignored Resources
├── pytest.ini          # Pytest Global Configurations
├── requirements.txt    # Project Dependencies
└── README.md           # Framework Documentation

Setup & Execution
Clone Repository:

git clone https://github.com/Hanialmran576/api-automation-framework.git

cd api-automation-framework

Install Dependencies:

pip install -r requirements.txt

Execute Test Suite & Generate HTML Report:

pytest