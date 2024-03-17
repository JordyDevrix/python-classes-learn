
def main():
    som = float(input())
    x = 0
    while som != 1:
        x += 1
        if som % 2 == 0:
            som = som / 2
        else:
            som = (3 * som) + 1

        with open("responses.txt", "a") as file:
            file.writelines(f"{str(som)}\n")
        print(f"{x} \t {str(som)}")


if __name__ == '__main__':
    main()
