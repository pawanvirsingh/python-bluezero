import sys
import os

from sense_hat import SenseHat

sys.path.insert(0,
                os.path.split(os.path.dirname(os.path.realpath(__file__)))[0])
from bluezero import peripheral


sense = SenseHat()


def get_sensehat_pressure():
    if pressure_characteristic.notifying:
        print(int(sense.pressure))
        pressure_characteristic.send_notify_event(int(sense.pressure))
        return True
    else:
        return False

def ble_change_update_rate():
    peripheral.GObject.timeout_add(1000, get_sensehat_pressure)



pressure_service = peripheral.Service(
    '11118000-2222-3333-4444-555566667777',
    True)


# Pressure
pressure_characteristic = peripheral.Characteristic(
    '11118010-2222-3333-4444-555566667777',
    ['read', 'notify'],
    pressure_service,
    value=0)

pressure_characteristic.add_notify_event(ble_change_update_rate)
# Descriptor
pressure_descriptor = peripheral.UserDescriptor('Pressure', pressure_characteristic)
pressure_characteristic.add_descriptor(pressure_descriptor)

# Update Frequency
update_characteristic = peripheral.Characteristic(
    '11118011-2222-3333-4444-555566667777',
    ['read', 'write'],
    pressure_service,
    value=1020)
update_characteristic.add_write_event(ble_change_update_rate)
# Descriptor
update_descriptor = peripheral.UserDescriptor('update rate', update_characteristic)
update_characteristic.add_descriptor(update_descriptor)

pressure_service.add_characteristic(pressure_characteristic)
pressure_service.add_characteristic(update_characteristic)

app = peripheral.Application()
app.add_service(pressure_service)

app.add_device_name('SensePressure')

# Start service and advertise
try:
    app.start()
except KeyboardInterrupt:
    print('KeyboardInterrupt')
finally:
    app.stop()
    print('finally')
