import lesson1.calc.calculator as c
# prova pull req
class FooCalculator:
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m, n)
    
    def div(self, m, n):
        return c.divide(m, n)

my_calc = FooCalculator()
print(my_calc.sum(3, 5))
print(my_calc.div(3, -1))
print(my_calc.div(-3, 1))
print(my_calc.div(-3, -1))
print(my_calc.div(3, 0))