from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Inicializar o driver do navegador Chrome
@given('estou no navegador chrome')
def step_estou_no_navegador_chrome(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.implicitly_wait(10)

# Acessar a página de registro (substituindo com URL do Sauce Demo)
@given('estou na pagina de registro')
def step_estou_na_pagina_de_registro(context):
    context.driver.get("https://www.saucedemo.com/")

# Preencher o formulário de registro com dados existentes
@when('eu preencho o formulario de registro com dados existentes')
def step_preencho_formulario_com_dados_existentes(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()

# Preencher o formulário de registro com dados dinâmicos (substituindo com campos do Sauce Demo)
@when('eu preencho o formulario de registro com dados existentes com "{nome}" e "{sobrenome}"')
def step_preencho_formulario_com_dados_dinamicos(context, nome, sobrenome):
    context.driver.find_element(By.ID, "user-name").send_keys(nome)
    context.driver.find_element(By.ID, "password").send_keys(sobrenome)
    context.driver.find_element(By.ID, "login-button").click()

# Clicar no botão de registro (login no caso do Sauce Demo)
@when('clico no botao de registro')
def step_clico_no_botao_de_registro(context):
    context.driver.find_element(By.ID, "login-button").click()

# Verificar a mensagem de erro (ajustar para a mensagem do Sauce Demo)
@then('devo ver uma mensagem de erro informando que o usuario ja existe')
def step_verificar_mensagem_de_erro(context):
    mensagem_erro = context.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Epic sadface: Username and password do not match any user in this service" in mensagem_erro

# Acessar a página de registro via plataforma específica (ajustando para Sauce Demo)
@given('estou na pagina de registro via "{plataforma}"')
def step_estou_na_pagina_de_registro_via_plataforma(context, plataforma):
    context.driver.get("https://www.saucedemo.com/")  # Usando a mesma URL para todas as plataformas no exemplo

# Fechar o navegador após os testes
def after_scenario(context, scenario):
    context.driver.quit()
