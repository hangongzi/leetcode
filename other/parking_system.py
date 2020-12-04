class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        if self.parking[carType]>0:
            self.parking[carType] -= 1
            return True

        for i in range(1, carType)[::-1]:
            if self.parking[i]>0:
                self.parking[i] -= 1
                return True
        return False

obj = ParkingSystem(0, 1, 2)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
