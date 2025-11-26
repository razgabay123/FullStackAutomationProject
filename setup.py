from setuptools import setup, find_packages

setup(
    name="test_automation_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=8.3.4",
        "selenium>=3.141.0",
        "playwright>=1.52.0",
        "allure-pytest>=2.13.5",
        "appium-python-client>=1.3.0",
        "requests>=2.32.3",
        "mysql-connector-python>=9.2.0",
        "python-dotenv>=1.0.1",
        "webdriver-manager>=4.0.2",
    ],
    author="Raz",
    description="Test Automation Framework",
    python_requires=">=3.8",
)
# Last updated: 2025-11-26
