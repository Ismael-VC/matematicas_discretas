#!/usr/bin/env python3


from textwrap import dedent as dd

import decimal


'''Permite manipular numeros con precision decimal en distintos sistemas (2, 8, 10 y 16) numericos.'''


__author__ = 'Ismael Venegas Castelló    < ismael.vc1337@gmail.com >'


class Numero():
    base = 10
    # Digitos permitidos en base 10:
    permitidos = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
                  '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    
    def __init__(self, entero=None ,dec=None,
                 base=base, permitidos=permitidos):
        self.base = base
        self.permitidos = permitidos
        
        if entero is None:
            self.entero = ['0']
        else:
            self.entero = list(entero)
        
        if dec is None:
            self.dec = ['0']
        else: 
            self.dec = list(dec)

        for n in self.entero + self.dec:
            if n not in self.permitidos.keys():
                raise ValueError('Digito "{0}" no permitido '
                                 'en base {1}.'.format(n, self.base))


    def __str__(self):
        return '{0}.{1} ({2})'.format(''.join(n for n in self.entero),
                                      ''.join(n for n in self.dec),
                                      self.base)
                                 

    def a_float(self):
        posiciones_entero = list(reversed(range(len(self.entero))))
        posiciones_dec = [-n for n in range(1, len(self.dec) +1)]
        numero = [int(n) for n in self.entero + self.dec]
        posicion = posiciones_entero + posiciones_dec
        resultado = sum(x*self.base**y for (x, y) in zip(numero, posicion))
        return resultado
        
        
    def a_base(self, base=10, precision=5):
        permitidos = [2, 8, 10, 16]
        hexa = {10: 'A', 11: 'B', 12: 'C',
                13: 'D', 14: 'E', 15: 'F'}
        if base not in permitidos:
            raise ValueError('Tipo de base "{0}" no '
                             'implementada.'.format(base))
        
        cociente = int(decimal.Decimal(str(self.a_float())))
        fraccion = decimal.Decimal(str(self.a_float())) - cociente

        restos = []
        productos = []
        
        while cociente:
            cociente, resto = divmod(cociente, base)
            if resto in hexa and base == 16:
                resto = hexa[resto]
            restos.append(str(resto))
            dec = cociente
        restos.reverse()

        while fraccion:
            producto = int(fraccion * base)
            fraccion = (fraccion * base) - producto
            if producto in hexa and base == 16:
                producto = hexa[producto] 
            productos.append(str(producto))
            if len(productos) == precision:
                break
            
        if not productos:
            productos = ['0']

        return '{0}.{1} ({2})'.format(''.join(restos), ''.join(productos),
                                      base)
                       
                                      
def main(entero='1337', dec='007'):
    n = Numero(entero, dec)
    nd = n.a_float()
    n2 = n.a_base(2)
    n8 = n.a_base(8)
    n10 = n.a_base(10)
    n16 = n.a_base(16)

    print(dd('''
                Numero:\t\t{0}
                Float:\t\t{1}
                Binario:\t{2}
                Octal:\t\t{3}
                Decimal:\t{4}
                Hexadecimal:\t{5}'''.format(n, nd, n2, n8, n10, n16)))
    

if __name__ == '__main__':
    main()
