# Динамічна генерація SQL-запитів:
# Розробіть мікс, який надає можливість створювати складні SQL-запити на основі
# властивостей об'єкта і його методів. Це може бути корисно для оптимізації роботи з базами даних.
class SQLQueryMixin:
    def __init__(self, table_name):
        self._table_name = table_name

    def generate_select_query(self, **conditions):
        base_query = f"SELECT * FROM {self._table_name}"

        if conditions:
            condition_str = " AND ".join([f"{key} = '{value}'" for key, value in conditions.items()])
            base_query += f" WHERE {condition_str};"

        return base_query


class MyModel(SQLQueryMixin):
    def __init__(self, table_name):
        super().__init__(table_name)


model = MyModel('users')
query = model.generate_select_query(username='ilya', age=20)

print(query)  # SELECT * FROM users WHERE username = 'ilya' AND age = '20';
