from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.set.or.th/th/market/product/stock/quote/AOT/price')

def pricefunc():
    price = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[3]/h1').text
    chg = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[3]/h3/span[1]').text
    chg2 = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[3]/h3/span[2]').text
    name = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[2]/h1').text
    times = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[6]/div/div/div[1]/div[2]').text
    status = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[6]/div/div/div[1]/div[1]').text

    driver.refresh()
    return name, price, chg, chg2, status, times

while True:
    price = pricefunc()
    print("หุ้น : " + price[0])
    print("ราคาล่าสุด : " + price[1])
    print("change : " + price[2])
    print("change % : " + price[3])
    print(price[4])
    print(price[5])
    print()

    time.sleep(5)