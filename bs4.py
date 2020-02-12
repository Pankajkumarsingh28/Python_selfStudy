import bs4
import  requests


url="https://www.google.com/"
response=requests.get(url)
print(response.text)
print(response.status_code)

#parse_data=bs4.parse_data(response.text)