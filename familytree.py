from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Chrome\chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/Metis_(mythology)")
driver.maximize_window()
#adding wait so metis page load stays visible three seconds
time.sleep(3)
# Clicking on Nike Link
link=driver.find_element_by_xpath("//*[@id='mw-content-text']/div/table[1]/tbody/tr[6]/td/div/ul/li[13]/a").click()

#scroll by fix element(family tree)
flag=driver.find_element_by_xpath("//*[@id='Family_tree']")
driver.execute_script("arguments[0].scrollIntoView();",flag)

#adding wait so family tree stays visible for 5 sec
time.sleep(5)
#closing window
driver.close()