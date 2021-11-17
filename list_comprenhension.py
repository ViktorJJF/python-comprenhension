def run():
    # for i in range(1,101):
    #     number_square=i**2
    #     if number_square%3!=0:
    #         print(f"El cuadrado de {i} es {i**2}")
    squares=[i for i in range(1,10000) if i%36==0]
    print(squares)

if __name__=='__main__':
    run()