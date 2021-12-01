# AnalizadorLexicoPHPG1

## Integrantes

- Jose Vivanco
- Jose Jaramillo
- Claudio Olvera

# GUI

El archivo gui.py:

- La interfaz dispone de un editor de codigo y un espacio para mostrar la salida del programa
- El boton **validar lexico** permite validar los tokens de la entrada
- El boton **validar sintactico** permite la validación de la sintaxis, dentro de los limites que permite YACC

# Prueba por CLI

El archivo **main.py**:

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

## Salida/Entrada de datos
- echo
- print
- print_r
- vardump
- var_export

## Estructuras de control anidadas
Aunque con problemas debido a la limitaciones de PLY actualmente validamos:

### Estructuras if else elseif

```php
if ($a > $b) { 
    echo "a es mayor que b";
} elseif ($a == $b) { 
    echo "a es igual que b";
} else if ($a == 2) {
    // se permite combinar "else if" y "elseif"
	echo "a es igual a 2";
} else { 
    echo "a es menor que b"; }


```

la forma compacta:
```php
if ($a > $b):
	echo $a." es mayor que ".$b;
elseif ($a == $b):
	// solo se permite "elseif"
	echo $a." igual ".$b;
else:
	echo $a." no es ni mayor ni igual a ".$b;
endif;
```

### Estructuras While

```php
$x = 1;
while ($x <= 10) {
    echo $x++;
}

// sintaxis reducida
$x = 1;
while ($x <= 10):
	echo $x++;
endwhile;

```

## Funciones

- Una función recibe cero o más parámetros
- Puedo o no retornar un objeto o dato primitivo
- Llama dentro de si expresiones que pueden ser clases o funciones (incluyendo a si misma)
- Puede crear funciones y clases que solo existen dentro de la función
- Una función definida por el usuario se puede definir de distintas formas

```php
function foo(){
	echo “yo soy foo”;
}

function foo(var){
echo “tu eres ”, $var;
}

// funciones anonimas
function(){
	echo “yo soy foo”;
}

function (var){
	echo “tu eres ”, $var;
}

// funcion almacenada en una variable
$foo = function(){
	echo “yo soy foo”;
}
$foo();		//ejecutamos foo

$hello = function (var){
	echo “tu eres ”, $var;
}
$hello(“Jhon Cena”);	//ejecutamos hello
```

