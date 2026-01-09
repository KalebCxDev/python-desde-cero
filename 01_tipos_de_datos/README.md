# Tipos de Datos en Python
En esta sección se explican los **tipos de datos básicos en Python**, fundamentales para empezar a programar.

## Índice
- [Tipos de datos](#tipos-de-datos)
    - [Texto](#texto-str)
    - [Números](#números-int-float)
    - [Booleanos](#booleanos-bool)
- [Comprobación de tipos](#comprobación-de-tipos)
- [Ejercicios prácticos](#ejercicios-prácticos)
    - [Resueltos](#resueltos)
    - [No resueltos](#no-resueltos)
- [Conclusión](#conclusión)

## Tipos de datos
**¿Qué son los tipos de datos?**  
Los tipos de datos son clasificaciones que definen el tipo de valor que tiene una variable (texto, número, verdadero/falso, etc).  
*En otras palabras, los tipos de datos definen qué tipo de valor tendrá una variable.*

| Tipo | Descripción | Ejemplo |
|-----|-------------|---------|
| `int` | Números enteros | `10`, `-5` |
| `float` | Números decimales | `3.14`, `2.0` |
| `str` | Texto | `"Hola"` |
| `bool` | Verdadero / Falso | `True`, `False` |
| `list` | Colección ordenada y modificable | `[1, 2, 3]` |
| `tuple` | Colección ordenada e inmutable | `(1, 2)` |
| `dict` | Pares clave-valor | `{"edad": 18}` |

### Texto (str)
Los datos de tipo cadena de texto son literalmente texto.
```python
nombre = "Ana"
```
### Números (int, float)
Los datos de tipo número pueden ser dos:
- Int: Número entero
- Float: Número decimal
```python
edad = 18       # int
precio = 9.99   # float
```
### Booleanos (bool)
Los valores booleanos solo pueden ser dos:
- True: Expresión verdadera | 1
- False: Expresión falsa | 0
```python
variable_bool = True    # Verdadero
variable_bool = False  # Falso
```

### Comprobación de tipos
Podemos saber el tipo de dato que asigna Python a una variable con la función **type()**, junto a **print()** para imprimir en consola.

```python
print(type(nombre))
```
## Ejercicios prácticos
En esta sección veremos los ejercicios. En esta ocasión hay 2 ejercicios resueltos: 01_ejercicio_tdd.py y 02_ejercicio_tdd.py.
### Resueltos
#### Ejercicio 1 - **01_ejercicio_tdd.py**  
El primer ejercicio pide que creemos variables con los tipos de datos que vimos (nombre, edad, etc.).
Las variables creadas son las siguientes:
| Variable y valor | Concepto |
|-------------|------------|
| `nombre = "KalebCxDev"` | De tipo `String` o Texto |
| `edad = 22` | De tipo `Int` o numero entero |
| `estatura = 1.67` | De tipo `Float` o numerod decimal |
| `verdadero_o_falso = True` | De tipo `Booleano` |
| `sin_valor = None` | Variable sin valor o valor `None` |

#### Ejercicio 2 - **02_ejercicio_tdd.py**  
En el segundo ejercicio pide que creemos 2 variables:
- Una variable de tipo `Int`
- Otra variable de tipo `Float`

Luego pide que hagamos operaciones como: suma, resta y multiplicacion. Luego mostrar el resultado de cada operacion con un mensaje descriptivo.  
Ejm. "Resultado de [operacion]: 15"

Las variables creadas son las siguientes:
| Variable y valor | Concepto |
|-------------|--------------|
| `num_entero = 5` | De tipo `Int` o Texto |
| `num_decimal = 1.5` | De tipo `Float` |

**Explicación detallada**  
1. Creamos 2 variables: `num_entero` y `num_decimal`.
2. Asignamos un valor a cada variable: `5` y `1.5`.
3. Usando `print()` imprimimos: `"Suma:"`,  `num_entero` + `num_decimal`.
    - En esta linea sumamos los valores de las 2 variables y junto a un mensaje imprimimos su resultado. Usamos `+` para relizar una suma en python
4. Usando `print()` imprimimos: `"Resta:"`,  `num_entero` - `num_decimal`.
    - En esta linea restamos `num_decimal` a la variable `num_entero` y junto a un mensaje imprimimos su resultado. Usamos `-` para relizar una suma en python.
4. Usando `print()` imprimimos: `"Multiplicación:"`,  `num_entero` * `num_decimal`.
    - En esta linea multiplicamos los valores de las 2 variables y junto a un mensaje imprimimos su resultado. Usamos `*` para relizar una suma en python.

Mas adelante veremos mas operadores en python.  
Ejm. `*`, `/`, `%`, `//`, etc.

### No resueltos
En esta ocasión no hay ejercicios no resueltos, ya que estamos empezando con conceptos básicos.
Sin embargo, en la siguiente sección (variables) sí habrá ejercicios para que puedas practicar.
## Conclusión
Los tipos de datos son fundamentales en Python, ya que determinan cómo se almacena y manipula la información dentro de un programa.  
Comprenderlos es el primer paso para escribir código correcto, claro y eficiente.

<hr> <p align="center"> © 2026 • KalebCxDev • Python • 06-01-2026 </p>