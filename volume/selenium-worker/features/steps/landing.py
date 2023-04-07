from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u'open homepage')
def open_homepage(context):
    context.driver.get("https://google.com")
    assert "Google" in context.driver.title


@when(u'homepage is opened')
def log_user_out(context):
    pass


@then(u'verify title is present')
def verify_logo(context):
    pass
