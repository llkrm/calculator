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
class TestOperationsWithDecimals:

    def teardown_method(self):
        """
        Testing button AC or CE. Expecting 0 in the result field.
        This test method is used as a teardown_method, called after each test, to reset the result field.
        :return: None
        """
        print("In " + inspect.currentframe().f_code.co_name)
        try:
            # click on button AC
            click_buttons.Buttons(self.driver).click_button_AC()
        except:
            print("Button AC not present.")

        try:
            # click on button CE
            click_buttons.Buttons(self.driver).click_button_CE()
        except:
            print("Button CE not present.")

        # read value from the output field
        button_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_output == '0'
        sleep(1)


    def test_add_two_positive_decimal_nos(self):
        """
        Testing the addition of two positive decimal numbers:
        1.1 + 5.5 = 6.6
        Expecting 6.6 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()

        # click on button +
        click_buttons.Buttons(self.driver).click_button_plus()

        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '6.6'
        sleep(1)


    def test_add_one_positive_one_negative_decimal_no(self):
        """
        Testing the addition of one positive and one negative decimal number:
        2.5 + (-3.0) = -0.5
        Expecting -0.5 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()

        # click on button +
        click_buttons.Buttons(self.driver).click_button_plus()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()

        # click on button 3
        click_buttons.Buttons(self.driver).click_button_3()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 0
        click_buttons.Buttons(self.driver).click_button_0()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-0.5'
        sleep(1)


    def test_add_one_negative_one_positive_decimal_no(self):
        """
        Testing the addition of one negative and one positive decimal number:
        -3.00001 + 5.9999 = 2.99989
        Expecting 2.99989 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 3
        click_buttons.Buttons(self.driver).click_button_3()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(4):
            # click on button 0
            click_buttons.Buttons(self.driver).click_button_0()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()

        # click on button +
        click_buttons.Buttons(self.driver).click_button_plus()

        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(4):
            # click on button 9
            click_buttons.Buttons(self.driver).click_button_9()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '2.99989'
        sleep(1)


    def test_add_two_negative_decimal_nos(self):
        """
        Testing the addition of two negative decimal numbers:
        -3.9 + (- 5.1) = -9
        Expecting -9 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 3
        click_buttons.Buttons(self.driver).click_button_3()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 9
        click_buttons.Buttons(self.driver).click_button_9()

        # click on button +
        click_buttons.Buttons(self.driver).click_button_plus()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()

        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-9'
        sleep(1)


    def test_subtract_two_positive_decimal_nos(self):
        """
        Testing the subtraction of two positive decimal numbers:
        1.0 - 5.9 = -4.9
        Expecting -4.9 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 0
        click_buttons.Buttons(self.driver).click_button_0()

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()

        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 9
        click_buttons.Buttons(self.driver).click_button_9()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-4.9'
        sleep(1)


    @pytest.mark.skip("Cannot test without left parentheses. Out of scope.")
    def test_subtract_one_positive_one_negative_decimal_no(self):
        """
        Testing the subtraction of one positive and one negative decimal number:
        4.2 - (-7.2) = 11.4
        Expecting 11.4 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button (
        click_buttons.Buttons(self.driver).click_button_left_parentheses()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()

        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '11.4'
        sleep(1)


    def test_subtract_one_negative_one_positive_decimal_no(self):
        """
        Testing the subtraction of one negative and one positive decimal number:
        -8.9 - 7.9 = -16.8
        Expecting -16.8 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 8
        click_buttons.Buttons(self.driver).click_button_8()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 9
        click_buttons.Buttons(self.driver).click_button_9()

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()

        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 9
        click_buttons.Buttons(self.driver).click_button_9()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-16.8'
        sleep(1)


    @pytest.mark.skip("Cannot test without left parentheses. Out of scope.")
    def test_subtract_two_negative_decimal_nos(self):
        """
        Testing the subtraction of two negative decimal numbers:
        -4.01 - (-7.09) = 3.08
        Expecting 3.08 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 0
        click_buttons.Buttons(self.driver).click_button_0()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button (
        click_buttons.Buttons(self.driver).click_button_left_parentheses()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()

        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 0
        click_buttons.Buttons(self.driver).click_button_0()
        # click on button 9
        click_buttons.Buttons(self.driver).click_button_9()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '3.08'
        sleep(1)


    def test_multiply_two_positive_decimal_nos(self):
        """
        Testing the multiplication of two positive decimal numbers:
        1.005 * 5.99999 = 6.02998995
        Expecting 6.02998995 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(2):
            # click on button 0
            click_buttons.Buttons(self.driver).click_button_0()
        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()

        # click on button "×"
        click_buttons.Buttons(self.driver).click_button_multiply()

        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(5):
            # click on button 9
            click_buttons.Buttons(self.driver).click_button_9()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '6.02998995'
        sleep(1)


    def test_multiply_one_positive_one_negative_decimal_no(self):
        """
        Testing the multiplication of one positive and one negative decimal number:
        4.00001 * (-7.00001) = -28.0001100001
        Expecting -28.0001100001 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(4):
            # click on button 0
            click_buttons.Buttons(self.driver).click_button_0()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()

        # click on button "×"
        click_buttons.Buttons(self.driver).click_button_multiply()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()

        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(4):
            # click on button 0
            click_buttons.Buttons(self.driver).click_button_0()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-28.0001100001'
        sleep(1)


    def test_multiply_one_negative_one_positive_decimal_no(self):
        """
        Testing the multiplication of one negative and one positive decimal number:
        -4.99999 * 7.11111 = -35.5554788889
        Expecting -35.5554788889 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(5):
            # click on button 9
            click_buttons.Buttons(self.driver).click_button_9()

        # click on button "×"
        click_buttons.Buttons(self.driver).click_button_multiply()

        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(5):
            # click on button 1
            click_buttons.Buttons(self.driver).click_button_1()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-35.5554788889'
        sleep(1)


    def test_multiply_two_negative_decimal_nos(self):
        """
        Testing the multiplication of two negative decimal numbers:
        -1.00009 * (-5.00009) = 5.0005400081
        Expecting 5.0005400081 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(4):
            # click on button 0
            click_buttons.Buttons(self.driver).click_button_0()
        # click on button 9
        click_buttons.Buttons(self.driver).click_button_9()

        # click on button "×"
        click_buttons.Buttons(self.driver).click_button_multiply()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()

        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(4):
            # click on button 0
            click_buttons.Buttons(self.driver).click_button_0()
        # click on button 9
        click_buttons.Buttons(self.driver).click_button_9()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '5.0005400081'
        sleep(1)


    def test_divide_two_positive_decimal_nos(self):
        """
        Testing the division of two positive decimal numbers:
        10.9 / 5.9 = 1.84745762712
        Expecting 1.84745762712 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button 0
        click_buttons.Buttons(self.driver).click_button_0()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 9
        click_buttons.Buttons(self.driver).click_button_9()

        # click on button "÷"
        click_buttons.Buttons(self.driver).click_button_divide()

        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 9
        click_buttons.Buttons(self.driver).click_button_9()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '1.84745762712'
        sleep(1)


    def test_divide_one_positive_one_negative_decimal_no(self):
        """
        Testing the division of one positive and one negative decimal number:
        6.001 / (-2.001) = -2.99900049975
        Expecting -2.99900049975 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 6
        click_buttons.Buttons(self.driver).click_button_6()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(2):
            # click on button 0
            click_buttons.Buttons(self.driver).click_button_0()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()

        # click on button "÷"
        click_buttons.Buttons(self.driver).click_button_divide()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()

        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(2):
            # click on button 0
            click_buttons.Buttons(self.driver).click_button_0()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-2.99900049975'
        sleep(1)


    def test_divide_one_negative_one_positive_decimal_no(self):
        """
        Testing the division of one negative and one positive decimal number:
        -4.0 / 2.99999 = -1.33333777779
        Expecting -1.33333777779 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        # click on button 0
        click_buttons.Buttons(self.driver).click_button_0()

        # click on button "÷"
        click_buttons.Buttons(self.driver).click_button_divide()

        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(5):
            # click on button 9
            click_buttons.Buttons(self.driver).click_button_9()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-1.33333777779'
        sleep(1)


    def test_divide_two_negative_decimal_nos(self):
        """
        Testing the division of two negative decimal numbers:
        -12.11111 / (-4.11199) = 2.94531601487
        Expecting 2.94531601487 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()
        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()
        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(5):
            # click on button 1
            click_buttons.Buttons(self.driver).click_button_1()

        # click on button "÷"
        click_buttons.Buttons(self.driver).click_button_divide()
        # click on button -
        click_buttons.Buttons(self.driver).click_button_minus()

        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()
        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()
        for i in range(3):
            # click on button 1
            click_buttons.Buttons(self.driver).click_button_1()
        for i in range(2):
            # click on button 9
            click_buttons.Buttons(self.driver).click_button_9()

        # click on button =
        click_buttons.Buttons(self.driver).click_button_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '2.94531601487'
        sleep(1)