class AddProducts:

    def __init__(self, driver):
        self.driver = driver
        self.glasess_xpath = "//div[@class='input-group input-group-sm']//input"
        self.glasess_button_click = "/html/body/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div/span/button"
        self.ball_xpath_input ="/html/body/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div/input"
        self.ball_button_click = "/html/body/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div/span/button"
        self.foto_xpath_input = "/html/body/div/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/input"
        self.foto_button_click = "/html/body/div/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/span/button"

    def choice_glasess(self, amount):
        self.driver.find_element_by_xpath(self.glasess_xpath).clear()
        self.driver.find_element_by_xpath(self.glasess_xpath).send_keys(amount)
        self.driver.find_element_by_xpath(self.glasess_button_click).click ()

    def chocie_ball(self, amount):
        self.driver.find_element_by_xpath(self.ball_xpath_input).clear()
        self.driver.find_element_by_xpath(self.ball_xpath_input).send_keys(amount)
        self.driver.find_element_by_xpath(self.ball_button_click ).click()

    def choice_foto(self, amount):
        self.driver.find_element_by_xpath(self.foto_xpath_input).clear()
        self.driver.find_element_by_xpath(self.foto_xpath_input).send_keys(amount)
        self.driver.find_element_by_xpath(self.foto_button_click).click()