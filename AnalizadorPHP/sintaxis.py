import ply.yacc as yacc
from lexico import tokens, lexer

def p_expresiones(p):
    '''
    expresiones : expresion
                | expresion expresiones
    '''

def p_expresion(p):
    '''
    expresion : elemento_numerico
                | var_asignar
                | var_declarar
                | expresiones_de_salida

    '''

# var $variable = ...
def p_var_declarar(p):
    '''
    var_declarar : VAR var_asignar
    '''

# var variable = ...
def p_var_asignar(p):
    '''
    var_asignar : VARIABLE EQUALS VARIABLE SEMICOLON
                    | VARIABLE EQUALS elemento_numerico SEMICOLON
                    | VARIABLE EQUALS elemento_string SEMICOLON
                    | VARIABLE EQUALS elemento_logico SEMICOLON
                    | VARIABLE EQUALS funciones_ingreso_datos SEMICOLON
    '''

# 12212; (12+12/(12)); $asd + 12
def p_elemento_numerico(p):
    '''
    elemento_numerico : elemento_numerico operador elemento_numerico
                        | FLOAT
                        | NUMBER
                        | LPAREN elemento_numerico RPAREN
                        | VARIABLE
    '''

# operadores numericos
def p_operador(p):
    '''
    operador : PLUS
            | MINUS
            | DIVIDE
            | EXPONENTIAL
            | TIMES
    '''

# "lorem ipsum" ; 'lorem ipsum'
def p_elemento_string(p):
    '''elemento_string : STRING
                        | STRINGCC
                        | VARIABLE
    '''

# True False operaciones logicas
def p_elemento_logico(p):
    '''
    elemento_logico : TRUE
                    | FALSE
                    | elemento_logico comparador elemento_logico
                    | NOTLOGICAL elemento_logico
                    | LPAREN elemento_logico RPAREN
                    | VARIABLE
                    | elemento_numerico comparador elemento_numerico
                    | elemento_string comparador elemento_string
    '''

def p_comparador(p):
    '''
    comparador : IDENTICAL
               | NOTIDENTICAL
               | EQUALSLOGICAL
               | DIFFERENT
               | GREATEREQUAL
               | LESSEQUAL
               | GREATERTHAN
               | LESSTHAN
               | ANDlOGICAL
               | ORLOGICAL
    '''

# Start - Claudio Olvera

# clave precisa para poner en las llamadas de funciones
def p_param(p):
    '''
    param : VARIABLE
            | elemento_string
            | elemento_numerico
            | elemento_logico
    '''

# uno o mas parametros
def p_params(p):
    '''
    params : param
            | param COMMA params
    '''

# parametros opcionales (cero o mas parametros)
def p_optional_params(p):
    '''
    optional_params : param
                        | ""
                        | param COMMA optional_params
    '''


#echo $param,.., $paramN;
def p_expresiones_de_salida(p):
    '''
    expresiones_de_salida : echo
                            | print
                            | var_dump
                            | print_r
                            | var_export
    '''


def p_echo(p):
    '''
    echo : ECHO params SEMICOLON
    '''

def p_print(p):
    '''
    print : PRINT param SEMICOLON
    '''

def p_print_r(p):
    '''
    print_r : PRINT_R LPAREN param RPAREN SEMICOLON
    '''

def p_var_dump(p):
    '''
    var_dump : VAR_DUMP LPAREN param RPAREN SEMICOLON
    '''

def p_var_export(p):
    '''
    var_export : VAR_EXPORT LPAREN param RPAREN SEMICOLON
    '''

def p_funciones_ingreso_datos(p):
    '''
    funciones_ingreso_datos : VAR_EXPORT LPAREN param COMMA elemento_logico RPAREN
                        | READLINE LPAREN RPAREN
                        | READLINE LPAREN elemento_string RPAREN
    '''

# Estructuras de Control ###############################
def p_else_if(p):
    '''
    else_if : if
    '''

def p_if(p):
    '''
    if : IF LPAREN elemento_logico RPAREN LCURLY RCURLY
    '''

# End - Claudio Olvera

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
# Build the parser
parser = yacc.yacc()