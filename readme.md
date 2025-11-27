# Currency Converter

A simple Python-based currency conversion application that uses the ExchangeRate API to get real-time exchange rates.

## Features

- Convert IDR to USD
- Convert USD to IDR
- Convert IDR to CNY (Chinese Yuan)
- Real-time exchange rates from ExchangeRate API
- User-friendly command-line interface
- Option to perform multiple conversions

## Prerequisites

Before running the application, make sure you have:

- Python 3.x installed
- `requests` and `python-dotenv` packages
- API Key from [ExchangeRate-API](https://www.exchangerate-api.com/)

## Installation

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the root directory:
```
API_KEYS=your_api_key_here
```

4. Get a free API key from [ExchangeRate-API](https://www.exchangerate-api.com/) and add it to the `.env` file

## Usage

1. Run the script:
```bash
python main.py
```

2. Select the desired conversion type:
   - `1` - IDR to USD
   - `2` - USD to IDR
   - `3` - IDR to CNY

3. Enter the amount of money you want to convert

4. The conversion result will be displayed with 4 decimal places

5. Choose whether to perform another conversion or exit

## Contoh Output

```
Which currency do you want to convert:
    1. IDR to USD
    2. USD to IDR
    3. IDR to CNY
  Pilihan : 1
Berapa Uang Yang anda ingin konversikan : 100000
100000 IDR = 6.3500 USD

Apakah anda ingin menukarkan lagi ?
1. Ya
2. Tidak
Answer : tidak
```

## File Structure

```
.
├── main.py          # Main application file
├── .env            # API key configuration file (not committed)
└── README.md       # Documentation
```

## Notes

- Make sure you have an active internet connection as the application requires API access
- The free API has request limits, check ExchangeRate-API documentation for details
- The `.env` file should be added to `.gitignore` for security

## License

This project is free to use for learning and development purposes.