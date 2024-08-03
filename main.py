
from selenium import webdriver
import time


from Tests.TestPidHeader import TestPidHeader



def test_pid_header():
    driver = webdriver.Chrome()
   # driver.get("http://localhost:8088/data/perspective/client/SCADA_Ventura/SCADA/64")
   # time.sleep(5)

    testPidHeader = TestPidHeader(driver, "Dos Vientos Booster",64)
    testPidHeader.test_header()


test_pid_header()