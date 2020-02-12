from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver=Chrome("C:\\Users\\pankaj_kumar4\\Downloads\\chromedriver79.exe")
driver.get("https://thetestingworld.com/")
driver.maximize_window()
a=ActionChains(driver)
a.move_to_element(driver.find_element_by_xpath("//a[@title='TRAINING']")).perform()
a.context_click().perform()