from selenium import webdriver
import time

import SCADA.request
from Pages.PidPage import PidPage
from SCADA.Symbols.AnalogInput import AnalogInput
from SCADA.Faceplates.BasicFaceplate import BasicFaceplate
from config import GATEWAY_IP


def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=1")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("http://{gateway_ip}:8088/data/perspective/client/SIM_City_GW".format(gateway_ip=GATEWAY_IP))
    time.sleep(3)
    return driver


def test_ai(location_id, rootTagPath):
    driver = open_browser()
    page_inst = PidPage(driver, '', '')
    page_inst.navigate_to(location_id)
    ai_symbol =  AnalogInput(driver,rootTagPath)
    print("Label: " + str(ai_symbol.get_label()))
    print("Value: " + str(ai_symbol.get_value()))
    print("Units: " + str(ai_symbol.get_units()))
    print("Alarm: " + str(ai_symbol.is_alarm_icon_visible()))
    ai_symbol.open_faceplate()
    ai_faceplate = BasicFaceplate(driver, rootTagPath)
    ai_faceplate.open_tab("Engineering")
