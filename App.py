# %%
import time
from pprint import pprint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.chrome.options import Options


all_itens = []

opisao = webdriver.ChromeOptions()
opisao.add_argument("--headless=new")

driver = webdriver.Chrome(options=opisao)

local = input("oque você quer comprar: ")

driver.get(f"https://www.kabum.com.br/busca/{local}")

itens = driver.find_elements(By.XPATH, "//span[@class='text-base font-semibold text-gray-800' and @aria-hidden='false']")

for item in itens:
        all_itens.append(item.text)

df = pd.read_excel('achados.xlsx', names=['Valor'])
df.apply(all_itens)

pprint(all_itens)
# %%
