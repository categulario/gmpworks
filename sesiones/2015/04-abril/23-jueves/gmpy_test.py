"""
Pruebas de uso de la biblioteca gmpy

Requiere la instalación de gmpy
"""
from gmpy2 import mpfr
import gmpy2
from functools import partial

out = partial(print, sep='\n', end='\n\n')

if __name__ == '__main__':
    # Reales de precisión arbitraria
    # En el siguiente ejemplo se muestra con la precisión normal
    out ('Raíz de dos: ', gmpy2.sqrt(2))

    # Obtenemos la precisión máxima teórica de la computadora
    out ('Precisión máxima: ', gmpy2.get_max_precision())

    # ¿Cuál es la precisión por defecto?
    out ('Precisión por defecto', gmpy2.get_context().precision)

    # Cambiamos la precisión de la biblioteca
    gmpy2.get_context().precision=100

    # Otra vez la raíz de dos, con precisión aumentada
    out ('Raíz de dos: ', gmpy2.sqrt(2))
    # De hecho es la precisión de cualquier número
    out ('Un flotante: ', mpfr('1.2'))

    # Ahora creamos un contexto para manejar la precisión
    with gmpy2.local_context(gmpy2.context(), precision=200) as ctx:
        out ('Precisión alterada en contexto', gmpy2.sqrt(2))
        ctx.precision += 100
        out ('Aún mejor precision', gmpy2.sqrt(2))

    # De regreso al contexto original, precision normal
    out ('Raíz de dos', gmpy2.sqrt(2))
