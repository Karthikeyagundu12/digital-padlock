import json
import win32api
import win32file

CONFIG_FILE = "app/config.json"

def get_registered_usb():
    """Load saved USB serial number."""
    try:
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
            return data.get("usb_id")
    except:
        return None

def detect_usb():
    """Return serial number of first connected USB (removable) drive, else None."""
    drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
    for drive in drives:
        drive_type = win32file.GetDriveType(drive)
        if drive_type == win32file.DRIVE_REMOVABLE:  # Only USB drives
            try:
                vol_info = win32api.GetVolumeInformation(drive)
                serial = str(vol_info[1])  # volume serial number
                return serial
            except:
                continue
    return None

def register_usb():
    """Register first found removable USB drive as the key."""
    drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
    for drive in drives:
        drive_type = win32file.GetDriveType(drive)
        if drive_type == win32file.DRIVE_REMOVABLE:
            try:
                vol_info = win32api.GetVolumeInformation(drive)
                serial = str(vol_info[1])
                with open(CONFIG_FILE, "w") as f:
                    json.dump({"usb_id": serial}, f)
                print(f"✅ USB Key Registered: {serial}")
                return serial
            except:
                continue
    print("⚠️ No USB drive found to register.")
    return None
