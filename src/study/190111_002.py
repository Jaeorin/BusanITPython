import RPi.GPIO as GPIO

import time
            
LED = 19
            
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
            
try:
    while (True):
        GPIO.output(LED, True)
        time.sleep(0.5)
        GPIO.output(LED, False)        
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nGood Bye")
    GPIO.cleanup()
