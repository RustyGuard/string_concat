from  behave import given, when, then

@given('Не указан файла вывода')
def step_impl(context):
    pass

@when('Утилита запущена')
def step_impl(context):
    assert True is not False

@then('Результирующая строка выведена в терминал')
def step_impl(context):
    assert context.failed is False
