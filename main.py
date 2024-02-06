import reken
from car import Car
from reken import Reken


def main():
    car_one = Car("Mercedes", "GLS", 2023, "black")
    print(car_one.color)
    car_one.drive()
    waardes = Reken(2, 8)
    print(waardes.substract(reverse=True))


if __name__ == '__main__':
    main()

