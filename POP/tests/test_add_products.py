import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from POP.pages.add_products import AddProducts
from POP.pages.add_products_results import AddProductResults

class TestAddProducts:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(r'C:\Users\gonta\PycharmProjects\Selenium\seleniumddemo\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_add_products(self, setup):
        self.driver.get('https://testingcup.pgs-soft.com/task_1')
        add_products = AddProducts(self.driver)
        add_products.choice_glasess(10)
        add_products.chocie_ball(2)
        add_products.choice_foto(1)

        check_results = AddProductResults(self.driver)
        check_results.product_amount()
        check_results.product_value()


