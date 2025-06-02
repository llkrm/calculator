import pytest
from selenium import webdriver
from twocaptcha import TwoCaptcha
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeServ


@pytest.fixture(scope="class")
def setup_driver(request):
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--incognito")
    #driver = webdriver.Chrome(options=chrome_options)

    # instantiate the webdriver
    driver = webdriver.Chrome(service=ChromeServ(ChromeDriverManager().install()))

    # Load the target page
    captcha_page_url = "https://www.google.com/search?q=calculator&oq=calculator&ags=chrome..69i57j0i433i6j69i65.2216j0j7&sourceid=chrome&ie=UTF-8"
    driver.get(captcha_page_url)
    driver.maximize_window()

    # PLEASE UNCOMMENT THIS SECTION OF THE CODE TO SOLVE CAPTCHA AUTOMATICALLY, MAY REQUIRE YOUR OWN API_KEY FOR 2captcha
    """
    # Solve the Captcha
    print("Solving Captcha")
    solver = TwoCaptcha("8a49669361a44d0b35ea0fa823a27d81") # this is the API_KEY that may need to be replaced
    response = solver.recaptcha(sitekey='6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO', url=captcha_page_url)
    code = response['code']
    print(f"Successfully solved the Captcha. The solve code is {code}")

    # Set the solved Captcha
    recaptcha_response_element = driver.find_element(By.ID, 'g-recaptcha-response')
    driver.execute_script(f'arguments[0].value = "{code}";', recaptcha_response_element)

    # Submit the form
    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="verify"]')
    submit_btn.click()
    """

    input("Solve the CAPTCHA and press Enter to continue...\n")

    if request.cls is not None:
       request.cls.driver = driver

    def teardown_fin():
       print("Quit webdriver")
       driver.quit()
    request.addfinalizer(teardown_fin)

