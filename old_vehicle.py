# Sprint 1 OO Unit Test Spike:
# Vehicle class iteration 1
#      > offers insights into potential attributes and behavior... supporting OO Analysis & Design
#      > experiment with white box testing
#
# At WeGo, SWE's focus on strategic, maintainable software over tactical programming
# A fundamental strategic code construct is block box testing (aka unit test)
#      > Unit test coverage is a scrum team KPI
#      > Unit tests will be packaged and run on-demand as SWEs iterate and increment code
#      > Unit test suites enable automated software build and deployment to our cloud environment
#
# Tutorial https://www.jetbrains.com/help/pycharm/basic-tutorials.html

class Vehicle:
    def __init__(self, plate_num, speed=0):
        self.plate_num = plate_num
        self.speed = speed
        self.odometer = 0
        self.tripTime = 0

    def reportState(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    # Our autonomous vehicle will ultimately navigate a route
    # This iteratioin simply steps the odometer and time
    def stepRoute(self):
        self.odometer += self.speed
        self.tripTime += 1

    def avgSpeed(self):
        if self.tripTime != 0:
            return self.odometer / self.tripTime


def main():
    myVehicle = Vehicle()
    print("*" * 8, "I'm an autonomous vehicle!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, show average [S]peed? or [Q]uit\t ---> ").upper()
        if action not in "ABOSQ" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            myVehicle.accelerate()
        elif action == 'B':
            myVehicle.brake()
        elif action == 'O':
            print("The vehicle has driven {} kilometers".format(myVehicle.odometer))
        elif action == 'S':
            print("The vehicle's average speed was {} kph".format(myVehicle.avgSpeed()))
        elif action == 'Q':
            break
        myVehicle.stepRoute()
        myVehicle.reportState()
    print('\n****** bye-bye'.upper())