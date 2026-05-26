import freecurrencyapi, datetime, csv, os

client = freecurrencyapi.Client('fca_live_KsqAPmNxLYQ8EGJh0MpWsmv8S2Dvt5uezaiyKzMX')
file_path = "C:/Users/New/Documents/VS/json_csv/currencies.csv"
data = client.latest()["data"]
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
headers = ["timestamp", "currency", "price"]
file_exists = os.path.isfile(file_path)

with open (file_path, "a", newline="", encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=headers, delimiter=';')

    if not file_exists:
        writer.writeheader()

    for currency, price in data.items():
        writer.writerow({
            "timestamp": timestamp,
            "currency": currency,
            "price": price
        })

print("Готово, проверь файл")