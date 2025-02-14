from factorial_calc import FactorialCalculator


class AdapterListToInt:

    def calc_factorial(self,*numbers:list):
        return (FactorialCalculator().calc_factorial(int(num)) for num in numbers)



