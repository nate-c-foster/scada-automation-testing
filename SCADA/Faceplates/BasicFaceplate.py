
from selenium.webdriver.common.by import By

from SCADA.Symbols.BasicComponent import BasicComponent
from Components.PerspectiveComponents.Displays.Label import Label
from Components.BasicComponent import BasicPerspectiveComponent
import SCADA.request

CSS_ID_PREFIX = "faceplate"

# add id at root and begin with symbol-analog-input-root--provider--tagPath
# for tagPath (replace  space with _      / with - )

class BasicFaceplate:

    def __init__(self, driver, rootTagPath):
        self.driver = driver
        self.rootTagPath = rootTagPath

    # this is inherited
    def open_tab(self, name):
        css_id = CSS_ID_PREFIX + '-tab-' + name + SCADA.request.tag_to_css_id(self.rootTagPath)
        self._tab = BasicPerspectiveComponent(driver=self.driver, locator=(By.ID, css_id ))
        self._tab.click(binding_wait_time=2)
        

    # # this is inherited
    # def get_label(self):
    #     css_id = CSS_ID_PREFIX + '-label' + SCADA.request.tag_to_css_id(self.rootTagPath)
    #     self._label = Label(driver=self.driver, locator=(By.ID, css_id ))
    #     label_text = self._label.get_text()
    #     return label_text

    # def get_value(self):
    #     css_id = CSS_ID_PREFIX + '-value' + SCADA.request.tag_to_css_id(self.rootTagPath)
    #     self._value = Label(driver=self.driver, locator=(By.ID, css_id ))
    #     value_text = self._value.get_text()
    #     return value_text

    # def get_units(self):
    #     css_id = CSS_ID_PREFIX + '-units' + SCADA.request.tag_to_css_id(self.rootTagPath)
    #     self._units = Label(driver=self.driver, locator=(By.ID, css_id ))
    #     units_text = self._units.get_text()
    #     return units_text

    # # this is inherited
    # def open_faceplate(self):
    #     css_id = CSS_ID_PREFIX + '-root' + SCADA.request.tag_to_css_id(self.rootTagPath)
    #     self._root = BasicPerspectiveComponent(driver=self.driver, locator=(By.ID, css_id ))
    #     self._root.click(binding_wait_time=2)

    # # this is inherited
    # def is_alarm_icon_visible(self):
    #     css_id = CSS_ID_PREFIX + '-alarm-icon' + SCADA.request.tag_to_css_id(self.rootTagPath)
    #     self._alarm_icon = BasicPerspectiveComponent(driver=self.driver, locator=(By.ID, css_id ))
    #     visibility = self._alarm_icon.get_css_property('visibility')
    #     return visibility == 'visible'
