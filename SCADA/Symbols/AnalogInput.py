
from SCADA.Symbols.BasicComponent import BasicComponent


# add id at root and begin with symbol-analog-input-root--provider--tagPath
# for tagPath (replace  space with _      / with - )

class AnalogInput(BasicComponent):
    pass

    # this is inherited
    def get_label():
        pass

    def get_value():
        pass

    def get_units():
        pass

    # this is inherited
    def open_faceplate():
        pass

    # this is inherited
    def is_alarm_active():
        pass
        # check visibility of symbol
        # check border


    