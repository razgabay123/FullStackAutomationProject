@echo off
echo ========================================
echo   Performance Testing with Locust
echo   JSONPlaceholder API Load Testing
echo ========================================

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

REM Install required packages
echo 📦 Installing required packages...
pip install locust faker -q

REM Check if packages were installed successfully
if %errorlevel% neq 0 (
    echo ❌ Failed to install required packages
    pause
    exit /b 1
)

echo ✅ Dependencies installed successfully
echo.

REM Show menu options
echo 🎯 Choose a performance test option:
echo.
echo 1. Quick Validation Test (5 users, 2 minutes)
echo 2. Light Load Test (25 users, 5 minutes)
echo 3. Moderate Load Test (50 users, 10 minutes)
echo 4. Heavy Load Test (100 users, 15 minutes)
echo 5. Stress Test (200 users, 10 minutes)
echo 6. Interactive Web UI (Manual control)
echo 7. Run All Tests Sequentially
echo 8. List All Available Scenarios
echo 9. Exit
echo.

set /p choice="Enter your choice (1-9): "

if "%choice%"=="1" (
    echo 🔍 Running Quick Validation Test...
    python performance_tests/run_performance_tests.py smoke_test
) else if "%choice%"=="2" (
    echo 🔄 Running Light Load Test...
    python performance_tests/run_performance_tests.py light_load
) else if "%choice%"=="3" (
    echo 📈 Running Moderate Load Test...
    python performance_tests/run_performance_tests.py moderate_load
) else if "%choice%"=="4" (
    echo 🔥 Running Heavy Load Test...
    python performance_tests/run_performance_tests.py heavy_load
) else if "%choice%"=="5" (
    echo ⚡ Running Stress Test...
    python performance_tests/run_performance_tests.py stress_test
) else if "%choice%"=="6" (
    echo 🌐 Starting Interactive Web UI...
    echo Open your browser to http://localhost:8089
    python performance_tests/run_performance_tests.py interactive
) else if "%choice%"=="7" (
    echo 🔄 Running All Test Scenarios...
    python performance_tests/run_performance_tests.py all
) else if "%choice%"=="8" (
    echo 📋 Available Test Scenarios:
    python performance_tests/run_performance_tests.py list
) else if "%choice%"=="9" (
    echo 👋 Goodbye!
    exit /b 0
) else (
    echo ❌ Invalid choice. Please select 1-9.
)

echo.
echo 📊 Performance test completed!
echo 📁 Check test-results/performance/ for detailed reports
echo.
pause 