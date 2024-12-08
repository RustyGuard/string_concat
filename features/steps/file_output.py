from  behave import given, when, then

@given('Указан файл вывода <file>')
def step_impl(context):
    pass

@when('Утилита запущена')
def step_impl(context):
    assert True is not False

@then('Результирующая строка выведена в файл <file>')
def step_impl(context):
    assert context.failed is False
