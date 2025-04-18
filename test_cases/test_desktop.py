import allure
import pytest

from extensions.verifications import Verifications
from workflows.desktop_flows import Desktop_Flows as flows


@pytest.mark.usefixtures("init_desktop_driver")
class Test_Desktop:
	@allure.title("Test01: Simple Sum")
	@allure.description("This test verifies the result of a simple sum")
	def test_01_calculate_simple_sum(self):
		flows.calculate_flow("1+1")
		Verifications.verify_equals(flows.get_result_flow(), '2')
		
	@allure.title("Test02: Complex calculation")
	@allure.description("This test verifies the result of a more complex calculation")
	def test_02_calculate_complex(self):
		flows.calculate_flow("2*3+7-9*2/2")
		Verifications.verify_equals(flows.get_result_flow(), '4')
	
	def teardown_method(self):
		flows.clear_flow()
		