from selenium.webdriver import Chrome
import pytest

def test_registration_validate_Date():
    driver =Chrome("C:\\Users\\pankaj_kumar4\\Downloads\\chromedriver79.exe")
    driver.get("https://thetestingworld.com/testings/")
    driver.maximize_window()

#test_registration_validate_Date()