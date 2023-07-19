import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def setup(request):
    # Set up the WebDriver
    driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser
    driver.maximize_window()  # Maximize the browser window
    driver.implicitly_wait(10)  # Set implicit wait time for element locating

    # Pass the WebDriver instance to the test class
    request.cls.driver = driver
    yield
    driver.quit()  # Quit the browser after all tests complete

@pytest.mark.usefixtures("setup")
class TestSimpleApplication:
    def test_login(self):
        # Open the login page
        self.driver.get("https://ticker-app-production.up.railway.app/login")

        # Fill in the login form
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys("demo@demo.io")
        password_field.send_keys("password")
        submit_button.click()

    # Verify that the login is successful
    # welcome_message = self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Welcome')]")
    # assert welcome_message.text == "Welcome, testuser!"

    def test_search(self):
        # Perform a search
        search_field = self.driver.find_element(By.ID, "search")
        search_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        search_field.send_keys("automation testing")
        search_button.click()

        # Verify the search results
        search_results = self.driver.find_elements(By.CLASS_NAME, "result-item")
        assert len(search_results) > 0

if __name__ == '__main__':
    pytest.main()