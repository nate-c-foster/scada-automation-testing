from Tests.TestNavigation import test_all_pid_headers
from Tests.TestSymbol import test_ai
import SCADA.request

#test_all_pid_headers()
test_ai(64, '[SCADA]SIM City/Wells/Well 1/Flow')

#print(SCADA.request.tag_to_css_id('[SCADA]SIM City/Distribution/Booster PS/Pressure/Control/DeviceStatus/Output')['cssId'])