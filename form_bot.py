# BOT for SQL destination creation and mapping

# necessary modules and libraries:
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time, pandas as pd


def pdm_destination(dmformpath, dbname, tblname):
    wdpath = Service("webdriver.exe...")
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--kiosk")
    driver = webdriver.Firefox(service=wdpath,
                               options=options)
    driver.get(dmformpath)
    
    # username:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "user_remember_me_1")))
    
    driver.find_element(By.ID, 'user_remember_me_1').click()
    mail = 'xxx'
    mail_enter = driver.find_element(By.ID, 'user_email')
    mail_enter.send_keys(mail)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "commit")))
    driver.find_element(By.NAME, 'commit').click()
    
    # password:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "user_password")))
    
    pswd = 'yyy'
    pswd_enter = driver.find_element(By.ID, 'user_password')
    pswd_enter.send_keys(pswd)
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "commit")))
    driver.find_element(By.NAME, 'commit').click()
    
    # sql destination creation:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "create_destination_link")))
    driver.find_element(By.ID, 'create_destination_link').click()
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "sql_transport-list-item")))
    driver.find_element(By.ID, 'sql_transport-list-item').click()
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "xml_format-list-item")))
    driver.find_element(By.ID, 'xml_format-list-item').click()
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "destination_description")))
    
    dstn = driver.find_element(By.ID, 'destination_description')
    dstn.send_keys('xxx')
    dstn.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "sql_transport_host")))
    
    host = driver.find_element(By.ID, 'sql_transport_host')
    host.send_keys('zzz')
    host.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "sql_transport_username")))
    
    usrnm = driver.find_element(By.ID, 'sql_transport_username')
    usrnm.send_keys('aaa')
    usrnm.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "sql_transport_password")))
    
    pswd1 = 'qqq'
    pswd_enter1 = driver.find_element(By.ID, 'sql_transport_password')
    pswd_enter1.send_keys(pswd1)
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "sql_transport_port")))
    
    port = driver.find_element(By.ID, 'sql_transport_port')
    port.send_keys('ccc')
    port.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "sql_transport_database_name")))
    
    dbnm = driver.find_element(By.ID, 'sql_transport_database_name')
    dbnm.send_keys(dbname)
    dbnm.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "fetch-table-names")))
    driver.find_element(By.ID, 'fetch-table-names').click()
    
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sql_transport_table_name"]'))).click()
    select = Select(driver.find_element(By.XPATH, '//*[@id="sql_transport_table_name"]'))
    select.select_by_visible_text(tblname)
    
   
    # mapping process:
    path0 = 'form_id.xlsx'
    df0 = pd.read_excel(path0)    
    list0 = list(df0.dm_table_id)
    dm_table_id_list = list0

    path1 = 'sql_ud.xlsx'
    df1 = pd.read_excel(path1)    
    list1 = list(df1.sql_table_id)
    sql_table_id_list = list1
    
    time.sleep(2)

    for x, y in zip (dm_table_id_list, sql_table_id_list):
        field_enter = driver.find_element(By.ID, y)
        field_enter.send_keys(x)
    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "create_new_destination_button")))
    driver.find_element(By.ID, 'create_new_destination_button').click()

    driver.quit()
    
    print('Destination has been created and mapped with a SQL database/table!')
    
# calling main function:
pdm_destination("url",
                'dbname',
                'tblname')