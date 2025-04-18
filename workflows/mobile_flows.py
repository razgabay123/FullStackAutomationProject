import allure
import test_cases.conftest as conf
from extensions.touch_actions import Touch_Actions
import utilities.manage_pages as pages
from extensions.verifications import Verifications
import utilities.common_ops as ops


class MobileFlows:
    @staticmethod
    @allure.step('fill details and calculate')
    def calculate_morgage(amount, years, percent, save):
        Touch_Actions.clear(pages.mobile_calculator.get_gbp())
        Touch_Actions.update_text(pages.mobile_calculator.get_gbp(), amount)
        Touch_Actions.clear(pages.mobile_calculator.get_years())
        Touch_Actions.update_text(pages.mobile_calculator.get_years(), years)
        Touch_Actions.clear(pages.mobile_calculator.get_percentage())
        Touch_Actions.update_text(pages.mobile_calculator.get_percentage(), percent)
        Touch_Actions.click(pages.mobile_calculator.get_calc_button())
        if save:
            Touch_Actions.click((pages.mobile_calculator.get_save_btn()))
    
    @staticmethod
    @allure.step('verify repayment £#')
    def verify_repayment_amount(expected: str):
        actual = pages.mobile_calculator.get_repayment().text
        Verifications.verify_equals(actual, '£' + expected)
    
    @staticmethod
    @allure.step('verify interest £#')
    def verify_interest_rate(expected: str):
        actual = pages.mobile_calculator.get_interest().text
        Verifications.verify_equals(actual, '£' + expected)
    
    @staticmethod
    @allure.step('swipe to save')
    def swipe_to_save(direction):
        width = conf.mobile_size['width']
        height = conf.mobile_size['height']
        
        start_x = None
        start_y = None
        end_x = None
        end_y = None
        
        if direction == 'left':
            start_x = width * 0.9
            end_x = width * 0.1
            start_y = end_y = height * 0.5
        if direction == 'right':
            start_x = width * 0.1
            end_x = width * 0.9
            start_y = end_y = height * 0.5
            
        if direction == 'up':
            start_y = height * 0.9
            end_y = height * 0.1
            start_x = end_x = width * 0.5
            
        if direction == 'down':
            start_y = height * 0.1
            end_y = height * 0.9
            start_x = end_x = width * 0.5
        print(start_x,start_y,start_y,end_y)
        Touch_Actions.swipe_action(start_x, start_y, end_x, end_y, int(ops.get_data('swipe_dur')))
        
    @staticmethod
    @allure.step('verify %#')
    def verify_percent(expected):
        actual = pages.saved_calculations.get_rate().text
        Verifications.verify_equals(actual,  expected + "%")
        
    @staticmethod
    @allure.step('delete afer verify')
    def delete_save():
        Touch_Actions.click(pages.saved_calculations.get_delete())
        Touch_Actions.click(pages.saved_calculations.get_okay())
        
        
# data for calculations
calculations = ops.read_csv(ops.get_data('calculations_csv'))
calculations_data = [
            (calculations[0][0], calculations[0][1], calculations[0][2], calculations[0][3], calculations[0][4],
             calculations[0][5]),
            (calculations[1][0], calculations[1][1], calculations[1][2], calculations[1][3], calculations[1][4],
             calculations[1][5]),
            (calculations[2][0], calculations[2][1], calculations[2][2], calculations[2][3], calculations[2][4],
             calculations[2][5]),
            (calculations[3][0], calculations[3][1], calculations[3][2], calculations[3][3], calculations[3][4],
             calculations[3][5]),
            ]
