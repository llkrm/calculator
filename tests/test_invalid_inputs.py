import pytest
import inspect
from time import sleep
from source import click_buttons
from source import output_field
from source import send_keys


@pytest.mark.usefixtures("setup_driver")
class TestInvalidInputs:


    def teardown_method(self):
        """
        Sending key "backspace" 5000 times to clear long strings of characters.
        Expecting 0 in the result field.
        This test method is used as a teardown_method, called after each test, to reset the output field.
        """
        print("In " + inspect.currentframe().f_code.co_name)

        # need to send "backspace" 5000 times to clear the output
        send_keys.UserKeys(self.driver).send_key_backspace_multiple(5000)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0'
        sleep(1)

    def test_invalid_keys(self):
        """
        Testing some invalid keys that should not produce any output:
        @#$&_{}|[]\"':;?><~` and all of the F keys: F1 - F12
        Expecting "0" in the result field.
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "-"
        send_keys.UserKeys(self.driver).send_multiple_keys(r"@#$&_{}|[]\"':;?><~`")
        send_keys.UserKeys(self.driver).send_F_keys()
        send_keys.UserKeys(self.driver).send_key_CTRL()
        send_keys.UserKeys(self.driver).send_key_ALT()
        send_keys.UserKeys(self.driver).send_key_SHIFT()
        send_keys.UserKeys(self.driver).send_key_TAB()

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0'
        sleep(1)


    def test_random_keys(self):
        """
        Testing random keys sent 100 times to stress the application and check that it does not crash.
        @#$&_{}|[]dKg?Aksrkjt%*^!':;?><~` times 100
        Expecting "0" in the result field.
        """
        print("Running " + inspect.currentframe().f_code.co_name)

        # send key "-"
        send_keys.UserKeys(self.driver).send_multiple_keys(r"@#$&_{}|[]dKg?Aksrkjt%*^!':;?><~`" * 100)

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output != '0'
        sleep(1)

    @pytest.mark.parametrize("button", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "=", "+", "-", "*", "/", "AC", "CE"])
    def test_buttons_mouse_right_click(self, button):
        """
        Testing right click on each button. No change expected in the result field.
        Expecting "0" in the result field.
        """
        print("Running " + inspect.currentframe().f_code.co_name)
        try:
            # right click on <button>
            click_buttons.Buttons(self.driver).right_click_button(button)
        except:
            print(f"Button {button} not present")

        # read value from the output field
        output = output_field.OutputField(self.driver).read_value()

        # check if the actual value is equal with the expected value
        assert output == '0'
        sleep(1)
