"""
Test script to verify .env configuration is working correctly.
Run this to test that your .env file is being read properly.
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from utilities.common_ops import get_data, _convert_xml_name_to_env_name

# Load .env file
load_dotenv()

print("=" * 60)
print("Testing .env Configuration")
print("=" * 60)

# Test a few key configurations
test_configs = [
    'WaitTime',
    'Browser',
    'URL',
    'API_URL',
    'API_KEY',
    'PW-browser',
    'Mobile_Device',
    'UDID',
]

print("\nTesting get_data() function:")
print("-" * 60)

for config in test_configs:
    try:
        value = get_data(config)
        env_var_name = _convert_xml_name_to_env_name(config)
        env_var = os.getenv(env_var_name)
        source = "ENV (.env)" if env_var else "XML (fallback)"
        # Mask sensitive values
        display_value = value if config != 'API_KEY' else value[:10] + "..." if len(value) > 10 else value
        print(f"✓ {config:20} = {display_value:40} [{source}]")
    except KeyError as e:
        print(f"✗ {config:20} = NOT FOUND - {str(e)}")

print("\n" + "=" * 60)
print("Direct Environment Variable Check:")
print("-" * 60)

# Check some direct env vars
env_vars = ['API_KEY', 'BROWSER', 'WEB_URL', 'WAIT_TIME']
for var in env_vars:
    value = os.getenv(var)
    if value:
        # Mask sensitive values
        display_value = value if var != 'API_KEY' else value[:10] + "..." if len(value) > 10 else value
        print(f"✓ {var:20} = {display_value}")
    else:
        print(f"✗ {var:20} = Not set (will use XML fallback)")

print("\n" + "=" * 60)
print("Summary:")
print("-" * 60)
print("If you see values from 'ENV (.env)', your .env file is working!")
print("If you see values from 'XML (fallback)', .env is not set, using XML.")
print("=" * 60)

