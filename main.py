from car import Car


def main():
    car_one = Car("Mercedes", "GLS", 2023, "black")
    print(car_one.color)
    car_one.drive()


if __name__ == '__main__':
    main()
