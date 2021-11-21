import ply.yacc as yacc
from lexico import tokens, lexer

def p_expresiones(p):
    '''
    expresiones : expresion
                | expresion expresiones
    '''

def p_expresion(p):
    '''
    expresion : var_asignar
                | var_declarar
                | expresiones_de_salida
                | estructuras_de_control
                | var_plusminus
                | datos_estructurados

    '''

#Start - Vivanco
# var $variable = ...
def p_var_declarar(p):
    '''
    var_declarar : VAR var_asignar
    '''

def p_var_plusminus(p):
    '''
    var_plusminus : VARIABLE PLUS PLUS SEMICOLON
                | VARIABLE MINUS MINUS SEMICOLON
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
    elemento_logico : elemento_logico_pri
                    | elemento_logico_pri comparador elemento_logico_pri
                    | NOTLOGICAL elemento_logico_pri
                    | LPAREN elemento_logico_pri RPAREN
                    | VARIABLE
                    | elemento_numerico comparador elemento_numerico
                    | elemento_string comparador elemento_string
    '''

###########
def p_elemento_logico_pri(p):
    '''
    elemento_logico_pri : TRUE
                        | FALSE
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

# End - Vivanco
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

def p_params_points(p):
    '''
    params_points : param
                | param POINT params_points
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
            | ECHO params_points SEMICOLON
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
def p_estructuras_de_control(p):
    '''
    estructuras_de_control : if_structures
                            | estructuras_while
    '''

def p_if_structures(p):
    '''
    if_structures : if
            | if else
            | if else_if else
            | if else_if
            | if_r ENDIF SEMICOLON
            | if_r else_r ENDIF SEMICOLON
            | if_r elseif_r else_r ENDIF SEMICOLON
            | if_r elseif_r ENDIF SEMICOLON

    '''

def p_if(p):
    '''
    if : IF LPAREN elemento_logico RPAREN LCURLY expresiones RCURLY
    '''

def p_else(p):
    '''
    else : ELSE LCURLY expresiones RCURLY
    '''

def p_else_if(p):
    '''
    else_if : ELSEIF LPAREN elemento_logico RPAREN LCURLY expresiones RCURLY
            | ELSE IF LPAREN elemento_logico RPAREN LCURLY expresiones RCURLY
            | else_if else_if
    '''

def p_if_r(p):
    '''
    if_r : IF LPAREN elemento_logico RPAREN DOUBLEPOINT expresiones
    '''

def p_else_r(p):
    '''
    else_r : ELSE DOUBLEPOINT expresiones
    '''

def p_elseif_r(p):
    '''
    elseif_r : ELSEIF LPAREN elemento_logico RPAREN DOUBLEPOINT expresiones
                | elseif_r elseif_r
    '''

def p_estructuras_while(p):
    '''
    estructuras_while : while

    '''

def p_while(p):
    '''
    while : WHILE LPAREN elemento_logico RPAREN LCURLY expresiones RCURLY
            | WHILE LPAREN elemento_logico RPAREN DOUBLEPOINT expresiones ENDWHILE SEMICOLON
    '''

# End - Claudio Olvera

# Start - Vivanco
# End - Vivanco

# Start - Jaramillo
def p_datos_estructurados(p):
    '''
    datos_estructurados : map
                            | vector
                            | set
    '''
# $mapa = new \Ds\Map (["a"=>1,"b"=>2]);    $mapa = new \Ds\Map (["a"=>"c","b"=>"d"]);
# $mapa = new \Ds\Map (["a"=>true,2=>"d"]);
def p_map(p):
    '''
    map : VARIABLE EQUALS NEW MAP LPAREN LBRACKET todos_clave_valor RBRACKET RPAREN SEMICOLON
    '''

def p_clave_valor(p):
    '''
    clave_valor : elemento_string ARROW elemento_string
                    | elemento_string ARROW NUMBER
                    | NUMBER ARROW elemento_string
                    | NUMBER ARROW NUMBER
                    | NUMBER ARROW elemento_logico_pri
                    | elemento_string ARROW elemento_logico_pri
    '''

def p_todos_clave_valor(p):
    '''
    todos_clave_valor : clave_valor
                            | clave_valor COMMA todos_clave_valor
    '''

# $vector = new \Ds\Vector (["a",1,"b",true]);
def p_vector(p):
    '''
    vector : VARIABLE EQUALS NEW VECTOR LPAREN LBRACKET llenar RBRACKET RPAREN SEMICOLON
    '''

def p_datos(p):
    '''
    datos : FLOAT
                | NUMBER
                | STRING
                | STRINGCC
                | elemento_logico_pri
    '''

def p_llenar(p):
    '''
    llenar : datos
                | datos COMMA llenar
    '''

def p_set(p):
    '''
    set : VARIABLE EQUALS NEW SET LPAREN LBRACKET llenar RBRACKET RPAREN SEMICOLON
    '''
# End - JaramilloR



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
# Build the parser
parser = yacc.yacc()