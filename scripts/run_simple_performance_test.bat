@echo off
echo ========================================
echo     Simple Performance Test Runner
echo ========================================

REM Check if locust is installed
locust --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Locust...
    pip install locust
)

echo.
echo 🚀 Running performance test with simple reporting...
echo.

REM Run the test for 2 minutes with 10 users
locust -f test_cases/test_performance/reqres.py --users 10 --spawn-rate 2 --run-time 2m --headless --host https://reqres.in

echo.
echo ✅ Test completed!
echo 📊 Check the test-results folder for your simple HTML report
echo.
pause

