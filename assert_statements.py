def divisors(number):
    assert number > -1, "Debes ingresar un numero positivo!"
    divisors = [i for i in range(1, number+1) if number % i == 0]
    return divisors


def run():
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un numero"
    result = divisors(int(num))
    if result:
        print(f"Los divisores son: {result}")


if __name__ == '__main__':
    run()
