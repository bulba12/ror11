import requests

def get_usd_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    data = response.json()

    for rate in data:
        if rate['cc'] == 'USD':
            return rate['rate']
    return None

def convert_to_usd(amount_uah, usd_rate):
    return round(amount_uah / usd_rate, 2)

# Основний блок програми
usd_rate = get_usd_rate()
if usd_rate:
    print(f"Поточний курс долара (USD): {usd_rate} грн")
    try:
        amount_uah = float(input("Введіть суму в гривнях: "))
        amount_usd = convert_to_usd(amount_uah, usd_rate)
        print(f"{amount_uah} грн дорівнює приблизно {amount_usd} доларів США.")
    except ValueError:
        print("Будь ласка, введіть коректне число.")
else:
    print("Не вдалося отримати курс долара.")
