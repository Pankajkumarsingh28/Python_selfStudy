from selenium.webdriver import Chrome



driver=Chrome("C:\\Users\\pankaj_kumar4\\Downloads\\chromedriver79.exe")
driver.get("http://www.qaclickacademy.com/practice.php")
driver.maximize_window()
driver.switch_to.frame("courses-iframe")

driver.find_element_by_xpath("//a[text()='Courses']").click()
driver.switch_to.default_content()
driver.find_element_by_xpath("//input[@value='radio1']").click()