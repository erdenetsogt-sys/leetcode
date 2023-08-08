class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_space = big
        self.medium_space = medium
        self.small_space = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_space == 0:
                return False
            else:
                self.big_space -= 1
                return True
        elif carType == 2:
            if self.medium_space == 0:
                return False
            else:
                self.medium_space -= 1
                return True
        else:
            if self.small_space == 0:
                return False
            else:
                self.small_space -= 1
                return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)