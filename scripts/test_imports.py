#!/usr/bin/env python3
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

try:
    import workflows.playwright_flows as flow
    print("✅ Successfully imported workflows.playwright_flows")
    print(f"Available methods: {[method for method in dir(flow.PlaywrightFlows) if not method.startswith('_')]}")
except ImportError as e:
    print(f"❌ Failed to import workflows.playwright_flows: {e}")

try:
    from test_cases import conftest
    print("✅ Successfully imported test_cases.conftest")
except ImportError as e:
    print(f"❌ Failed to import test_cases.conftest: {e}")

print(f"Python path includes: {sys.path[:3]}...")  # Show first 3 entries 