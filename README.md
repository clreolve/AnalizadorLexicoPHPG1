# AnalizadorLexicoPHPG1

## Integrantes

- Jose Vivanco
- Jose Jaramillo
- Claudio Olvera

# Uso de la herramienta de prueba

- Durante la ejecución se generara una consola que permitira las validaciones directas de sentencias php

- Por facilidad de uso la consola solo admitira sentencias directas de php sin usar la estructura ```php <!php ... ?>```

- Se dispone de un archivo text.txt y un metodo de prueba opcional **permite probar las sentencias que escritas en el mismo**; cuyo resultado se mostrara al inicio de la consola

# El analizador sintáctico permite validar:

- Declaraciones y asignaciones de variables
- Operaciones matemáticas y booleanas
- Funciones con o sin parametros 
- Estructuras de control anidadas 
- Declaracion de funciones, su cuerpo y return
- Datos estructurados (map, vector y set) con diferentes funciones ((key,diff), (find, push), (union, remove)) respectivamente.

## salida/entrada de datos
- echo
- print
- print_r
- vardump
- var_export

## Estructuras de control anidadas
Aunque con problemas debido a la limitaciones de PLY actualmente validamos:

bucles while

if - elseif -else

if - else if -else

```php
    if ($a > $b) { 
        echo "a es mayor que b";
    } elseif ($a == $b) { 
        echo "a es igual que b";
    } else { 
        echo "a es menor que b"; }
```

la forma compacta:
```php
    if ($a > $b):
      echo $a." es mayor que ".$b;
    elseif ($a == $b):
      // Tenga en cuenta la combinación de las palabras.
      echo $a." igual ".$b;
    else:
      echo $a." no es ni mayor ni igual a ".$b;
    endif;
```
