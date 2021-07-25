import time
import random


class Low_Battery(Exception):
    pass

class Zero_Battery(Exception):
    pass

class Low_Warer(Exception):
    pass

class Zero_Water(Exception):
    pass

class Full_Trech(Exception):
    pass

class Almost_Full_Trech(Exception):
    pass


class RobotCleaner:
    max_battery_charge = 100
    max_trash_box = 100
    max_water_box = 100
    cur_i = 0

    def __init__(self, cur_battery_charge, cur_trash_box, cur_water_box):
        self.cur_battery_charge = int(cur_battery_charge)
        if self.cur_battery_charge > self.max_battery_charge:
            self.cur_battery_charge = self.max_battery_charge
        elif self.cur_battery_charge < 0:
            self.cur_battery_charge = 0
        self.cur_trash_box = int(cur_trash_box)
        if self.cur_trash_box > self.max_trash_box:
            self.cur_trash_box = self.max_trash_box
        elif self.cur_trash_box < 0:
            self.cur_trash_box = 0
        self.cur_water_box = int(cur_water_box)
        if self.cur_water_box > self.max_water_box:
            self.cur_water_box = self.max_water_box
        elif self.cur_water_box < 0:
            self.cur_water_box = 0

    def move(self, i):
        print(f"Robot starts with battery lvl={self.cur_battery_charge}%, water lvl={self.cur_water_box}%, trash box fullness lvl={self.cur_trash_box}%")

        while self.cur_i < int(i):
            self.cur_i += 1
            try:
                self.cur_battery_charge -= random.randrange(3, 10, 1)
                if self.cur_battery_charge<= 15:
                    if self.cur_battery_charge <= 0:
                        raise Zero_Battery("The battery is discharged")
                    raise Low_Battery(f"Low battery: = {self.cur_battery_charge}%")
                print(f"Robot moves with battery lvl = {self.cur_battery_charge}%")
            except(Low_Battery):
                print((f"Robot moves with low battery lvl: = {self.cur_battery_charge}%"))
            except (Zero_Battery):
                print("The battery is discharged")
                break

            try:
                self.__wash()
            except(Zero_Water):
                print("No water for cleaning")
            except(Low_Warer):
                print(f"Robot washes with low water lvl = {self.cur_trash_box}%")

            try:
                self.__vacuum_cleaner()
            except(Full_Trech):
                print("The trash box is full")
            except(Almost_Full_Trech):
                print(f"The trash box can is almost full = {self.cur_trash_box}%")
                break
            time.sleep(1)
            print("\n")
        if self.cur_i == i:
            print("Cleaning finished")

    def __wash(self):
        self.cur_water_box -= random.randrange(10, 20, 1)
        if self.cur_water_box <= 10:
            if self.cur_water_box <= 0:
                raise Zero_Water("No water for cleaning")
            raise Low_Warer("There is almost no water for cleaning")
        print(f"Robot washes with water lvl = {self.cur_trash_box}%")

    def __vacuum_cleaner(self):
        self.cur_trash_box += random.randrange(7, 15, 1)
        if self.cur_trash_box >= 80:
            if self.cur_trash_box >= self.max_water_box:
                raise Full_Trech("The trash box is full")
            raise Almost_Full_Trech("The trash box can is almost full")
        print(f"Robot cleans with fullness lvl = {self.cur_trash_box}%")

if __name__ == "__main__":
    robot = RobotCleaner(100, 40, 60)
    robot.move(3)

