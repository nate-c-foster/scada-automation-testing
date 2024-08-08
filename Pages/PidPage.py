
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from Components.PerspectiveComponents.Displays.Tree import Tree
#from Components.PerspectiveComponents.Common.Icon import Icon
from Components.PerspectiveComponents.Displays.Label import Label
from Pages.PerspectivePageObject import PerspectivePageObject
import SCADA.request
from SCADA.Navigation.NavTree import NavTree
from config import PID_HEADER_LABEL_ID

class PidPage(PerspectivePageObject):


    def __init__(self, driver, gateway_address, page_config_path):
            super().__init__(driver=driver, gateway_address=gateway_address, page_config_path=page_config_path)
            self._header_label = Label(driver=driver, locator=(By.ID, PID_HEADER_LABEL_ID ))

    def navigate_to(self, location_id):
        nav_tree = NavTree(self.driver)
        nav_tree.navigate_to(location_id)

    def get_header_label(self):
        label_text = self._header_label.get_text()
        print("Header Label: " + label_text)
        return label_text