
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UserKeys:

    def __init__(self, driver):
        self.driver = driver

    def send_key_0(self):
        # send key 0
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("0")

    def send_key_1(self):
        # send key 1
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("1")

    def send_key_2(self):
        # send key 2
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("2")

    def send_key_3(self):
        # send key 3
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("3")

    def send_key_4(self):
        # send key 4
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("4")

    def send_key_5(self):
        # send key 5
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("5")

    def send_key_6(self):
        # send key 6
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("6")

    def send_key_7(self):
        # send key 7
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("7")

    def send_key_8(self):
        # send key 8
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("8")

    def send_key_9(self):
        # send key 9
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("9")

    def send_key_dot(self):
        # send key "."
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys(".")

    def send_key_equal(self):
        # send key "="
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("=")

    def send_key_plus(self):
        # send key "+"
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("+")

    def send_key_minus(self):
        # send key "-"
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("-")

    def send_key_multiply(self):
        # send key "*"
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("*")

    def send_key_divide(self):
        # send key "/"
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("/")

    def send_key_backspace(self):
        # send key "Backspace"
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys(Keys.BACK_SPACE)

    def send_key_enter(self):
        # send key "Enter"
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys(Keys.ENTER)

    def send_letters(self):
        # send all alphabet keys
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("qwertyuiopasdfghjklzxcvbnm")

    def send_key_backspace_multiple(self, n=2):
        # send key "Backspace" <n> times. Default for "n" is 2.
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys([Keys.BACK_SPACE] * n)

    def send_all_numeric_keys(self):
        # send all 10 numeric keys: 1234567890
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div').send_keys("1234567890")