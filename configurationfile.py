from configparser import ConfigParser

config=ConfigParser()
config.read("C:/Users/Pankaj_kumar4/PycharmProjects/Selenium_Automation_21_Dec/Config.cfg")

print(config.get("section1","username"))