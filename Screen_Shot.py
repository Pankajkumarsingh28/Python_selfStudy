from selenium.webdriver import Chrome



driver=Chrome("C:\\Users\\pankaj_kumar4\\Downloads\\chromedriver79.exe")
driver.get("https://thetestingworld.com/testings/")
driver.maximize_window()
driver.get_screenshot_as_file("C://Users//pankaj_kumar4//Desktop//Python//screenshot.png")
driver.execute_script("window.scrollTo(0,400);")