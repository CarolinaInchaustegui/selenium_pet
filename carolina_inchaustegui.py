from cgitb import text
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

service = Service(executable_path="C:\Automatizacion\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

def flow_authorization_api_key():
    driver.get("https://petstore3.swagger.io/")

    driver.implicitly_wait(10)
    button_api_key_open_authorization = driver.find_element(By.XPATH, "//*[@id=\"swagger-ui\"]/section/div[2]/div[2]/div[2]/section/div[2]/button")
    button_api_key_open_authorization.click()

    text_api_key_value = driver.find_element(By.XPATH, "//*[@id=\"swagger-ui\"]/section/div[2]/div[2]/div[2]/section/div[2]/div/div[2]/div/div/div[2]/div[2]/form/div[1]/div/div[4]/section/input")
    text_api_key_value.send_keys("real_plaza")

    button_api_key_authorization = driver.find_element(By.XPATH, "//*[@id=\"swagger-ui\"]/section/div[2]/div[2]/div[2]/section/div[2]/div/div[2]/div/div/div[2]/div[2]/form/div[2]/button[1]")
    button_api_key_authorization.click()

    button_api_key_close_popup = driver.find_element(By.XPATH, "//*[@id=\"swagger-ui\"]/section/div[2]/div[2]/div[2]/section/div[2]/div/div[2]/div/div/div[1]/button")
    button_api_key_close_popup.click()

def api_pet_insert():
    driver.get("https://petstore3.swagger.io/#/pet/addPet")

    model_pet = "{\"id\": 11,\"name\": \"doggie demo\",\"category\": { \"id\": 1, \"name\": \"Dogs\" },\"photoUrls\": [\"string\"],\"tags\": [{ \"id\": 0, \"name\": \"string\" }],\"status\": \"available\"}"

    driver.implicitly_wait(20)
    button_try_it_out = WebDriverWait(driver, 10)\
        .until(ec.presence_of_element_located((By.XPATH, "//*[@id=\"operations-pet-addPet\"]/div[2]/div/div[2]/div[1]/div[2]/button")))
    button_try_it_out.click()

    driver.implicitly_wait(5)
    text_param_json = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-addPet\"]/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div/textarea")
    text_param_json.clear()
    text_param_json.send_keys(model_pet)

    button_execute = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-addPet\"]/div[2]/div/div[3]/button")
    button_execute.click()

    message_response_server = driver.find_element(By.XPATH, "//*[@id=\"post_pet_responses\"]/tbody/tr[1]/td[1]")\
        .text

    assert message_response_server == "200"

def api_pet_update():
    driver.get("https://petstore3.swagger.io/#/pet/updatePet")

    model_pet = "{\"id\": 11,\"name\": \"doggie actualizado\",\"category\": {\"id\": 1,\"name\": \"Dogs\"},\"photoUrls\": [\"string\"],\"tags\": [{\"id\": 0,\"name\": \"string\"}],\"status\": \"available\"}"

    driver.implicitly_wait(20)
    button_try_it_out = WebDriverWait(driver, 10)\
        .until(ec.presence_of_element_located((By.XPATH, "//*[@id=\"operations-pet-updatePet\"]/div[2]/div/div[2]/div[1]/div[2]/button")))
    button_try_it_out.click()

    driver.implicitly_wait(5)
    text_param_json = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-updatePet\"]/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div/textarea")
    text_param_json.clear()
    text_param_json.send_keys(model_pet)

    button_execute = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-updatePet\"]/div[2]/div/div[3]/button")
    button_execute.click()

    message_response_server = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-updatePet\"]/div[2]/div/div[4]/div[2]/div/div/table/tbody/tr/td[1]")\
        .text

    assert message_response_server == "200"

def api_pet_delete():
    driver.get("https://petstore3.swagger.io/#/pet/deletePet")

    driver.implicitly_wait(20)
    button_try_it_out = WebDriverWait(driver, 20)\
        .until(ec.presence_of_element_located((By.XPATH, "//*[@id=\"operations-pet-deletePet\"]/div[2]/div/div[1]/div[1]/div[2]/button")))
    button_try_it_out.click()

    driver.implicitly_wait(5)
    text_api_key = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-deletePet\"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input")
    text_api_key.send_keys("real_plaza")

    text_pet_id = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-deletePet\"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/input")
    text_pet_id.send_keys("11")

    button_execute = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-deletePet\"]/div[2]/div/div[2]/button")
    button_execute.click()

    message_response_server = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-deletePet\"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")\
        .text
    
    assert "200" in message_response_server

def api_pet_list_by_id():
    driver.get("https://petstore3.swagger.io/#/pet/getPetById")

    driver.implicitly_wait(20)
    button_try_it_out = WebDriverWait(driver, 20)\
        .until(ec.presence_of_element_located((By.XPATH, "//*[@id=\"operations-pet-getPetById\"]/div[2]/div/div[2]/div[1]/div[2]/button")))
    button_try_it_out.click()

    text_pet_id = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-getPetById\"]/div[2]/div/div[2]/div[2]/div/table/tbody/tr/td[2]/input")
    text_pet_id.clear()
    text_pet_id.send_keys("11")

    button_execute = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-getPetById\"]/div[2]/div/div[3]/button")
    button_execute.click()

    message_response_server = driver.find_element(By.XPATH, "//*[@id=\"operations-pet-getPetById\"]/div[2]/div/div[4]/div[2]/div/div/table/tbody/tr/td[1]")\
        .text
    
    assert message_response_server == "200"

flow_authorization_api_key()
api_pet_insert()
api_pet_update()
api_pet_list_by_id()
api_pet_delete()

driver.quit()
