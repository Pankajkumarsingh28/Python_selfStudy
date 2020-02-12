from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select  # for Importing Select class for drop down.
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By




driver=Chrome("C:\\Users\\pankaj_kumar4\\Downloads\\chromedriver79.exe")
driver.get("https://thetestingworld.com/testings/")
driver.maximize_window()
driver.find_element_by_name("fld_username").send_keys("Pankaj Kumar")
driver.find_element_by_name("fld_email").send_keys("pks@gmail.com")
driver.find_element_by_name("fld_password").send_keys("123456")
driver.find_element_by_name("fld_cpassword").send_keys("123456")

#clcik on radio button.
driver.find_element_by_xpath("//input[@value='home']").click()

#click on checkbox
driver.find_element_by_xpath("(//input[@name='terms'])[1]").click()



# Working on drop down.
obj=Select(driver.find_element_by_xpath("//select[@name='sex']"))
obj.select_by_index(2)
print(obj.first_selected_option.text)

print(driver.find_element_by_xpath("//select[@name='sex']").text)

country=Select(driver.find_element_by_id("countryId"))
country.select_by_visible_text("India")

Wait=WebDriverWait(driver,100)
Wait.until(ec.text_to_be_present_in_element((By.ID,'stateId'),"Bihar"))

state=Select(driver.find_element_by_id("stateId"))
state.select_by_visible_text("Bihar")



#driver.find_element_by_xpath("//a[text()='Read Detail']").click()