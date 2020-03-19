class AddProductResults:
    def __init__(self, driver):
        self.driver = driver
        self.number_products = "/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/p[1]/span"
        self.to_pay = "/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/p[2]/span"

    def product_amount(self):
        self.products = self.driver.find_element_by_xpath(self.number_products).text
        self.pay = self.driver.find_element_by_xpath(self.to_pay).text

    def product_value(self):

        print("\nIlosc Produktow: ", self.products)
        print("Do Zaplaty:", self.pay)
