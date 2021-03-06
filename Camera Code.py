# Find Rects Example
#
# This example shows off how to find rectangles in the image using the quad threshold
# detection code from our April Tags code. The quad threshold detection algorithm
# detects rectangles in an extremely robust way and is much better than Hough
# Transform based methods. For example, it can still detect rectangles even when lens
# distortion causes those rectangles to look bent. Rounded rectangles are no problem!
# (But, given this the code will also detect small radius circles too)...
import sensor, image, time, pyb, utime

SQUARES = 4
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE) # grayscale is faster (160x120 max on OpenMV-M7)
sensor.set_framesize(sensor.VGA)
sensor.set_auto_whitebal(False)
sensor.set_auto_exposure(False,300)
sensor.skip_frames(time = 2000)
clock = time.clock()
Threshold = (45, 255)
indicator_servo = pyb.Servo(2)
'''indicator_red = pyb.Pin('P9', pyb.Pin.OUT_PP)
while(True):
    utime.sleep_ms(2000)
    indicator_servo.angle(90)
    indicator_red.value(0)
    utime.sleep_ms(2000)
    indicator_servo.angle(0)
    indicator_red.value(1)'''  #debug stuff
while(True):
    clock.tick()
    img = sensor.snapshot()
    # `threshold` below should be set to a high enough value to filter out noise
    # rectangles detected in the image which have low edge magnitudes. Rectangles
    # have larger edge magnitudes the larger and more contrasty they are...

    blobs = img.find_blobs([Threshold])
    list_o_blobs = 0
    for blob in blobs:
        print(blob.pixels())
        if blob.pixels() <= 150 and blob.pixels() >= 85:

            list_o_blobs += 1

    if list_o_blobs == SQUARES:
         print("empty")
         indicator_servo.angle(180)
    else:
        print("not empty")
        indicator_servo.angle(0)
    print(list_o_blobs)

    print("FPS %f" % clock.fps())
