from behave import fixture
from behave.fixture import use_fixture_by_tag
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


capabilities = DesiredCapabilities.CHROME.copy()


@fixture
def chrome_driver(context):
    context.driver = webdriver.Remote(
        command_executor="http://selenium-hub:4444/wd/hub",
        desired_capabilities=capabilities,
    )
    yield context.driver
    context.driver.quit()


fixture_registry = {
    "fixture.chrome.driver": chrome_driver,
}


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)
