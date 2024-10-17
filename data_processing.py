import csv

# Имя входного и выходного файлов
input_file = 'prices.csv'
output_file = 'processed_prices.csv'

# Открываем входной файл для чтения и выходной файл для записи
with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
        open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    headers = next(reader, None)
    writer.writerow(headers)

    for row in reader:
        # Предполагаем, что цена находится в первом столбце
        price_str = row[0]

        # Убираем текст "руб." и любые пробелы
        price_numeric = price_str.replace('руб.', '').replace(' ', '')

        # Преобразуем строку в число
        try:
            price_numeric = int(price_numeric)
        except ValueError:
            # Если преобразование не удалось, пропускаем эту строку
            print(f"Невозможно преобразовать строку в число: {price_str}")
            continue

        # Записываем обработанную цену в новый файл
        writer.writerow([price_numeric])

print(f"Обработка завершена. Обработанные данные сохранены в файле {output_file}.")