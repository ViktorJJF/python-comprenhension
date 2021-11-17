def divisors(number):
    try:
        if number < 0:
            raise Exception("Debes ingresar un numero positivo")
        divisors = [i for i in range(1, number+1) if number % i == 0]
        return divisors
    except:
        print("Debes ingresar numeros positivos")


def run():
    try:
        num = int(input("Ingresa un numero: "))
        result = divisors(num)
        if result:
            print(f"Los divisores son: {result}")
    except ValueError:
        print("Debes ingresar un numero...")


if __name__ == '__main__':
    run()
