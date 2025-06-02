import pytest
import inspect
from time import sleep
from source import output_field
from source import send_keys


@pytest.mark.usefixtures("setup_driver")
class TestOperationsWithKeys:


    def teardown_method(self):
        """
        Testing key "backspace" 5 times.
        Expecting 0 in the result field.
        This test method is used as a teardown_method, called after each test, to reset the result field.
        :return: None
        """
        print("In " + inspect.currentframe().f_code.co_name)

        # need to send "backspace" 15 times to clear the output
        send_keys.UserKeys(self.driver).send_key_backspace_multiple(15)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0'
        sleep(1)

    def test_add_two_large_negative_positive_nos(self):
        """
        Testing the addition of two very large negative and positive numbers:
        -8e+42 + 1e+42 = -7e+42
        Expecting -7e+42 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "-"
        send_keys.UserKeys(self.driver).send_key_minus()
        # send key 8
        send_keys.UserKeys(self.driver).send_key_8()
        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()
        # send keys for 1e+42
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(42)

        # send key "+"
        send_keys.UserKeys(self.driver).send_key_plus()

        # send keys for 1e+42
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(42)

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-7e+42'
        sleep(1)

    def test_add_two_small_positive_decimal_nos(self):
        """
        Testing the addition of two very small positive decimal numbers:
        1e-42 + 9e-42 = 1e-41
        Expecting 1e-41 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send keys for 1e-42
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(-42)

        # send key "+"
        send_keys.UserKeys(self.driver).send_key_plus()

        # send key 9
        send_keys.UserKeys(self.driver).send_key_9()
        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()
        # send keys for 1e-42
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(-42)

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '1e-41'
        sleep(1)


    def test_subtract_two_large_positive_nos(self):
        """
        Testing the subtraction of two very large positive numbers:
        9.33e+42 - 1.77e+42 = 7.56e+42
        Expecting 7.56e+42 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)


        # send keys "9.33"
        send_keys.UserKeys(self.driver).send_multiple_keys("9.33")
        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()
        # send keys for 1e+42
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(42)

        # send key "+"
        send_keys.UserKeys(self.driver).send_key_minus()

        # send keys "1.77"
        send_keys.UserKeys(self.driver).send_multiple_keys("1.77")
        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()
        # send keys for 1e+42
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(42)

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '7.56e+42'
        sleep(1)


    def test_subtract_two_small_positive_decimal_nos(self):
        """
        Testing the subtraction of two very small positive decimal numbers:
        1e-42 - 9e-42 = -8e-42
        Expecting -8e-42 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send keys for 1e-42
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(-42)

        # send key "-"
        send_keys.UserKeys(self.driver).send_key_minus()

        # send key 9
        send_keys.UserKeys(self.driver).send_key_9()
        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()
        # send keys for 1e-42
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(-42)

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-8e-42'
        sleep(1)


    def test_multiply_two_large_negative_nos(self):
        """
        Testing the multiplication of two very large negative numbers:
        -1e+980 * (-9e+81) = 9e+1061
        Expecting "Infinity" in the result field, as it exceeds the max value allowed.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "-"
        send_keys.UserKeys(self.driver).send_key_minus()
        # send keys for 1e+80
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(980)

        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()

        # send key "-"
        send_keys.UserKeys(self.driver).send_key_minus()
        # send key 9
        send_keys.UserKeys(self.driver).send_key_9()
        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()
        # send keys for 1e-42
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(81)

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == 'Infinity'
        sleep(1)

    def test_multiply_two_small_negative_positive_decimal_nos(self):
        """
        Testing the multiplication of two very small positive and negative numbers:
        -1e-999 * 9e-1000 = -9e-1999
        Expecting "0" in the result field, as it exceeds the min value allowed.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "-"
        send_keys.UserKeys(self.driver).send_key_minus()
        # send keys for 1e-999
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(-999)

        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()

        # send key 9
        send_keys.UserKeys(self.driver).send_key_9()
        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()
        # send keys for 1e-1000
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(-1000)

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0'
        sleep(1)


    def test_divide_two_large_positive_nos(self):
        """
        Testing the division of two very large positive numbers:
        1e+100 / 9e+99 = 1.111111e+198
        Expecting 1.111111e+198 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send keys for 1e+100
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(100)

        # send key "÷"
        send_keys.UserKeys(self.driver).send_key_divide()

        # send key 9
        send_keys.UserKeys(self.driver).send_key_9()
        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()
        # send keys for 1e+99
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(99)

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '1.111111e+198'
        sleep(1)


    def test_divide_two_negative_nos(self):
        """
        Testing the division of two negative numbers:
        -8e-1000 / (-2e+999) = 4e-1999
        Expecting "0" in the result field, as it exceeds the min value allowed.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "-"
        send_keys.UserKeys(self.driver).send_key_minus()
        # send key 8
        send_keys.UserKeys(self.driver).send_key_8()
        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()
        # send keys for 1e-1000
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(-1000)

        # send key "÷"
        send_keys.UserKeys(self.driver).send_key_divide()

        # send key "-"
        send_keys.UserKeys(self.driver).send_key_minus()
        # send key 2
        send_keys.UserKeys(self.driver).send_key_2()
        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()
        # send keys for 1e+999
        send_keys.UserKeys(self.driver).send_10_to_the_power_of(999)

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0'
        sleep(1)


    def test_add_zero(self):
        """
        Testing the addition of 0:
        7 + 0 = 7
        Expecting "7" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key 7
        send_keys.UserKeys(self.driver).send_key_7()

        # send key "+"
        send_keys.UserKeys(self.driver).send_key_plus()

        # send key 0
        send_keys.UserKeys(self.driver).send_key_0()

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '7'
        sleep(1)


    def test_subtract_zero(self):
        """
        Testing the subtraction of 0:
        7 - 0 = 7
        Expecting "7" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key 7
        send_keys.UserKeys(self.driver).send_key_7()

        # send key "-"
        send_keys.UserKeys(self.driver).send_key_minus()

        # send key 0
        send_keys.UserKeys(self.driver).send_key_0()

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '7'
        sleep(1)


    def test_multiply_by_zero(self):
        """
        Testing the multiplication of a number by 0:
        7 * 0 = 0
        Expecting "0" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key 7
        send_keys.UserKeys(self.driver).send_key_7()

        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()

        # send key 0
        send_keys.UserKeys(self.driver).send_key_0()

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0'
        sleep(1)


    def test_divide_by_zero_positive_no(self):
        """
        Testing the division of a number by 0:
        7 / 0 = not supported
        Expecting "Infinity" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key 7
        send_keys.UserKeys(self.driver).send_key_7()

        # send key "÷"
        send_keys.UserKeys(self.driver).send_key_divide()

        # send key 0
        send_keys.UserKeys(self.driver).send_key_0()

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == 'Infinity'
        sleep(1)


    def test_divide_by_zero_negative_no(self):
        """
        Testing the division of a number by 0:
        -7 / 0 = not supported
        Expecting "-Infinity" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "-"
        send_keys.UserKeys(self.driver).send_key_minus()
        # send key 7
        send_keys.UserKeys(self.driver).send_key_7()

        # send key "÷"
        send_keys.UserKeys(self.driver).send_key_divide()

        # send key 0
        send_keys.UserKeys(self.driver).send_key_0()

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()
        sleep(1)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-Infinity'
        sleep(1)