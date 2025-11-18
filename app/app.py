import time
import usb_watch
import guard

def main():
    print("🔐 USBKeyGuard Started...")
    registered_id = usb_watch.get_registered_usb()

    while True:
        current_id = usb_watch.detect_usb()
        if current_id == registered_id:
            print("✅ USB Key detected! System Unlocked.")
            guard.unlock_screen()
        else:
            print("❌ USB Key missing! System Locked.")
            guard.lock_screen()

        time.sleep(5)  # check every 5 seconds

if __name__ == "__main__":
    main()
