from .base_page import BasePage
from .locators import ProductsPageLocators


class ProductPage(BasePage):
    def add_goods_to_basket(self):
        add_button = self.browser.find_element(*ProductsPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_alert_with_product_name(self):
        assert self.is_element_present(*ProductsPageLocators.PRODUCT_NAME_ALERT), 'нет сообщения о добавлении товара ' \
                                                                                  'в корзину'

    def should_be_alert_with_product_price(self):
        assert self.is_element_present(*ProductsPageLocators.PRODUCT_PRICE_IN_ALERT), 'нет сообщения о цене ' \
                                                                                      'добавленного товара'

    def should_be_product_price_in_alert(self):
        price_in_alert = self.browser.find_element(*ProductsPageLocators.PRODUCT_PRICE_IN_ALERT)
        price_in_card = self.browser.find_element(*ProductsPageLocators.PRODUCT_PRICE)
        assert price_in_alert.text == price_in_card.text, 'цена товара в уведомлении не соответсвует цене в карточке ' \
                                                          'товара'

    def should_be_product_name_in_alert(self):
        name_in_alert = self.browser.find_element(*ProductsPageLocators.PRODUCT_NAME_ALERT)
        name_in_card = self.browser.find_element(*ProductsPageLocators.PRODUCT_NAME)
        assert name_in_alert.text == name_in_card.text, 'название товара в каточке не соответсвует названию в ' \
                                                        'уведомлении'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductsPageLocators.PRODUCT_NAME_ALERT), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductsPageLocators.PRODUCT_NAME_ALERT), "алерт с сообщением не удалился"



