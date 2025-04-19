# 🚀 Final Automation Project

This is a full-featured, multi-platform **test automation framework** built with Python. It supports **Web**, **Mobile**, **API**, **Desktop**, and **Electron** automation using a modular architecture based on the **Page Object Model (POM)**, **Workflows**, and **Data-Driven Testing (DDT)**. Integrated with **Allure Reports** for rich visual test reporting.

---
## 📌 Highlights
- Modular structure for reusability and maintenance

- Data-driven via CSV for flexibility

- Platform-specific separation of logic and flows

- Centralized actions and utilities

- Suppots CI/CD intergration with Allure for reporting

---

## 🧰 Tech Stack

- **Language:** Python
- **Test Framework:** Pytest
- **Automation Tools:** Selenium, Appium, Requests, Pywinauto (or similar)
- **Reporting:** Allure
- **Data Handling:** CSV, XML
- **Design Patterns:** Page Object Model, Workflows, DDT

---

## 📁 Project Structure

Folder -	Description:

- **configuration/**	XML-based test data and configurations

- **ddt/**	CSV files for data-driven testing scenarios

- **extensions/**	Reusable action modules: API, UI, DB, verification, etc.

- **page_objects/**	Page Object definitions grouped by platform (web, mobile, desktop, etc.)

- **test_cases/**	Entry points for tests – includes platform-specific and API/database tests

- **utilities/**	Common operations, event listeners, and page management logic

- **workflows/**	Business logic for each platform, separated from test scripts

- **allure-results/** allure-report/	Output directories for Allure reporting

- **requirements.txt**	Python dependencies list
---

## 💡 Future Ideas
- Dockerize test environment

- Integrate with Jenkins or GitHub Actions

- Add mock server for API testing

- Implement parallel test execution
