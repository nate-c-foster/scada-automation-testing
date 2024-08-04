import time
from selenium.webdriver.common.by import By

import SCADA.request
from Components.PerspectiveComponents.Displays.Tree import Tree


class NavTree:

    NAV_TREE_ID = "scada-nav-tree"

    def __init__(self, driver):
        self.driver = driver
        self._nav_tree = Tree(driver=driver, locator=(By.ID, self.NAV_TREE_ID))


    def navigate_to(self, location_id):
        location_details = SCADA.request.location_details(location_id)
        location_name = location_details['locationName']
        short_name = location_details['shortName']
        if short_name:
            label = short_name
        else:
            label = location_name
        nav_icon = self.driver.find_element(By.ID, "nav-tree-icon")
        nav_icon.click()
        time.sleep(1)
        self._nav_tree.click_item_label(label, 2)