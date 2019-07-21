from gpiozero import Button

wind_speed_sensor = Button(5)
wind_count = 0
test = 1

def spin():
    global wind_count
    wind_count = wind_count + 1
    print("spin" + str(wind_count))

wind_speed_sensor.when_pressed = spin

while(True):
    test = test+1
