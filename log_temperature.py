#!/usr/bin/env/ python3

import time
import csv
import board
import digitalio
import busio
import adafruit_max31856

# Set up SPI and chip select
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Replace with your actual CS pin
thermocouple = adafruit_max31856.MAX31856(spi, cs)

# Open CSV file for logging
with open('temperature_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature (°C)"])  # Write header

    try:
        while True:
            # Read temperature
            temperature = thermocouple.temperature
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Log data to CSV
            writer.writerow([timestamp, temperature])
            print(f"{timestamp} - Temperature: {temperature:.2f} °C")
            
            # Wait for 10 seconds
            time.sleep(10)
    except KeyboardInterrupt:
        print("Logging stopped.")
