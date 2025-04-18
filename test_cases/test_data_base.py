import allure
import pytest
from workflows.DB_flows import DB_Flows
from workflows.web_flows import Web_Flows


@pytest.mark.usefixtures('init_web_driver')
@pytest.mark.usefixtures('init_db_connection')
class Test_DB:
	@allure.title("test heroes login with a database")
	@allure.description("this test uses a SQL database (SELECT) to login and verify each")
	def test_db(self):
		Web_Flows.go_back_main()
		DB_Flows.choose_heroes_db()
	