from time import sleep
import pytest
import inspect
from source import click_buttons
from source import output_field

@pytest.mark.usefixtures("setup_driver")
class TestButtons:


    def teardown_method(self):
        """
        Testing button CE.
        Expecting 0 in the result field.
        This test method is used as a teardown_method, called after each test, to reset the result field.
        :return: None
        """
        print("In " + inspect.currentframe().f_code.co_name)

        # click on button CE
        click_buttons.Buttons(self.driver).click_button_CE()

        # read value from the output field
        button_CE_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_CE_output == '0'
        sleep(1)


    def test_button_0(self):
        """
        Testing button 0.
        Expecting 0 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 0
        click_buttons.Buttons(self.driver).click_button_0()

        # read value from the output field
        button_0_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_0_output == '0'
        sleep(1)


    def test_button_1(self):
        """
        Testing button 1.
        Expecting 1 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 1
        click_buttons.Buttons(self.driver).click_button_1()

        # read value from the output field
        button_1_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_1_output == '1'
        sleep(1)


    def test_button_2(self):
        """
        Testing button 2.
        Expecting 2 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 2
        click_buttons.Buttons(self.driver).click_button_2()

        # read value from the output field
        button_2_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_2_output == '2'
        sleep(1)


    def test_button_3(self):
        """
        Testing button 3.
        Expecting 3 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 3
        click_buttons.Buttons(self.driver).click_button_3()

        # read value from the output field
        button_3_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_3_output == '3'
        sleep(1)


    def test_button_4(self):
        """
        Testing button 4.
        Expecting 4 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 4
        click_buttons.Buttons(self.driver).click_button_4()

        # read value from the output field
        button_4_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_4_output == '4'
        sleep(1)


    def test_button_5(self):
        """
        Testing button 5.
        Expecting 5 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 5
        click_buttons.Buttons(self.driver).click_button_5()

        # read value from the output field
        button_5_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_5_output == '5'
        sleep(1)


    def test_button_6(self):
        """
        Testing button 6.
        Expecting 6 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 6
        click_buttons.Buttons(self.driver).click_button_6()

        # read value from the output field
        button_6_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_6_output == '6'
        sleep(1)


    def test_button_7(self):
        """
        Testing button 7.
        Expecting 7 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 7
        click_buttons.Buttons(self.driver).click_button_7()

        # read value from the output field
        button_7_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_7_output == '7'
        sleep(1)


    def test_button_8(self):
        """
        Testing button 8.
        Expecting 8 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 8
        click_buttons.Buttons(self.driver).click_button_8()

        # read value from the output field
        button_8_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_8_output == '8'
        sleep(1)


    def test_button_9(self):
        """
        Testing button 9.
        Expecting 9 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button 9
        click_buttons.Buttons(self.driver).click_button_9()

        # read value from the output field
        button_9_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_9_output == '9'
        sleep(1)


    def test_button_dot(self):
        """
        Testing button "." (dot).
        Expecting "." in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button "."
        click_buttons.Buttons(self.driver).click_button_dot()

        # read value from the output field
        button_dot_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_dot_output == '.'
        sleep(1)


    def test_button_equal(self):
        """
        Testing button "=" (equal).
        Expecting 0 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button "="
        click_buttons.Buttons(self.driver).click_button_equal()

        # read value from the output field
        button_equal_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_equal_output == '0'
        sleep(1)


    def test_button_plus(self):
        """
        Testing button "+" (plus).
        Expecting "0 +" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button "+"
        click_buttons.Buttons(self.driver).click_button_plus()

        # read value from the output field
        button_plus_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_plus_output == '0 +'
        sleep(1)


    def test_button_minus(self):
        """
        Testing button "-" (minus).
        Expecting "0 -" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button "-"
        click_buttons.Buttons(self.driver).click_button_minus()

        # read value from the output field
        button_minus_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_minus_output == '0 -'
        sleep(1)


    def test_button_multiply(self):
        """
        Testing button "×" (multiply).
        Expecting "0 ×" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button "×"
        click_buttons.Buttons(self.driver).click_button_multiply()

        # read value from the output field
        button_multiply_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_multiply_output == '0 ×'
        sleep(1)


    def test_button_divide(self):
        """
        Testing button "÷" (divide).
        Expecting "0 ÷" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # click on button "÷"
        click_buttons.Buttons(self.driver).click_button_divide()

        # read value from the output field
        button_divide_output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert button_divide_output == '0 ÷'
        sleep(1)


