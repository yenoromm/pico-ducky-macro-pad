from board import *
import digitalio
import storage

noStorageStatus = True
noStoragePin = digitalio.DigitalInOut(GP14)
noStoragePin.switch_to_input(pull=digitalio.Pull.UP)
noStorageStatus = noStoragePin.value

if(noStorageStatus == True):
    # don't show USB drive to host PC
    storage.disable_usb_drive()
    print("Disabling USB drive")
else:
    # normal boot
    print("USB drive enabled")
