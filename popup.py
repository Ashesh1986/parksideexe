import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains

#declaring browser path (We need to download dirver for whichever browser we want to run test)
driver=webdriver.Chrome(executable_path="C:\Chrome\chromedriver.exe")

#declaring "target" which we want to open using above browser
driver.get("https://en.wikipedia.org/wiki/Metis_(mythology)")
driver.maximize_window()

# grabbing path for NIKE link and adding exception handle
try:
    link=driver.find_element_by_xpath("//*[@id='mw-content-text']/div/table[1]/tbody/tr[6]/td/div/ul/li[13]/a")
#scrolling webpage to reach to NIKE link
    driver.execute_script("arguments[0].scrollIntoView();",link)
    time.sleep(3)
except NoSuchElementException:
    print("Element not found")

#Performing mouse over using actionchain control
action=ActionChains(driver)
action.move_to_element(link).perform()
time.sleep(5)
text=driver.find_elements_by_xpath("/html/body/div[8]/div/a[2]")
for link in text:
    print(link.text)

time.sleep(5)
driver.close()