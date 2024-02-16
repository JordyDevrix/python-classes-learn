import reken
from car import Car
from reken import Reken
from replacer import String


def printer():
    print("hello world")


def main():
    waarde = String("lorum ipsum is een prachtig verhaal en ik ga dat vandaag lezen")
    print(waarde.herzet('e', 'a').herzet('i', 'a'))


if __name__ == '__main__':
    main()

