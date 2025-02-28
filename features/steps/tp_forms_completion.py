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
url=('file:///C:/Users/fbouchaud2024/Downloads/TP/TP/05%20-%20Forms%20Completion/inscription.html')

#use_step_matcher("re")


@given("Je suis sur la page formulaire d\'inscrition Eni Tech Community")
# def step_impl(context):
def ouvrir_moteur_recherche(context):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    sleep(delay)
    context.driver.implicitly_wait(delay)

#raise NotImplementedError(u'STEP: Given Je suis sur la page formulaire d\'inscrition Eni Tech Community')


@when('Je saisis un email valide "{email}" dans le champ email')
def saisir_email(context, email):
    context.driver.find_element(By.NAME, 'inputEmail4').send_keys(email)
    sleep(delay)


@step('Je saisis un mot de passe valide "{motdepasse}" dans le champ mot de passe')
def saisir_motdepasse(context, motdepasse):
    context.driver.find_element(By.NAME, 'inputPassword4').send_keys(motdepasse)
    sleep(delay)


@step('Je saisis une adresse valide "{addresse}" dans le champ addresse')
def saisir_addresse(context, addresse):
    context.driver.find_element(By.NAME, 'inputAddress').send_keys(addresse)
    sleep(delay)


@step('Je saisis un code postal valide "{zipcode}" dans le champ code postal')
def saisir_zipcode(context, zipcode):
    context.driver.find_element(By.NAME, 'inputZip').send_keys(zipcode)
    sleep(delay)


@step('Je saisis une ville "{city}" dans le champ ville')
def saisir_city(context, city):
    context.driver.find_element(By.NAME, 'inputCity').send_keys(city)
    sleep(delay)


@step('Je choisis "{state}" dans la liste déroulante pays')
def saisir_state(context, state):
    context.driver.find_element(By.ID, 'inputState').send_keys(state)
    sleep(delay)


@step("Je clique sur le bouton valider")
def step_when_i_click_the_submit_button(context):
    submit_button = context.driver.find_element(By.ID, "connexionToastBtn")
    submit_button.click()
    input()
    sleep(delay)


