# -- TIPOS DE DATOS -- #

# - TEXTO - #
# -> Strings
string_var = "Ejemplo de texto: Texto de ejemplo"       # Con comillas dobles: En la misma linea    

string_var_two = 'Ejemplo de texto: Texto de ejemplo'   # Con comillas simples: En la misma linea

string_var_three = """
Ejemplo de texto:
Texto de ejemplo
"""                                 # Con triple comillas dobles: Sirve para varias lineas      

string_var_four = '''
Ejemplo de texto:
Texto de ejemplo
'''                                 # Con triple comillas simples: Sirve para varias lineas

# No suele haber diferencia en cuanto al uso de comillas simples o dobles, pero comunmente se usa 
# comillas triples para strings de varias lineas.
# El mas comun es: " " y """ """. Las comillas trples se usa para documentar codigo
# ------------------------------ #

# - NUMERICOS - #
# -> Int
int_var = 10        # Tipo de dato int: Numero entero
int_var_two = 15

# -> Float
float_var = 5.7     # Tipo de dato float: Numero decimal
float_var_two = 1.73

# - BOOLEANOS - #
bool_var = True         # Tipo de dato booleano: True o False: Verdadero o falso
bool_var_two = False


# - NULO - #
# -> Nulo
null_var = None     # Tipo de dato nulo: Nome: Representa la ausencia de valor o un valor faltante

# - Imprimir el tipo de dato - #
# Para saber el tipo de dato de una variable usamos type() junto a print():
# print(): Se usa para imprimir por consola
# type(): Se usa para saber el tipo de dato de una variable
# ------------------------------ #

# - String - # 
print(type(string_var))     # | <class 'str'>

# - Int - #
print(type(int_var))        # | <class 'int'>

# - Float - # 
print(type(float_var))        # | <class 'float'>

# - Boolean - # 
print(type(bool_var))        # | <class 'bool'>

# - Null - # 
print(type(null_var))        # | <class 'NoneType'>
# ------------------------------ #