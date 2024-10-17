import csv

input_file = 'prices.csv'
output_file = 'processed_prices.csv'

with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
        open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    headers = next(reader, None)
    writer.writerow(headers)

    for row in reader:
        price_str = row[0]

        price_numeric = price_str.replace('руб.', '').replace(' ', '')

        try:
            price_numeric = int(price_numeric)
        except ValueError:
            print(f"Невозможно преобразовать строку в число: {price_str}")
            continue

        writer.writerow([price_numeric])

print(f"Обработка завершена. Обработанные данные сохранены в файле {output_file}.")