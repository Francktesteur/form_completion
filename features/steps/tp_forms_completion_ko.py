from multiprocessing import context

from behave.configuration import options
from selenium.webdriver.support.ui import Select
from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

delay = 2
url='file:///C:/Users/fbouchaud2024/Downloads/TP/TP/05%20-%20Forms%20Completion/inscription.html'

@given("Je suis sur la page formulaire d'inscrition Eni Tech Community avec les champs apparants")
def ouvrir_moteur_recherche(context):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    sleep(delay)
    context.driver.implicitly_wait(delay)


@when('Je saisis un email  "{email}" dans le champ email')
def set_enter_email(context, email):
    context.driver.find_element(By.NAME, 'inputEmail4').send_keys(email)


@step('Je saisis un mot de passe  "{password}" dans le champ mot de passe')
def set_enter_password(context, password):
    context.driver.find_element(By.NAME, 'inputPassword4').send_keys(password)

@step('Je saisis une adresse "{adresse}" dans le champ addresse')
def set_enter_adresse(context, adresse):
    context.driver.find_element(By.NAME, 'inputAddress').send_keys(adresse)

@step('Je saisis un code postal  "{zipcode}" dans le champ code postal')
def set_enter_zipcode(context, zipcode):
    context.driver.find_element(By.NAME, 'inputZip').send_keys(zipcode)

@step('Je saisis une ville "<city>" dans le champ ville')
def set_enter_city(context, city):
    context.driver.find_element(By.NAME, 'inputCity').send_keys(city)

@step('Je choisis "<states>" dans la liste déroulante pays')
def set_enter_state(context, state):
    context.driver.find_element(By.NAME, 'inputCity').send_keys(state)