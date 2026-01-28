
class TestClass:

    def test_1(self, class_scope, module_scope, session_scope, function_scope):
        print(f'\n Тест1 test_module1 (в классе): скоуп функция: {function_scope}, скоуп модуля {module_scope}, '
              f'скоуп класса {class_scope}, скоуп сесстя {session_scope}')



    def test_2(self, class_scope, module_scope, session_scope, function_scope):
        print(f'\n Тест2 test_module1 (в классе): скоуп функция: {function_scope}, скоуп модуля {module_scope}, '
              f'скоуп класса {class_scope}, скоуп сесстя {session_scope}')
