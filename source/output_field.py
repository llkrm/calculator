from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OutputField:

    def __init__(self, driver):
        self.driver = driver

    def read_value(self):
        # read value from the output field
        return self.driver.find_element(By.XPATH, '//*[@id="cwos"]').text

    def clear_output(self):
        # clear output field
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').clear()
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_selected(output_field))