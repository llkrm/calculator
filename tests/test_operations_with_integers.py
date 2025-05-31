from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServ
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest
import inspect
from source import click_buttons
from source import output_field

@pytest.mark.usefixtures("setup_driver")
class TestOperations:

    def teardown_method(self):
        """
        Testing button AC. Expecting 0 in the result field.
        This test method is used as a teardown_method, called after each test, to reset the result field.
        :return: None
        """
        print("In " + inspect.currentframe().f_code.co_name)

        # click on button AC
        click_buttons.Buttons(self.driver).click_button_AC()

        # read value from the output field
        button_AC_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_AC_output == '0'
        sleep(1)


    def test_add_two_positive_nos(self):
        """
        Testing the addition of two positive numbers:
        1 + 5 = 6
        Expecting 6 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button +
        click_buttons.Buttons(self.driver).click_button_plus()
        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '6'
        sleep(1)


    def test_add_one_positive_one_negative_no(self):
        """
        Testing the addition of one positive and one negative number:
        2 + (-3) = -1
        Expecting -1 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()
        # click on button +
        click_buttons.Buttons(self.driver).click_button_plus()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 3
        click_buttons.Buttons(self.driver).click_button_3()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-1'
        sleep(1)


    def test_add_one_negative_one_positive_no(self):
        """
        Testing the addition of one negative and one positive number:
        -3 + 5 = 2
        Expecting 2 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 3
        click_buttons.Buttons(self.driver).click_button_3()
        # click on button +
        click_buttons.Buttons(self.driver).click_button_plus()
        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '2'
        sleep(1)


    def test_add_two_negative_nos(self):
        """
        Testing the addition of two negative numbers:
        -3 + (- 5) = -8
        Expecting -8 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 3
        click_buttons.Buttons(self.driver).click_button_3()
        # click on button +
        click_buttons.Buttons(self.driver).click_button_plus()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-8'
        sleep(1)


    def test_subtract_two_positive_nos(self):
        """
        Testing the subtraction of two positive numbers:
        1 - 5 = -4
        Expecting -4 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-4'
        sleep(1)


    @pytest.mark.skip("Cannot test without left parentheses. Out of scope.")
    def test_subtract_one_positive_one_negative_no(self):
        """
        Testing the subtraction of one positive and one negative number:
        4 - (-7) = 11
        Expecting 11 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button (
        click_buttons.Buttons(self.driver).click_button_left_parentheses()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '11'
        sleep(1)


    def test_subtract_one_negative_one_positive_no(self):
        """
        Testing the subtraction of one negative and one positive number:
        -8 - 7 = -15
        Expecting -15 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 8
        click_buttons.Buttons(self.driver).click_button_8()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-15'
        sleep(1)


    @pytest.mark.skip("Cannot test without left parentheses. Out of scope.")
    def test_subtract_two_negative_nos(self):
        """
        Testing the subtraction of two negative numbers:
        -4 - (-7) = 3
        Expecting 3 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button (
        click_buttons.Buttons(self.driver).click_button_left_parentheses()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '3'
        sleep(1)


    def test_multiply_two_positive_nos(self):
        """
        Testing the multiplication of two positive numbers:
        1 * 5 = 5
        Expecting 5 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button "×"
        click_buttons.Buttons(self.driver).click_button_multiply()
        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '5'
        sleep(1)


    def test_multiply_one_positive_one_negative_no(self):
        """
        Testing the multiplication of one positive and one negative number:
        4 * (-7) = -28
        Expecting -28 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button "×"
        click_buttons.Buttons(self.driver).click_button_multiply()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-28'
        sleep(1)


    def test_multiply_one_negative_one_positive_no(self):
        """
        Testing the multiplication of one negative and one positive number:
        -4 * 7 = -28
        Expecting -28 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button "×"
        click_buttons.Buttons(self.driver).click_button_multiply()
        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-28'
        sleep(1)


    def test_multiply_two_negative_nos(self):
        """
        Testing the multiplication of two negative numbers:
        -1 * (-5) = 5
        Expecting 5 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button "×"
        click_buttons.Buttons(self.driver).click_button_multiply()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '5'
        sleep(1)


    def test_divide_two_positive_nos(self):
        """
        Testing the division of two positive numbers:
        10 / 5 = 2
        Expecting 2 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button 0
        click_buttons.Buttons(self.driver).click_button_0()
        # click on button "÷"
        click_buttons.Buttons(self.driver).click_button_divide()
        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '2'
        sleep(1)


    def test_divide_one_positive_one_negative_no(self):
        """
        Testing the division of one positive and one negative number:
        6 / (-2) = -3
        Expecting -1.5 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 6
        click_buttons.Buttons(self.driver).click_button_6()
        # click on button "÷"
        click_buttons.Buttons(self.driver).click_button_divide()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-3'
        sleep(1)


    def test_divide_one_negative_one_positive_no(self):
        """
        Testing the division of one negative and one positive number:
        -4 / 2 = -2
        Expecting -28 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button "÷"
        click_buttons.Buttons(self.driver).click_button_divide()
        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-2'
        sleep(1)


    def test_divide_two_negative_nos(self):
        """
        Testing the division of two negative numbers:
        -12 / (-4) = 3
        Expecting 3 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()
        # click on button "÷"
        click_buttons.Buttons(self.driver).click_button_divide()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '3'
        sleep(1)