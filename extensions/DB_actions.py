import allure


class DB_Actions:
    database = None  # Shared DB connection inside the class

    @staticmethod
    @allure.step("Build a SQL query: SELECT x FROM y...")
    def query_builder(columns, table, where_name, where_val) -> str:
        cols = ",".join(columns)
        query = "SELECT " + cols + " FROM " + table + " WHERE " + where_name + " " + where_val
        return query

    @staticmethod
    @allure.step("Returns the SQL query results")
    def get_query_result(columns, table, where_name, where_val) -> list:
        query = DB_Actions.query_builder(columns, table, where_name, where_val)
        db_cursor = DB_Actions.database.cursor()  # Use the shared class variable
        db_cursor.execute(query)
        result = db_cursor.fetchall()
        return result
