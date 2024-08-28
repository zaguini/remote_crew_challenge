from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class WebBrowser:

    def __init__(self) -> None:
        self.driver = webdriver.Edge()

    def __access_ibge_site__(self):
        self.driver.get("https://www.ibge.gov.br/")

    def __access_ibge_download_page__(self):
        self.driver.find_element('id','nav-toggle').click()
        self.driver.find_element('xpath','//*[@id="menu_principal"]/ul/li[1]/span').click()
        self.driver.find_element('xpath','//*[@id="menu_principal"]/ul/li[1]/ul/li[7]/a').click()

    def __access_1991_census_data__(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "Censos")))
        self.driver.find_element('id','Censos').click()
        self.driver.find_element('xpath',"//*[contains(text(), 'Censo_Demografico_1991')]").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Censos/Censo_Demografico_1991/Indice_de_Gini_anchor'))).click()

    def download_zip_files(self,BRAZILIAN_STATES):
        self.__access_ibge_site__()
        self.__access_ibge_download_page__()
        self.__access_1991_census_data__()
        for state in BRAZILIAN_STATES:
            try:
                self.driver.find_element('xpath',f"//*[contains(text(), '{state}')]").click()
            except:
                try:
                    self.driver.find_element('id','cookie-btn').click()
                except:
                    pass
                self.driver.find_element('xpath',f"//*[contains(text(), '{state}')]").click()
            sleep(1)

