import sys
import os

sys.path.insert(0,
                os.path.split(os.path.dirname(os.path.realpath(__file__)))[0])
from bluezero import peripheral
from bluezero import tools

# Bluetooth
# Add beacon information
ukBaz_beacon = peripheral.Service('FEAA', True, type='broadcast')
service_data = tools.url_to_advert(
    'https://github.com/ukBaz',
    frame_type=0x10,
    tx_power=0xFF)
ukBaz_beacon.add_service_data(service_data)


# Add application
app = peripheral.Application()
app.add_service(ukBaz_beacon)

app.add_device_name('ukBazBeacon')

# Start service and advertise
try:
    app.start()
except KeyboardInterrupt:
    print('KeyboardInterrupt')
finally:
    app.stop()
    print('finally')
