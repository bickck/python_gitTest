from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\PracticeSave\selenium\chromedriver')
driver.get("https://www.pixiv.net/")
assert "pixiv" in driver.title

driver.implicitly_wait(5)

print(driver.title)
try:
     WebDriverWait(driver, 5).until( EC.presence_of_all_elements_located((By.XPATH),'/html/body/div[3]/div[3]/div[3]/div/div[2]/a[3]'))
except:
    print("해당 URL이 없음")
    driver.find_element_by_xpath(' /html/body/div[3]/div[3]/div[3]/div/div[2]/a[3]').click()
else:
    #url_link =driver.find_element_by_link_text('Google로 계속하기')
    driver.close()

#assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
