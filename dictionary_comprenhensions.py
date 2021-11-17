from math import sqrt
def run():
    numbers={i: sqrt(i) for i in range(1,1001)}
    # for i in range(1,101):
    #     if i%3!=0:
    #         numbers[i]=i**3
    print(numbers)

if __name__=='__main__':
    run()