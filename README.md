# AnalizadorLexicoPHPG1

## Integrantes

- Jose Vivanco
- Jose Jaramillo
- Claudio Olvera

# Uso de la Herramienta

Se debe ejecutar el  archivo **gui.py** para lanzar la interfaz grafica que:

- La interfaz dispone de un editor de codigo y un espacio para mostrar la salida del programa
- Enmcuentra la posicion del primer error en un bloque de errores
- El boton **validar lexico** permite validar los tokens de la entrada
- El boton **validar sintactico** permite la validación de la sintaxis, dentro de los limites que permite YACC

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

### Foreach

Itera sobre arreglos de objetos y tipos primitivos, brindando una variable temporal que puede usarse dentro del foreach

```php
foreach($array as $e){
	echo $e;
}

```

También se puede obtener la clave/indice del arreglo

```php
foreach($array as $k => $e){
	echo $array[$k];
}
```

