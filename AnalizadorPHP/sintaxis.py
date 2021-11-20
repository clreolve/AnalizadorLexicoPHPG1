import ply.yacc as yacc
from lexico import tokens, lexer

def p_expresiones(p):
    '''
    expresiones : elemento_numerico
                | var_asignar
                | var_declarar
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
    '''comparador : IDENTICAL
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

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('Python > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)