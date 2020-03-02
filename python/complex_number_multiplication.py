import cmath


class Solution:
    def init_complex_number(self, num_string):
        a = num_string.split('+')
        real = int(a[0])
        imag = int(a[1][:len(a[1])-1])
        return complex(real, imag)
    
    def complexNumberMultiply(self, a: str, b: str) -> str:
        complex_a = self.init_complex_number(a)
        complex_b = self.init_complex_number(b)
        product = complex_a * complex_b
        real = str(int(product.real))
        imag = str(int(product.imag))
        return real + '+' + imag + 'i'
