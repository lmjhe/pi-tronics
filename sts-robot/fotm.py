
#import usb.core
#import usb.util
import motobrella
import time

#motobrella.light.red.on()
motobrella.move.stop()
#motobrella.light.pulse(0.5)

#motobrella.move.forward(15)
#time.sleep(2)
#motobrella.move.stop()

while True:
        motobrella.light.green.pulse(0.5)
        motobrella.move.right(15)
        time.sleep(20)
        motobrella.light.off()
        motobrella.move.stop()

        motobrella.light.red.pulse(0.5)
        motobrella.move.left(15)
        time.sleep(20)
        motobrella.light.off()
        motobrella.move.stop()

        motobrella.light.amber.pulse(0.5)
        time.sleep(8)
        motobrella.light.off()


#motobrella.move.left(90,0,90)
#motobrella.move.right(90,0,90)
#motobrella.move.forward(0)

exit(0)



left = 62
right = 5
down = 81
up = 82

dev = usb.core.find(idVendor=0x0219, idProduct=0x2433)
endpoint = dev[0][(0,0)][0]

if dev.is_kernel_driver_active(0) is True:
	dev.detach_kernel_driver(0)

usb.util.claim_interface(dev, 0)

motobrella.light.red.off()
motobrella.light.green.on()

while True:
	try:
		control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
	except:
		pass
	print control[2]

	if control[2] == down:
		motobrella.move.forward(0)
	if control[2] == up:
		motobrella.move.forward(90)
	if control[2] == left:
		motobrella.move.left(90,0,90)
	if control[2] == right:
		motobrella.move.right(90,0,90)

	if motobrella.button.is_pressed():
		exit()

	time.sleep(0.02)
