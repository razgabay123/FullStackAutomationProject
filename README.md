# 🚀 Final Automation Project

This is a full-featured, multi-platform **test automation framework** built with Python. It supports **Web**, **Mobile**, **API**, **Desktop**, and **Electron** automation using a modular architecture based on the **Page Object Model (POM)**, **Workflows**, and **Data-Driven Testing (DDT)**. Integrated with **Allure Reports** & **Jenkins** for rich visual test reporting.

##### ([Sample video](https://github.com/user-attachments/assets/2482df07-7b11-41b0-b2a5-9c03a4890007))
##### ([jenkins integration preview](https://github.com/user-attachments/assets/fa768f32-39d9-492b-93ca-3fd97f8744b8))
##### ([jenkins run preview](https://github.com/user-attachments/assets/ae59d8a8-42a3-4d06-9a92-30036e0756a5))

---
## 📌 Highlights
- Modular structure for reusability and maintenance

- Data-driven via CSV for flexibility

- Platform-specific separation of logic and flows

- Centralized actions and utilities

- Supports CI/CD integration with Allure & Jenkins for reporting

---

## 🧰 Tech Stack





- **Language:** Python
- **Test Framework:** Pytest
- **Automation Tools:** Selenium, Appium, Requests, Pywinauto, Playwright
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

