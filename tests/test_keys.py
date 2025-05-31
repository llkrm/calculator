import pytest
import inspect
from time import sleep
from source import output_field
from source import send_keys


@pytest.mark.usefixtures("setup_driver")
class TestKeys:


    def teardown_method(self):
        """
        Testing key "backspace" 26 times.
        Expecting 0 in the result field.
        This test method is used as a teardown_method, called after each test, to reset the result field.
        :return: None
        """
        print("In " + inspect.currentframe().f_code.co_name)

        # need to send "backspace" 26 times to clear any possible output from test_alphabet_letters test
        send_keys.UserKeys(self.driver).send_key_backspace_multiple(26)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0'
        sleep(1)


    def test_numeric_keys(self):
        """
        Testing all 10 numeric keys.
        Expecting 1234567890 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key 1
        send_keys.UserKeys(self.driver).send_all_numeric_keys()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '1234567890'
        sleep(1)


    def test_key_dot(self):
        """
        Testing key ".".
        Expecting "." in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key 1
        send_keys.UserKeys(self.driver).send_key_dot()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '.'
        sleep(1)


    def test_key_equal(self):
        """
        Testing key "=".
        Expecting "0" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "="
        send_keys.UserKeys(self.driver).send_key_equal()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0'
        sleep(1)


    def test_key_plus(self):
        """
        Testing key "+".
        Expecting "0 +" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "+"
        send_keys.UserKeys(self.driver).send_key_plus()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0 +'
        sleep(1)


    def test_key_minus(self):
        """
        Testing key "-".
        Expecting "-" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "-"
        send_keys.UserKeys(self.driver).send_key_minus()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '-'
        sleep(1)


    def test_key_multiply(self):
        """
        Testing key "*".
        Expecting "0 ×" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "*"
        send_keys.UserKeys(self.driver).send_key_multiply()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0 ×'
        sleep(1)


    def test_key_divide(self):
        """
        Testing key "/".
        Expecting "0 ÷" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "/"
        send_keys.UserKeys(self.driver).send_key_divide()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0 ÷'
        sleep(1)


    def test_alphabet_letters(self):
        """
        Testing all alphabet letters.
        Expecting a different from "0" value in the result field, due to shortcuts for other operations
        that cannot be disabled.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send all 26 letters
        send_keys.UserKeys(self.driver).send_letters()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output != '0'
        sleep(1)


    def test_key_backspace(self):
        """
        Testing key "backspace".
        Expecting "0" in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key 3
        send_keys.UserKeys(self.driver).send_key_3()

        # send key backspace
        send_keys.UserKeys(self.driver).send_key_backspace()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0'
        sleep(1)


    def test_key_enter(self):
        """
        Testing key "enter" using addition of two numbers:
        3 + 1 <enter> 4
        Expecting 4 in the result field.
        :return: None
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key 3
        send_keys.UserKeys(self.driver).send_key_3()
        # send key "+"
        send_keys.UserKeys(self.driver).send_key_plus()
        # send key 1
        send_keys.UserKeys(self.driver).send_key_1()
        # send key enter
        send_keys.UserKeys(self.driver).send_key_enter()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '4'
        sleep(1)
