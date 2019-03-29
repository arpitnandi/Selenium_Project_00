from appium import webdriver
import time

from appium.webdriver.webdriver import WebDriver

desired_caps = {}
desired_caps['deviceName'] = 'Pixel_XL_API_26'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8'
desired_caps['app'] = '/Users/arpit.nandi/Downloads/patientapp-debug.apk'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['autoGrantPermissions'] = 'true'

AndroidDriver: WebDriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

AndroidDriver.implicitly_wait(120)

AndroidDriver.find_element_by_id('btn_register').click()
AndroidDriver.find_element_by_id('et_email').send_keys('validUser9@protius.com')
AndroidDriver.find_element_by_id('btn_next').click()
AndroidDriver.find_element_by_id('cb_policy_agreement').click()
AndroidDriver.find_element_by_id('btn_i_agree').click()
AndroidDriver.find_element_by_xpath('//android.widget.RelativeLayout').is_displayed()
AndroidDriver.find_element_by_id('btn_action_positive').click()
AndroidDriver.find_element_by_id('et_start_code').send_keys('mobile')
AndroidDriver.find_element_by_id('btn_next').click()
AndroidDriver.find_element_by_id('et_patient_id').send_keys('PP1234')
AndroidDriver.find_element_by_id('btn_next').click()
AndroidDriver.find_element_by_id('et_first_name').send_keys('Colonel Nick')
AndroidDriver.find_element_by_id('et_last_name').send_keys('Fuery')
AndroidDriver.find_element_by_id('btn_next').click()
AndroidDriver.find_element_by_id('et_phone').send_keys('1234567890')
AndroidDriver.find_element_by_id('btn_next').click()
AndroidDriver.find_element_by_id('et_dob').click()
for i in range(10):
    AndroidDriver.find_element_by_xpath('//android.widget.NumberPicker[1]/android.widget.Button[2]').click()
    AndroidDriver.find_element_by_xpath('//android.widget.NumberPicker[2]/android.widget.Button[2]').click()
    AndroidDriver.find_element_by_xpath('//android.widget.NumberPicker[3]/android.widget.Button[2]').click()
AndroidDriver.find_element_by_id('btn_action_positive').click()
AndroidDriver.find_element_by_id('btn_next').click()
AndroidDriver.find_element_by_id('et_password').send_keys('1234567890')
AndroidDriver.find_element_by_id('btn_next').click()
AndroidDriver.find_element_by_id('btn_skip_for_now').click()
AndroidDriver.find_element_by_id('btn_action_positive').click()
AndroidDriver.find_element_by_id('btn_action_positive').click()
AndroidDriver.find_element_by_id('btn_yes').click()
assert AndroidDriver.find_element_by_id('tv_patch_status').is_enabled()
E=AndroidDriver.find_element_by_id('tv_menu')
assert E.is_enabled()
E.click()
time.sleep(2)
E=AndroidDriver.find_element_by_xpath('//android.support.v7.widget.LinearLayoutCompat[5]/android.widget.CheckedTextView')
assert E.is_enabled()
E.click()
AndroidDriver.find_element_by_id('tv_lbl_password_pin').click()
AndroidDriver.find_element_by_id('frame_change_password').click()
AndroidDriver.find_element_by_id('et_password').send_keys('1234567890')
AndroidDriver.find_element_by_id('btn_next').click()
AndroidDriver.find_element_by_id('et_password').send_keys('0987654321')
AndroidDriver.find_element_by_id('btn_next').click()
AndroidDriver.find_element_by_id('btn_action_positive').click()
AndroidDriver.find_element_by_id('tv_back').click()
AndroidDriver.find_element_by_id('tv_editProfile_signOut').click()
AndroidDriver.find_element_by_id('btn_action_positive').click()
E=AndroidDriver.find_element_by_xpath('//android.widget.ImageView')
assert E.is_displayed()
AndroidDriver.quit()