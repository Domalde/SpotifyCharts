from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
cod = []
navegador.get('https://spotifycharts.com/regional/global/daily/latest')
MUSIC_SEARCH = "Envolver"
chart = open(r"Top200.txt","a")
DATA_CHART = navegador.find_element(By.XPATH, '//*[@id="content"]/div/div/div/span/div[2]/div/div/div/div[3]/div').text
chart.write(f'{DATA_CHART}\n')

for I in range(1,74):
    lista_urls = navegador.find_element(By.XPATH, f'//*[@id="content"]/div/div/div/span/div[2]/div/div/div/div[1]/ul/li[{I}]').get_attribute('data-value')
    cod.append(lista_urls)

for url_list in cod:
    navegador.get(f"https://spotifycharts.com/regional/{url_list}/daily/latest")
    for J in range(1,200):
        try:
            MUSIC = navegador.find_element(By.XPATH,f'//*[@id="content"]/div/div/div/span/table/tbody/tr[{J}]/td[4]/strong').text
            if MUSIC == MUSIC_SEARCH:
                POSITION = navegador.find_element(By.XPATH, f'//*[@id="content"]/div/div/div/span/table/tbody/tr[{J}]/td[2]').text
                COUNTRY_NAME = navegador.find_element(By.XPATH, '//*[@id="content"]/div/div/div/span/div[2]/div/div/div/div[1]/div').text
                chart.write(f'{COUNTRY_NAME}: {POSITION}\n')
                break
        except:
            break

navegador.close()
chart.write(f'\n')
chart.close()


    