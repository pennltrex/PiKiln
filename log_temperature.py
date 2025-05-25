import os
import csv
import time
import board
import digitalio
import busio
import adafruit_max31856
import settings

# Set up SPI and chip select
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(getattr(board, settings.DIGITAL_INOUT_PIN))  # Replace with your actual CS pin
thermocouple = adafruit_max31856.MAX31856(spi, cs)

# Check if the file exists and is empty
file_exists = os.path.isfile(settings.CSV_FILE_NAME)
write_header = not file_exists or os.path.getsize(settings.CSV_FILE_NAME) == 0

try:
    while True:
        # Read temperature
        temperature = thermocouple.temperature
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Log data to CSV
        with open(settings.CSV_FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(["Timestamp", "Temperature (°C)"])
                write_header = False
            writer.writerow([timestamp, temperature])
        print(f"{timestamp} - Temperature: {temperature:.2f} °C")
        
        # Wait for specified seconds
        time.sleep(settings.LOG_INTERVAL_SECONDS)
except KeyboardInterrupt:
    print("Logging stopped.")