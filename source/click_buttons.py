
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Buttons:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def click_button_0(self):
        # click on button 0
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[1]/div/div').click()

    def click_button_1(self):
        # click on button 1
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div').click()

    def click_button_2(self):
        # click on button 2
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div').click()

    def click_button_3(self):
        # click on button 3
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[3]/div/div').click()

    def click_button_4(self):
        # click on button 4
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[1]/div/div').click()

    def click_button_5(self):
        # click on button 5
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[2]/div/div').click()

    def click_button_6(self):
        # click on button 6
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[3]/div/div').click()

    def click_button_7(self):
        # click on button 7
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[1]/div/div').click()

    def click_button_8(self):
        # click on button 8
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[2]/div/div').click()

    def click_button_9(self):
        # click on button 9
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[3]/div/div').click()

    def click_button_dot(self):
        # click on button "."
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[2]/div/div').click()

    def click_button_equal(self):
        # click on button "="
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div').click()

    def click_button_plus(self):
        # click on button "+"
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[4]/div/div').click()

    def click_button_minus(self):
        # click on button "-"
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[4]/div/div').click()

    def click_button_multiply(self):
        # click on button "×"
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div').click()

    def click_button_divide(self):
        # click on button "÷"
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[4]/div/div').click()

    def click_button_CE(self):
        # click on button CE
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[1]/td[4]/div/div[2]').click()

    def click_button_AC(self):
        # click on button AC
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[1]/td[4]/div/div[1]').click()

    # this method is out of scope.
    def click_button_left_parentheses(self):
        # click on button "("
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[1]/td[1]/div/div').click()

    def locate_button(self, button):
        # locate button
        if button == "0":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[1]/div/div')
        elif button == "1":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div')
        elif button == "2":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div')
        elif button == "3":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[3]/div/div')
        elif button == "4":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[1]/div/div')
        elif button == "5":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[2]/div/div')
        elif button == "6":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[3]/div/div')
        elif button == "7":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[1]/div/div')
        elif button == "8":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[2]/div/div')
        elif button == "9":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[3]/div/div')
        elif button == ".":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[2]/div/div')
        elif button == "=":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div')
        elif button == "+":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[4]/div/div')
        elif button == "-":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[4]/div/div')
        elif button == "*":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div')
        elif button == "/":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[4]/div/div')
        elif button == "AC":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[1]/td[4]/div/div[1]')
        elif button == "CE":
            return self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[1]/td[4]/div/div[2]')

    def right_click_button(self, button):
        button_loc = self.locate_button(button)
        self.action.move_to_element(button_loc).perform()
        self.action.context_click(button_loc).perform()
