import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEYS = os.getenv('API_KEYS')

while True:
  choices = int(input("""Which currency do you want to convert:
    1. IDR to USD
    2. USD to IDR
    3. IDR to CNY
  Pilihan : """))

  if choices == 1:
    money_input = int(input("Berapa Uang Yang anda ingin konversikan : "))
    url = f'https://v6.exchangerate-api.com/v6/{API_KEYS}/latest/USD'
    response = requests.get(url)
    data = response.json()

    rate_usd = data['conversion_rates']["IDR"]

    usd = money_input / rate_usd

    print(f"{money_input} IDR = {usd:.4f} USD")


  elif choices == 2:
    money_input = int(input("Berapa Uang Yang anda ingin konversikan : "))
    url = f'https://v6.exchangerate-api.com/v6/{API_KEYS}/latest/USD'
    response = requests.get(url)
    data = response.json()

    rate_usd = data['conversion_rates']['IDR']

    idr = money_input * rate_usd
    print(f"{money_input} USD = {idr:.4f} IDR")

  elif choices == 3:
    money_input = int(input("Berapa Uang Yang anda ingin konversikan : "))
    url = f'https://v6.exchangerate-api.com/v6/{API_KEYS}/latest/USD'
    response = requests.get(url)
    data = response.json()

    rate_idr = data['conversion_rates']['IDR']
    rate_cny = data['conversion_rates']['CNY']

    usd = money_input / rate_idr
    cny = usd * rate_cny
    print(f"{money_input} CNY = {cny:.4f} CNY")

  user_input = input("""
Apakah anda ingin menukarkan lagi ?
1. Ya
2. Tidak
Answer : """).lower()

  if user_input == "ya" or user_input == "1":
      continue
  else:
      break