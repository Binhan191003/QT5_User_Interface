
# 🖥️ Smart Home Device Control Interface (Qt5 + PyQt5)

This project is a graphical interface built using **Python** and **PyQt5** to simulate and control household electronic devices. It provides functionalities for toggling devices, switching TV channels, adjusting air conditioner levels, and viewing simulated environmental sensor data such as temperature and humidity. The interface is designed for classroom projects or smart home demonstrations.

---

## 📷 GUI Overview

![Smart Home GUI](images/59f59383-3da6-4de2-a7c2-d87cbe5430eb.png)

---

## 🎯 Features

✅ Control simulated devices:
- **Lamp**: Turn ON/OFF  
- **TV**: Power toggle and switch channels (Channel 1, 2, 3)  
- **Air Conditioner**: Adjust between 3 levels using a slider  
- **CLEAR**: Reset all devices to OFF state  
- **EXIT**: Close the application

✅ Environmental Monitoring:
- Simulates **temperature** and **humidity** values, updated every 10 seconds

✅ Electricity Chart:
- Click the `OPEN` button to display a monthly electricity usage bar chart

✅ Realistic Visual Feedback:
- Device icons and visuals change based on user interaction

---

## 🧰 Technologies Used

- **Python 3.x**
- **PyQt5** – For building the GUI  
- **Matplotlib** – For displaying the electricity usage chart  
- **Qt Designer** – For GUI layout (manually coded here)  
- **Random Module** – For simulating sensor data

---

## 🗂️ File Structure

```plaintext
.
├── main.py               # Main PyQt5 application code
├── images/
│   ├── background.jpg
│   ├── Khach_TV_ON.png
│   ├── Khach_TV_OFF.png
│   ├── Khach_TV_CN1.png
│   ├── Khach_TV_CN2.png
│   ├── Khach_TV_CN3.png
│   ├── Khach_AC_1.png
│   ├── Khach_AC_2.png
│   ├── Khach_AC_OFF.png
│   ├── Khach_Lamp_ON.png
│   ├── Khach_Lamp_OFF.png
│   └── ...
└── README.md
```

> Ensure all image assets are correctly located in the `images/` folder and referenced properly in your Python code with `Qt Resource System` or file paths.

---

## 🛠️ How to Run

### 📦 Prerequisites

Install the required packages:

```bash
pip install PyQt5 matplotlib
```

### ▶️ Run the application

```bash
python main.py
```

---

## 💡 Demo Logic Highlights

- **Channel Switching Logic**: TV must be ON to switch channels  
- **Slider (Air Conditioner)**:  
  - Level 0 → OFF  
  - Level 1 → Low power  
  - Level 2 → Max cooling  

- **Chart Function**: Opens a bar chart of electricity cost over months  
- **Sensor Values**: Generated randomly between realistic bounds and refreshed every 10 seconds

---

## 👤 Author

- **Lê Trí Bình An** – 22119160  
- HCMUTE – Faculty of Electrical and Electronics Engineering

---

## 📌 Notes

This interface is part of a university-level IoT or embedded systems coursework and can be further integrated with real microcontroller inputs or MQTT for real-time smart home control.

---
