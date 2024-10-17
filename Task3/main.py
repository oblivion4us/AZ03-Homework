from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import csv

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get('https://www.divan.ru/kaliningrad/category/divany-i-kresla')
time.sleep(5)

divan_prices = driver.find_elements(By.XPATH, "//span[contains(@class, 'ui-LD-ZU KIkOH')]")

with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])

    if divan_prices:
        for price in divan_prices:
            writer.writerow([price.text])
    else:
        print("Цены не найдены.")

driver.quit()