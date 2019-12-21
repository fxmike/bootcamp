import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
url = 'https://risk.ostc.com/Members/Calendar.aspx'

def enter():                    #funkcja naciskająca "enter"
    pyautogui.PAUSE = 5
    pyautogui.press('enter')

driver = webdriver.Firefox()
driver.get(url)
html = driver.execute_script('return document.documentElement.outerHTML') #javascript call to get the HTML related to JS
sel_soup = BeautifulSoup(html, 'html.parser')

def login_OSTC():
    driver.find_element_by_id('Username').send_keys('michal.gluszczuk@ostc.com')
    driver.find_element_by_id ('Password').send_keys('GUstaw!@345')
    driver.find_element_by_id ('Password').send_keys(enter())


login_OSTC()

