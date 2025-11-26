from extensions.DB_actions import DB_Actions
from extensions.verifications import Verifications
from workflows.web_flows import Web_Flows


class DB_Flows:
    @staticmethod
    def choose_heroes_db():
        columns = ['name', 'username', 'password', 'title']
        result = DB_Actions.get_query_result(columns, "heroes", "name", "IN('ironman', 'captainamerica', 'hulk', 'thor')")
        for hero, username, password, title in result:
            heroname = hero
            print(heroname)
            Web_Flows.choose_hero(heroname)
            print(username, password)
            Web_Flows.input_login(username, password)
            film_title = title
            Web_Flows.verify_hero_title(film_title)
            Web_Flows.go_back_main()
# Last updated: 2025-11-26
