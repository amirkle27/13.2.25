from adapter_list_to_int import AdapterListToInt

def print_factorial_number(factorial, *numbers):
    for result in factorial.calc_factorial(*numbers):
        print(result)

if __name__ == "__main__":

    print_factorial_number(AdapterListToInt(),7, 9, 10,3.2,*[5,2,40.5])

