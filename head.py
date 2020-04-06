#writing tests using selenium webdriver
#importing selenium webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
#declaring browser path (We need to download dirver for whichever browser we want to run test and give path below)

driver=webdriver.Chrome(executable_path="C:\Chrome\chromedriver.exe")

#declaring "target" which we want to open using above browser
driver.get("https://en.wikipedia.org/wiki/Metis_(mythology)")
driver.maximize_window()

#Now printing text of "content" box and appending values in array content
try:
    contentdict=driver.find_elements(By.CLASS_NAME,"toctext")
    content = []
    for link in contentdict:
        print(link.text)
        content.append(link.text)
except NoSuchElementException:
    print("Element not found")

#her also printing elements of class"mw-headline" of header and appending values in array heading
try:
    headingdict=driver.find_elements_by_xpath("//span[@class='mw-headline']")
    heading = []
    for span in headingdict:
        print(span.text)
        heading.append(span.text)
except NoSuchElementException:
    print("Element not found")

#now printing both arrays
print(content)
print(heading)

# now comparing both arrays "content" and "heading"
if content.sort() == heading.sort():
    print("Success")
else:
    print("Fail")

#closing browser
driver.close()