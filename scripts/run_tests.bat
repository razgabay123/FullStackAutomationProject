@echo off
set PYTHONPATH=%cd%
.\venv\Scripts\python.exe -m pytest test_cases\ -v --html=test-results/report.html --self-contained-html
pause 