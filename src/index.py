# Libraries
import RPi.GPIO as GPIO
import time
import statistics

import client
from detector import Detector

if __name__ == '__main__':
    try:
        detectors = [
            Detector('joker', 17, 27),
            Detector('batman', 23, 24)
        ]
        while True:
            map(lambda detector: detector.measure(), detectors)
            time.sleep(0.5)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
