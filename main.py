import reken
from car import Car
from reken import Reken


def main():
    car_one = Car("Mercedes", "GLS")
    car_two = Car("Mercedes", "GLC")
    print(car_two.get_car_data())
    car_two.add_values(2023, "White")
    print(car_two.get_car_data())

    #######################

    waardes = Reken(2, 8)
    print(waardes.multiply())


if __name__ == '__main__':
    main()

