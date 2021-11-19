import ply.yacc as yacc
from lexico import tokens, lexer

def p_expresiones(p):
    '''
    expresiones : elemento_numerico
    '''

"""
# var $variable = ...
def p_var_declarar(p):
    '''
    var_declarar : VAR var_asignar
    '''
# var variable = ...
def p_var_asignar(p):
    '''
    var_asignar : VARIABLE EQUALS VARIABLE
                    | VARIABLE EQUALS elemento_numerico SEMICOLON
    '''

"""

def p_elemento_numerico(p):
    '''
    elemento_numerico : elemento_numerico operador elemento_numerico
                        | FLOAT
                        | NUMBER
                        | LPAREN elemento_numerico RPAREN
                        | VARIABLE
    '''

def p_operador(p):
    '''
    operador : PLUS
                | MINUS
                | DIVIDE
                | EXPONENTIAL
                | TIMES
    '''

"""
def p_comparador(p):
    '''comparador : IDENTICAL
                       | NOTIDENTICAL
                       | EQUALSLOGICAL
                       | DIFFERENT
                       | EQUALS
                       | GREATEREQUAL
                       | LESSEQUAL
                       | GREATERTHAN
                       | LESSTHAN
                       | ANDlOGICAL
                       | ORLOGICAL
                       '''


def p_elemento_string(p):
    '''elemento_string : STRING
                    | STRINGCC
        '''
"""

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