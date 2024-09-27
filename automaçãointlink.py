#selenium for web scrapping and pyautogui/pygetwindow for mouse and keyboard manipulation

# duas classes span para verificar produto e local de estoque
# <span class="ng-binding"><b>Produto:</b> DM986-416  WI-FI ONU GPON </span>

#variáveis para armazenar = local de estoque, mac adress, cliente e produto (nome) 

#criar função para verificar se mensagem de observação spawnou depois de pesquisar o cliente e fechar ela

import pyperclip as pc

import pyautogui as pyautogui

import subprocess

import time

import pygetwindow as gw

import pandas as pd

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

#####################################################first part############################################

# Variables to open chrome instancy

service=Service()
options=webdriver.ChromeOptions()
driver=webdriver.Chrome(service=service, options=options)

url = "https://intlink.hubsoft.com.br/login"

driver.get(url)

time.sleep (2)

# Constants used to select pixels coordenates on the page

button_x = 455
button_y = 600

pyautogui.FAILSAFE= False

# Goes to username field

pyautogui.moveTo (button_x, button_y,  duration=1)
pyautogui.leftClick()
pyautogui.write ("richard.silva@clickip.com.br", interval=0.1)

pyautogui.moveTo (button_x - 0, button_y + 150, duration=1)

# Goes to password field

pyautogui.leftClick()
pyautogui.moveTo (button_x - 0, button_y + 50, duration=1)
pyautogui.leftClick()
pyautogui.write ("Ri21851619!",  interval=0.1)

# Goes to submit button

pyautogui.moveTo (button_x - 0, button_y + 170, duration=1)
pyautogui.leftClick()


# Goes to full open the page

pyautogui.moveTo (button_x + 420, button_y - 570, duration=1)
pyautogui.leftClick()

url_cliente = "https://intlink.hubsoft.com.br/cliente"

driver.get(url_cliente)

pyautogui.moveTo (button_x + 600, button_y - 150, duration=1)
pyautogui.leftClick()

pyautogui.moveTo (button_x + 600, button_y - 20, duration=1)
pyautogui.leftClick()

###############################################second part#################################################

excel_file = "C:/Users/Richard.silva/Downloads/names.xlsx"

# Pandas library reads the excel file 

data = pd.read_excel(excel_file)

# Retrives the current data on the xlsx datasheet and afterwards print on the terminal if the values of the tables were sucessful found

client_data = data["NomeRazaosocial"]

print (data)

# Opens a empty dictionary to organize the values

pasted_values = []

for index, row in data.iterrows():
 print(data.iterrows)
   
 item_to_paste = str(row["NomeRazaosocial"])

 print(f"Value to paste: { item_to_paste}")

###############################################third part#################################################
# uses pyperclip library to copy the itered data and pyautogui to paste the iterated value

 pc.copy(item_to_paste) 

 pyautogui.hotkey('ctrl', 'v')

 print(f"Copied item: {item_to_paste}")

# Moves to "status cadastro" and select option "todos"

 pyautogui.moveTo (button_x + 1000, button_y - 20, duration=1)
 pyautogui.leftClick()
 time.sleep(2)
 pyautogui.moveTo (button_x + 1000, button_y - 80, duration=1)
 pyautogui.leftClick()
 
# Moves to search icon and selects it

 pyautogui.moveTo (button_x + 1200, button_y - 40, duration=1)
 pyautogui.leftClick()
 time.sleep(3) 

########## ADVICE: when it finishes the process it will restart the loop
########## If not complete, it will get errors inside the selenium webdriver, most likely in search for XPATH value


# opens "VER" button by driver function, scrolling mouse and selects EQUIPAMENTOS button

 buttonVER = driver.find_element(By.XPATH, "//span[text()='Ver']")

 # it will be shown the tag that has a machine understanding and not readable human description.

 print (" Element was sucessfuly Found (button 'Ver', beware that the class is not human readable): "), print (buttonVER)
 buttonVER.click()
 pyautogui.moveTo (button_x + 1200, button_y + 240, duration=1)
 pyautogui.scroll(-400)
 pyautogui.moveTo (button_x + 1100, button_y + 240, duration=1)
 pyautogui.leftClick()

 # It will open the modal to see the product area

 pyautogui.moveTo(button_x + 1100, button_y - 40, duration=1)
 pyautogui.leftClick()

 # It will identify the product (if list will need to identify some more, and should add all the products) and them click the action button (open card to check products first)

 buttonPRODUCT1 = driver.find_element(By.XPATH, "//span[text()='ONU GPON DM986-414']")

 # It will be shown the tag that has a machine understanding and not readable human description.  

 print("Element was Found:(button 'Ver', class and tag is not human readable): "), print (buttonPRODUCT1)

 time.sleep (5)

 print ("after it completes down the function it will restart data.iterrows()")

 print ("beware that if not complete it will only restart and malfunction")
 
  

 


