from behave import given, when, then, step


@given("I open my browser")
def open_browser(context):
    print("Open browser")


@step("I should se home page")
def home_page(context):
    print("Home page")


@step("Other {item}")
def step_impl(context, item):
    """
    :param item:
    :type context: behave.runner.Context
    """
    context.internal_value = item
    print(f'Test {item}')


@then("Final value is displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(f"Final value {context.internal_value}")
