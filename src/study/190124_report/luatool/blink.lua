led = 0
gpio.mode(led, gpio.OUTPUT)
while 1 do
	gpio.write(led, gpio.HIGH)
	tmr.delay(1000000)
	gpio.write(led, gpio.LOW)
	tmr.delay(1000000)
end
