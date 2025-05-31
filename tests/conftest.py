import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup_driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    # driver = webdriver.Chrome(service=ChromeServ(ChromeDriverManager().install()))
    driver.maximize_window()

    url = "https://www.google.com/search?q=calculator&oq=calculator&ags=chrome..69i57j0i433i6j69i65.2216j0j7&sourceid=chrome&ie=UTF-8"
    driver.get(url)
    input("Solve the CAPTCHA and press Enter to continue...\n")
    if request.cls is not None:
       request.cls.driver = driver

    def teardown_fin():
       print("Quit webdriver")
       driver.quit()
    request.addfinalizer(teardown_fin)

