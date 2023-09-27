from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://localhost:3128')

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get('http://whatismyip.com')
    
    ip_element = driver.find_element(By.XPATH, '//*[@id="ipv4"]')
    
    your_ip = ip_element.text
    
    print(f"Seu endereço IP através da proxy é: {your_ip}")
    
except Exception as e:
    print(f"Erro ao verificar a proxy: {str(e)}")

finally:
    driver.quit()

