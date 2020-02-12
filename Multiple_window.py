from selenium.webdriver import Chrome



driver=Chrome("C:\\Users\\pankaj_kumar4\\Downloads\\chromedriver79.exe")
driver.get("https://www.google.com/intl/en-GB/gmail/about/#")
driver.maximize_window()
driver.find_element_by_xpath("//a[@class='h-c-button h-c-button--primary hero-carousel__cta hero-carousel__cta--reg']").click()
Allwindow=driver.window_handles
print(Allwindow)
for win in Allwindow:
    driver.switch_to.window(win)
    print(driver.current_url)
    print(driver.title)
