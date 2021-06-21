from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
 

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
    book = browser.find_element_by_id("book")
    book.click()
    

    #Находим, чему равен x и y
    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    #print(x)
    
    #Заполняем инпут
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    # Отправляем заполненную форму
    button2 = browser.find_element_by_id("solve")
    button2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()  