import allure
import pytest
import workflows.web_flows as flows


#  main test case, uses parameters from login csv file which is read from flows
@pytest.mark.usefixtures('init_web_driver')
class Test_Web:
	@pytest.mark.parametrize('hero, username, password, expected', flows.login_data)
	@allure.title("test hero logins")
	@allure.description(
		"this test clicks on the hero pictures, then inputs their credentials, logins, then verifies the "
		"hero's title over IMDB")
	def test_heroes(self, hero, username, password, expected):
		# goes back to the first page (the main page) after each cycle
		flows.Web_Flows.go_back_main()
		# clicks + inputs heroes user + pass depending on data
		flows.Web_Flows.choose_hero(hero)
		# verifies the title is the hero's name, eg: Ironman
		flows.Web_Flows.input_login(username, password)
		flows.Web_Flows.verify_hero_title(expected)
	

		