import os
import csv
import time
import board
import digitalio
import busio
import adafruit_max31856

# Set up SPI and chip select
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Replace with your actual CS pin
thermocouple = adafruit_max31856.MAX31856(spi, cs)

# Check if the file exists and is empty
file_exists = os.path.isfile('temperature_log.csv')
write_header = not file_exists or os.path.getsize('temperature_log.csv') == 0

# Open CSV file for appending
with open('temperature_log.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    if write_header:
        writer.writerow(["Timestamp", "Temperature (°C)"])  # Write header if file is new or empty

    try:
        while True:
            # Read temperature
            temperature = thermocouple.temperature
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Log data to CSV
            with open('temperature_log.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                if write_header:
                    writer.writerow(["Timestamp", "Temperature (°C)"])
                    write_header = False
                writer.writerow([timestamp, temperature])
            print(f"{timestamp} - Temperature: {temperature:.2f} °C")
            
            # Wait for 10 seconds
            time.sleep(10)
    except KeyboardInterrupt:
        print("Logging stopped.")
