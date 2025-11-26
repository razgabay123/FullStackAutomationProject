import allure
import pytest
import workflows.mobile_flows as flows
from utilities.common_ops import Save


# main test case, uses parameters from login csv file which is read from flows
class Test_Mobile:
	@allure.title("test01: parameter calculations")
	@allure.description("this test inputs several numbers into the calculator and checks if the results apply")
	@pytest.mark.usefixtures('init_mobile_driver')
	@pytest.mark.parametrize('amount, years, percentage, repayment, interest, save', flows.calculations_data)
	def test_mortgage_calculator_sums(self, amount, years, percentage, repayment, interest, save):
		flows.MobileFlows.calculate_morgage(amount, years, percentage, Save.save(save))
		flows.MobileFlows.verify_repayment_amount(repayment)
		flows.MobileFlows.verify_interest_rate(interest)
	
	@allure.title("test02: Verify and erase saved calculation")
	@allure.description("this test swipes to the saved calculations area, verifies the saved percentage, and erases it")
	def test_mortgage_calculator_save(self):
		flows.MobileFlows.swipe_to_save('left')
		flows.MobileFlows.verify_percent("1.0")
		flows.MobileFlows.delete_save()
# Last updated: 2025-11-26
