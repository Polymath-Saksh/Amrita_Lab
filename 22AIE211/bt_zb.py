# import serial

# def send_zigbee_message(message):
#     try:
#         zigbee_port = "/dev/ttyUSB0"  # Replace with your Zigbee serial port
#         with serial.Serial(zigbee_port, 9600) as ser:
#             ser.write(message.encode())
#             print(f"Sent Zigbee message: {message}")
#     except Exception as e:
#         print(f"Error sending Zigbee message: {e}")

# # Usage
# if __name__ == "__main__":
#     zigbee_message = "Hello from Zigbee!"
#     send_zigbee_message(zigbee_message)

from bluepy import btle

def send_ble_message(message):
    try:
        ble_device_mac = "00:11:22:33:44:55"  #
        with btle.Peripheral(ble_device_mac) as peripheral:
            service_uuid = btle.UUID("0000ffe0-0000-1000-8000-00805f9b34fb")
            char_uuid = btle.UUID("0000ffe1-0000-1000-8000-00805f9b34fb")
            char = peripheral.getCharacteristics(uuid=char_uuid)[0]
            char.write(message.encode())
            print(f"Sent BLE message: {message}")
    except Exception as e:
        print(f"Error sending BLE message: {e}")

# Usage
if __name__ == "__main__":
    ble_message = "Hi from BLE!"
    send_ble_message(ble_message)
