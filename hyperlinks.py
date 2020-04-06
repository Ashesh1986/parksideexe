import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#declaring browser path (We need to download dirver for whichever browser we want to run test and give path below)
driver= webdriver.Chrome(executable_path="C:\Chrome\chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/Metis_(mythology)")
driver.maximize_window()

#finding links using ID of element
links=driver.find_elements(By.ID,"toc")
#printing total numbers of links found
print("number of links present",len(links))

#printing all link texts
for link in links:
    print(link.text)

#finding element
family=driver.find_element_by_xpath("//*[@id='toc']/ul/li[1]/a/span[2]")
#printing element text
print(family.text)
#checking if element is visible and enbled
print("Family Hyperlink is Displayed : ", family.is_displayed())
print("Family Hyperlink is Enabled : ",family.is_enabled())
#clicking element(hyperlink)
driver.find_element_by_xpath("//*[@id='toc']/ul/li[1]/a/span[2]").click()
time.sleep(2)

#repeating all above steps for rest of elements
Mythology=driver.find_element_by_xpath("//*[@id='toc']/ul/li[2]/a/span[2]")
print(Mythology.text)
print("Mythology Hyperlink is Displayed : ", Mythology.is_displayed())
print("Mythology Hyperlink is Enabled : ",Mythology.is_enabled())
Mythology=driver.find_element_by_xpath("//*[@id='toc']/ul/li[2]/a/span[2]").click()
time.sleep(2)

References=driver.find_element_by_xpath("//*[@id='toc']/ul/li[3]/a/span[2]")
print(References.text)
print("References Hyperlink is Displayed : ", References.is_displayed())
print("References Hyperlink is Enabled : ",References.is_enabled())
References=driver.find_element_by_xpath("//*[@id='toc']/ul/li[3]/a/span[2]").click()
time.sleep(2)

Seealso=driver.find_element_by_xpath("//*[@id='toc']/ul/li[4]/a/span[2]")
print(Seealso.text)
print("Seealso Hyperlink is Displayed : ", Seealso.is_displayed())
print("Seealso Hyperlink is Enabled : ",Seealso.is_enabled())
Seealso=driver.find_element_by_xpath("//*[@id='toc']/ul/li[4]/a/span[2]").click()
time.sleep(2)

Furtherreading=driver.find_element_by_xpath("//*[@id='toc']/ul/li[5]/a/span[2]")
print(Furtherreading.text)
print("Furtherreading Hyperlink is Displayed : ", Furtherreading.is_displayed())
print("Furtherreading Hyperlink is Enabled : ",Furtherreading.is_enabled())
Furtherreading=driver.find_element_by_xpath("//*[@id='toc']/ul/li[5]/a/span[2]").click()
time.sleep(2)

#closing browser
driver.close()
