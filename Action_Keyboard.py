from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver=Chrome("C:\\Users\\pankaj_kumar4\\Downloads\\chromedriver79.exe")
driver.get("https://thetestingworld.com/testings/")
driver.maximize_window()

driver.find_element_by_name("fld_username").send_keys("Pankaj Kumar")

a=ActionChains(driver)
a.send_keys(Keys.TAB).perform()
#a.send_keys(driver.find_element_by_name("fld_email")).send_keys(Keys.TAB).perform()
