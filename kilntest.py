import board
import digitalio
import busio
import adafruit_max31856

# Set up SPI and chip select
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Use the correct GPIO pin for CS
thermocouple = adafruit_max31856.MAX31856(spi, cs)

# Read temperature
print("Temperature: {:.2f} °C".format(thermocouple.temperature))
