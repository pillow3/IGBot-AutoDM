# python 3.10.6
# selenium 4.14.0
# webdriver-manager  4.0.1

import json
import time
import csv
import tkinter as tk
from tkinter import *

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Allows search similar to beautiful soup: find_all
from selenium.webdriver.common.by import By

# ----------------------------------------------------------------------------------

# Load JSON
with open('credentials.json') as json_file:
    credentials_json = json.load(json_file)

# Avoid cookies & Enable automation
options = webdriver.ChromeOptions()
# options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Start driver Chrome
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Login Variables
insta_url = "https://www.instagram.com/"
cookies_button_XPATH = '//button[text()="Allow all cookies"]'
login_button_XPATH = '//*[@id="loginForm"]/div/div[3]/button/div'

# Prompts
username = credentials_json['username']
pasword = credentials_json['password']
csv_filename = credentials_json['csv_filename']

# Load accounts from csv Variables
accounts_url = []
accounts_test = ['https://instagram.com/ibaillanos', 'https://instagram.com/ibaillanos', 'https://instagram.com/ibaillanos', 'https://instagram.com/ibaillanos', 'https://instagram.com/s4vitarx',
                 'https://instagram.com/pillow3code', 'https://instagram.com/pillow3code']
accounts_test_cesar = ['https://instagram.com/cabronazi', 'https://instagram.com/pillow3code']

# Send message Variables
message_button_XPATH = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div'
message_button_noFriend_XPATH = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div'
name_account_XPATH = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[2]/a/div/div/span/span'
message_bar_XPATH = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p'
notifications_popup_button_XPATH = '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'


def load_accounts_from_csv():
    with open(f'spam-accounts-csv/{csv_filename}', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            instagram_url = row.get('instagram_url', '')  # Obtenemos el valor de la columna 'instagram_url'
            if instagram_url:  # Verificamos si el valor no está vacío
                accounts_url.append(instagram_url)
    print(f'File {csv_filename} loaded.')


def login():
    driver.implicitly_wait(2)
    driver.get(insta_url)

    time.sleep(1)

    cookies_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, cookies_button_XPATH)))
    cookies_button.click()
    print('Acept cookies')

    time.sleep(1)

    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
    username_field.send_keys(username)

    time.sleep(1)

    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
    password_field.send_keys(pasword)

    time.sleep(1)

    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_button_XPATH)))
    login_button.click()

    time.sleep(1)


def send_message():
    print("Send message executed")
    time.sleep(2)
    # Profile send message button
    try:
        message_button = driver.find_element(By.XPATH, message_button_noFriend_XPATH)
        message_button.click()
        print("Message button clicked (No friend account)")
    except NoSuchElementException:
        driver.find_element(By.XPATH, message_button_XPATH).click()
        print("Message button clicked (Friend account)")

    time.sleep(2)

    #  # Close popup notifications
    # try:
    #     notifications_button = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, notifications_popup_button_XPATH)))
    #     notifications_button.click()
    #     print("Notifications button popup closed")
    # except TimeoutException:
    #     print(
    #         "There is no notification button to close to   close")

    time.sleep(2)

    # Fetch account name
    name_account = driver.find_element(By.XPATH, name_account_XPATH).text
    print("Name account fetched")

    time.sleep(2)

    # Type message
    custom_message = f"Hola! {name_account}, soy un pequeño script de Python que itera por vuestras cuentas para ver si funciona, " \
                     f"por ejemplo tu nombre se escribió automáticamente (Test)"
    message_bar = driver.find_element(By.XPATH, message_bar_XPATH)
    message_bar.send_keys(custom_message)
    print("Message typed")

    time.sleep(2)

    # Send message
    message_bar.send_keys(Keys.RETURN)
    print("Message sent")


def start_messaging_bot(file_csv):
    print('Start messaging bot')
    login()
    print('Login successful')
    time.sleep(5)
    for account in file_csv:
        print(f'Search account: {account} (From file: {csv_filename})')
        driver.get(account)
        time.sleep(1)
        send_message()
        time.sleep(1)


# START
load_accounts_from_csv()
start_messaging_bot(accounts_test)
