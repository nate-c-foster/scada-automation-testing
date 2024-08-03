

from Pages.PidPage import PidPage


class TestPidHeader:



    def __init__(self, driver, location_name, location_id):
        self.location_name = location_name
        self.location_id = location_id
        self.page_inst = PidPage(driver, 'http://localhost:8088', '/SCADA_Ventura')
        self.page_inst.navigate_to(location_name, location_id)


    def test_header(self):
        assert self.location_name in self.page_inst.get_header_label(), "Header location name is incorrect"