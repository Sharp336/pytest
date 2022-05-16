class Culculyator():
    
    def plus(self, x, y): return x + y
    def minus(self, x, y): return x - y
    def mnoj(self, x, y): return x * y
    def delit(self, x, y): return "Нельзя делить на 0" if y == 0 else x / y
    def stepen(self, x, y): return "Нельзя возводить 0 в отрицательную степень" if x == 0 and y < 0 else x ** y
