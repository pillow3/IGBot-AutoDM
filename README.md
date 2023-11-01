# Instagram Messaging Bot

This Python script is designed to automate sending messages to Instagram accounts. It utilizes the Selenium library to interact with the Instagram website and send messages to a list of specified accounts. This README provides an overview of the code, its functionality, and how to use it.

## Requirements

- Python 3.10.6
- Selenium 4.14.0
- Webdriver-manager 4.0.1

You can install these dependencies using pip:

```bash
pip install python==3.10.6 selenium==4.14.0 webdriver-manager==4.0.1
```

## Setup

1. Clone this repository to your local machine.

2. Create a JSON file named `credentials.json` with the following structure:

```json
{
    "username": "your_instagram_username",
    "password": "your_instagram_password",
    "csv_filename": "accounts.csv"
}
```

Replace `"your_instagram_username"` and `"your_instagram_password"` with your Instagram credentials. The `csv_filename` should point to a CSV file containing the Instagram URLs you want to send messages to.

3. Install the Chrome WebDriver using the `webdriver-manager`:

```bash
webdriver-manager install chrome
```

## Usage

1. Load Instagram accounts from a CSV file by running:

```bash
python your_script_name.py
```

This will populate the `accounts_url` list with Instagram profile URLs from the specified CSV file.

2. Run the messaging bot by executing:

```bash
python your_script_name.py
```

The script will log in to your Instagram account, and for each profile URL in the `accounts_url` list, it will send a predefined message.

## Customization

You can customize the following aspects of the script:

- The message to send can be modified in the `send_message` function.

- The list of Instagram profile URLs to send messages to can be defined in the `accounts_url` list.

- The structure and content of the `credentials.json` file can be adjusted to match your Instagram account details.

## Disclaimer

Please use this script responsibly and respect Instagram's terms of service and community guidelines. Automated actions on Instagram may violate their policies, so be cautious when using this script.
