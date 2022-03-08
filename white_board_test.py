import unittest

from old_vehicle import Vehicle

class TestCar(unittest.TestCase):
      def setUp(self):
          self.vehicle = Vehicle()


class TestInit(TestCar):
      def test_initial_speed(self):
          self.assertEqual(self.vehicle.speed, 0)

      def test_initial_odometer(self):
          self.assertEqual(self.vehicle.odometer, 0)

      def test_initial_time(self):
          self.assertEqual(self.vehicle.tripTime, 0)


class TestAccelerate(TestCar):
      def test_accelerate_from_zero(self):
          self.vehicle.accelerate()
          self.assertEqual(self.vehicle.speed, 5)

      def test_multiple_accelerates(self):
          for _ in range(3):
            self.vehicle.accelerate()
          self.assertEqual(self.vehicle.speed, 15)


class TestBrake(TestCar):
       def test_brake_once(self):
           self.vehicle.accelerate()
           self.vehicle.brake()
           self.assertEqual(self.vehicle.speed, 0)

       def test_multiple_brakes(self):
            for _ in range(5):
                self.vehicle.accelerate()
            for _ in range(3):
                self.vehicle.brake()
            self.assertEqual(self.vehicle.speed, 10)

       def test_should_not_allow_negative_speed(self):
           self.vehicle.brake()
           self.assertEqual(self.vehicle.speed, 0)

       def test_multiple_brakes_at_zero(self):
           for _ in range(3):
               self.vehicle.brake()
           self.assertEqual(self.vehicle.speed, 0)