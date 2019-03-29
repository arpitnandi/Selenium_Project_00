from appium import webdriver

class Base:

    def __init__(self):

        desired_caps = {}
        desired_caps['deviceName'] = 'Pixel_XL_API_26'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['app'] = '/Users/arpit.nandi/Downloads/patientapp-debug.apk'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['autoGrantPermissions'] = 'true'
        self.AndroidDriver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
