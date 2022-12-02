import re
from pathlib import Path


def string_manipulation(old: str, special: str) -> str:
    print(old)
    new = re.sub(special, '', old)
    print(new)
    new = new.replace('|', '-')
    return new
   
        

if __name__ == '__main__':
    special_chars = '[!@#$%^&*();:,./<>?\`~=_+]'
    strings = ['01 | Análisis Chartista y Teoría Dow', 'Bloque 8 | Unidad 1 - Teoría de la Innovación: Schumpeter y Rogers.', 'Bloque 8 | Unidad 5 - Océano Rojo/Océano Azul']

    for s in strings:
        print('---> ' + string_manipulation(s, special_chars) + '\n')
