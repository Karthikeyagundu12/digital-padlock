#  Digital Padlock with USB Authentication

The **Digital Padlock** is a smart security system that unlocks only when a specific USB device is connected.  
Your USB acts as the **physical key**, making this a simple and effective access-control solution.

---

##  Features

-  Unlocks only with the correct USB device  
-  Acts like a physical key (USB = digital key)  
-  Beginner-friendly setup and code  
-  Works on Windows/Linux  
 -  Can be connected to hardware (Arduino, Raspberry Pi, servo lock, relay, solenoid)

---

##  Technologies Used

- **Python**
- **USB detection (Vendor ID + Product ID)**
- **Custom au

---

## How It Works

1. You insert your personal USB device.
2. The program reads its **Vendor ID (VID)** and **Product ID (PID)**.
3. If the stored ID matches → **Lock Opens**  
4. If mismatched or removed → **Lock Stays Locked**


## Setup Instructions

### 1️Clone the Repository

git clone https://github.com/Karthikeyagundu12/digital-padlock.git
cd digital-padlock

Copy code

### Install Requirements

pip install -r requirements.txt



###  Run the Program

python main.py

## Registering Your USB Key

1. Insert your USB.
2. Run the USB listener:



##  Registering Your USB Key

1. Insert your USB.
2. Run the USB listener:

##  Contributing

Contributions, ideas, and pull requests are welcome!  
Feel free to open an issue if you find any problems.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## devloped by

**Karthikeya Gundu**  
GitHub: [Karthikeyagundu12](https://github.com/Karthikeyagundu12
