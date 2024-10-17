from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import csv

# Установка и инициализация драйвера Edge
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Открытие страницы
driver.get('https://www.divan.ru/kaliningrad/category/divany-i-kresla')
time.sleep(5)  # Ожидание загрузки страницы

# Поиск элементов с ценами диванов
divan_prices = driver.find_elements(By.XPATH, "//span[contains(@class, 'ui-LD-ZU KIkOH')]")

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    if divan_prices:  # Проверяем, что список не пуст
        for price in divan_prices:
            writer.writerow([price.text])
    else:
        print("Цены не найдены.")

# Закрытие браузера
driver.quit()