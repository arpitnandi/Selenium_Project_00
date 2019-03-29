from behave import *
from selenium.webdriver.chrome.webdriver import WebDriver

use_step_matcher("re")

ChromeDriver = WebDriver("/Users/arpit.nandi/Python_Project_00/Selenium_Project_00/Resource/chromedriver")
ChromeDriver.implicitly_wait(20)

@given("User is on (.*)")
def step_impl(context,url):
    ChromeDriver.get(url)

@When("User enters the search (.*)")
def step_impl(context,Search):
    ChromeDriver.find_element_by_xpath("//input[@name='q']").send_keys(Search)

@Then("User clicks on search button")
def step_impl(context):
    ChromeDriver.find_element_by_xpath("//input[@name='btnK' and @value='Google Search']").click()

@Then("User selects all links from search result")
def step_impl(context):
    L=ChromeDriver.find_elements_by_xpath("//a/h3")
    for link in L:
        print("("+(str)(L.index(link))+")",link.text)

@Then("User cleare the Search edit text")
def step_impl(context):
    ChromeDriver.find_element_by_xpath("//input[@name='q']").clear()

@Then("User closes the window")
def step_impl(context):
    ChromeDriver.close()