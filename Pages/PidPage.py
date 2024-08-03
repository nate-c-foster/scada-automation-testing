
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from Components.PerspectiveComponents.Displays.Tree import Tree
#from Components.PerspectiveComponents.Common.Icon import Icon
from Components.PerspectiveComponents.Displays.Label import Label
from Pages.PerspectivePageObject import PerspectivePageObject

class PidPage(PerspectivePageObject):
    def __init__(self, driver, gateway_address, page_config_path):
            super().__init__(driver=driver, gateway_address=gateway_address, page_config_path=page_config_path)
            self._header_label = Label(driver=driver, locator=(By.ID, "pid-header-label"))
           # self._header_trend_icon = Icon(driver=driver, locator=(By.ID, "pid-header-icon-open-trending-tool"))
            self._nav_tree = Tree(driver=driver, locator=(By.ID, "scada-nav-tree"))


    def navigate_to(self, location_name, location_id):
        self.driver.get(self.url)
        time.sleep(5)
        nav_icon = self.driver.find_element(By.ID, "nav-tree-icon")
        nav_icon.click()
        time.sleep(3)
        self._nav_tree.click_item_label("Dos Vientos", 3)



    # def is_rendered_header_trend_icon(self):
    #      self._header_trend_icon.is_rendered()

    def get_header_label(self):
        label_text = self._header_label.get_text()
        print("Header Label: " + label_text)
        return label_text