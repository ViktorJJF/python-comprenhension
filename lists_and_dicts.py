def run():
    my_list=[1,"Helo",True,4.5]
    my_dict={"first_name":"Victor","last_name":"Jimenez"}
    
    super_list=[
        {"first_name":"Victor","last_name":"Jimenez"},
        {"first_name":"Juan","last_name":"Jimenez"},
        {"first_name":"Oscar","last_name":"Jimenez"}
    ]
    super_dict={
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.43]
    }
    
    for key,value in super_dict.items():
        print(f"La llave {key} tiene {value}")
     

if __name__=='__main__':
    run()