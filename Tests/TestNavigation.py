
from selenium import webdriver
import time

import SCADA.request
from Pages.PidPage import PidPage


def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8088/data/perspective/client/SIM_City_GW")
    time.sleep(3)
    return driver


def check_pid_header(driver, location_id):
    page_inst = PidPage(driver, '', '')
    page_inst.navigate_to(location_id)
    location_details = SCADA.request.location_details(location_id)
    location_name = location_details['locationName']
    assert location_name in page_inst.get_header_label(), "Header location name is incorrect"


def test_all_pid_headers():
    driver = open_browser()
    locations = SCADA.request.all_locations()
    for location in locations:
        location_id = location['locationID']
        location_type_id = location['locationTypeID']
        if int(location_type_id) == 6:
            check_pid_header(driver,location_id)
