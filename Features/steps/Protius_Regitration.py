from behave import *
from Utilities.Waits import Wailts
from appium import webdriver
import time

use_step_matcher("re")

desired_caps = {}
desired_caps['deviceName'] = 'Pixel_XL_API_26'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['app'] = '/Users/arpit.nandi/Downloads/patientapp-debug.apk'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['autoGrantPermissions'] = 'true'

AndroidDriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

Wailts().waitA(120)

@given("Login page is open")
def step(context):
    assert AndroidDriver.find_element_by_xpath('//android.widget.ImageView').is_displayed()

@When("User clicks on register button")
def step(context):
    AndroidDriver.find_element_by_id('btn_register').click()

@Then("Enters (.*) and (.*)")
def step(context,email,code):
    AndroidDriver.find_element_by_id('et_email').send_keys(email)
    AndroidDriver.find_element_by_id('btn_next').click()
    AndroidDriver.find_element_by_id('cb_policy_agreement').click()
    AndroidDriver.find_element_by_id('btn_i_agree').click()
    AndroidDriver.find_element_by_xpath('//android.widget.RelativeLayout').is_displayed()
    AndroidDriver.find_element_by_id('btn_action_positive').click()
    AndroidDriver.find_element_by_id('et_start_code').send_keys(code)
    AndroidDriver.find_element_by_id('btn_next').click()

@Then("Enters (.*), (.*), (.*), (.*) and (.*)")
def step(context, ID, FirstName, LastName, Phone, DOB):
    AndroidDriver.find_element_by_id('et_patient_id').send_keys(ID)
    AndroidDriver.find_element_by_id('btn_next').click()
    AndroidDriver.find_element_by_id('et_first_name').send_keys(FirstName)
    AndroidDriver.find_element_by_id('et_last_name').send_keys(LastName)
    AndroidDriver.find_element_by_id('btn_next').click()
    AndroidDriver.find_element_by_id('et_phone').send_keys(Phone)
    AndroidDriver.find_element_by_id('btn_next').click()
    AndroidDriver.find_element_by_id('et_dob').send_keys(DOB)

@Then("Provides a (.*) and skips from PIN")
def step(context, Password):
    AndroidDriver.find_element_by_id('et_password').send_keys(Password)
    AndroidDriver.find_element_by_id('btn_next').click()
    AndroidDriver.find_element_by_id('btn_skip_for_now').click()
    AndroidDriver.find_element_by_id('btn_action_positive').click()
    AndroidDriver.find_element_by_id('btn_action_positive').click()
    AndroidDriver.find_element_by_id('btn_yes').click()

@When("User is on Dashboard")
def step(context):
    assert AndroidDriver.find_element_by_id('tv_patch_status').is_enabled()

@Then("Clicks on menue")
def step(context):
    E = AndroidDriver.find_element_by_id('tv_menu')
    assert E.is_enabled()
    E.click()
    time.sleep(2)

@Then("Clicks on profile")
def step(context):
    E = AndroidDriver.find_element_by_xpath(
        '//android.support.v7.widget.LinearLayoutCompat[5]/android.widget.CheckedTextView')
    assert E.is_enabled()
    E.click()

@Then("Go for change the old password")
def step(context):
    AndroidDriver.find_element_by_id('tv_lbl_password_pin').click()
    AndroidDriver.find_element_by_id('frame_change_password').click()

@Then("Enters current (.*)")
def step(context, old)
    AndroidDriver.find_element_by_id('et_password').send_keys(old)
    AndroidDriver.find_element_by_id('btn_next').click()

@Then("Enters New (.*)")
def step(context, New):
    AndroidDriver.find_element_by_id('et_password').send_keys(New)
    AndroidDriver.find_element_by_id('btn_next').click()
    AndroidDriver.find_element_by_id('btn_action_positive').click()

@Then("Clicks on back button")
def step(comtext):
    AndroidDriver.find_element_by_id('tv_back').click()

@Then("Clicks on signout")
def step(context):
    AndroidDriver.find_element_by_id('tv_editProfile_signOut').click()

@Then("Clicks on confirm")
def step(context):
    AndroidDriver.find_element_by_id('btn_action_positive').click()

@Then("Comes to loggin page")
def step(context):
    assert AndroidDriver.find_element_by_xpath('//android.widget.ImageView').is_displayed()

@Then("Closes application")
def step(context):
    AndroidDriver.quit()