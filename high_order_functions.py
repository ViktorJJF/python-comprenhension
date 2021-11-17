from functools import reduce
def reduce_function():
    my_list=[2,2,2,2,2]
    print(reduce(lambda acc,x:acc*x,my_list))
def map_function():
    my_list=[1,2,3,4,5]
    my_second_list=list(map(lambda x:x**2,my_list))
    print(my_second_list)

def run():
    # map_function()
    reduce_function()
if __name__=='__main__':
    run()