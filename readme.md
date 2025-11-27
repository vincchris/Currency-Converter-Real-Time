Simple Currency Converter
This project is a simple Python script for converting currencies using real-time exchange rate data from the ExchangeRate-API.

✨ Key Features
Converts IDR (Indonesian Rupiah) to USD (US Dollar).

Converts USD (US Dollar) to IDR (Indonesian Rupiah).

Converts IDR (Indonesian Rupiah) to CNY (Chinese Yuan).

Secure use of an API Key via environment variables (.env).

🛠️ Prerequisites
You need Python 3.x installed on your system.

Python Dependencies
This project uses two Python libraries:

requests: For making HTTP requests to the API.

python-dotenv: For loading environment variables from a .env file.

You can install these dependencies using pip:

Bash

pip install requests python-dotenv

🚀 Setup and Installation
Follow the steps below to set up and run the script.

1. Get an API Key
Sign up for a free API Key from ExchangeRate-API.

Once signed up, you will get your API key.

2. Environment Configuration
Create a new file named .env in the same directory as your Python source code.

Add your API key to the .env file in the following format:

API_KEYS="YOUR_API_KEY_HERE"
Note: Make sure to replace "YOUR_API_KEY_HERE" with your actual API key.

3. Run the Script
Once the dependencies are installed and the .env file is configured, you can run the script from your terminal:

Bash

python your_file_name.py
(Replace your_file_name.py with the name of your Python file, e.g., converter.py)

🖥️ How to Use
After running the script, you will be prompted to choose the conversion type:

Which currency do you want to convert:
    1. IDR to USD
    2. USD to IDR
    3. IDR to CNY
Pilihan :
Enter the number corresponding to your conversion choice (1, 2, or 3).

The script will then ask you to enter the amount of money you wish to convert.

The conversion result will be displayed.

You will be asked if you want to perform another conversion. Enter Ya or 1 to continue, or anything else to exit.

📝 Additional Notes
All exchange rate requests use USD as the base currency.

Exchange rates are fetched in real-time from ExchangeRate-API (subject to the limitations of your plan).

🤝 Contributing
If you have suggestions for improvements or new features, please open an issue or submit a pull request.