import ply.yacc as yacc

from lexico import tokens, lexer

syntax_out = dict()

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
                | funciones_datos_estructurados
                | funcion_declaracion
                | return
                | funcion_ejecucion
                | foreach
    '''
    #syntax_out.update({lexer.lineno: {'text': f'CORRECT', 'error': False}})
    #print(syntax_out, f'{lexer.lineno}: CORRECT')

# Start - Claudio Olvera ###################################################

# clave precisa para poner en las llamadas de funciones
def p_param(p):
    '''
    param : VARIABLE
            | elemento_string
            | elemento_numerico
            | elemento_logico
            | VARIABLE LBRACKET VARIABLE RBRACKET
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

def p_params_unitype(p):
    '''
    params_unitype : only_string
                    | only_numerico
                    | only_logico
    '''

def p_only_string(p):
    '''
    only_string : elemento_string
                | elemento_string COMMA only_string
    '''

def p_only_numerico(p):
    '''
    only_numerico : elemento_numerico
                | elemento_numerico COMMA only_numerico
    '''

def p_only_logico(p):
    '''
    only_logico : elemento_logico
                | elemento_logico COMMA only_logico
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
                            | vardump
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

def p_vardump(p):
    '''
    vardump : VAR_DUMP LPAREN param RPAREN SEMICOLON
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

# Estructuras de Control
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
    estructuras_while : while_p

    '''

def p_while_p(p):
    '''
    while_p : WHILE LPAREN elemento_logico RPAREN LCURLY expresiones RCURLY
            | WHILE LPAREN elemento_logico RPAREN DOUBLEPOINT expresiones ENDWHILE SEMICOLON
    '''

def p_foreach(p):
    '''
    foreach : FOREACH LPAREN foreach_content RPAREN LCURLY expresiones RCURLY
    '''

def p_foreach_content(p):
    '''
    foreach_content : VARIABLE AS VARIABLE
                    | VARIABLE AS VARIABLE ARROW VARIABLE
    '''

# End - Claudio Olvera ###################################################

# Start - Vivanco ###################################################

# Funciones
def p_funcion_declaracion(p):
    '''
    funcion_declaracion : FUNCTION funcion_cabecera_declaracion funciones_cuerpo
                        | VARIABLE EQUALS FUNCTION LPAREN variables_por_comma RPAREN funciones_cuerpo
                        | VAR VARIABLE EQUALS FUNCTION LPAREN variables_por_comma RPAREN funciones_cuerpo
                        | FUNCTION LPAREN variables_por_comma RPAREN funciones_cuerpo
                        | FUNCTION LPAREN RPAREN funciones_cuerpo
    '''


def p_funcion_cabecera_declaracion(p):
    '''
    funcion_cabecera_declaracion : FUNCTION_NAME LPAREN variables_por_comma RPAREN
                                    | FUNCTION_NAME LPAREN RPAREN
    '''

def p_funciones_cuerpo(p):
    '''
    funciones_cuerpo : LCURLY expresiones RCURLY
                    | LCURLY RCURLY
    '''

def p_return(p):
    '''
    return : RETURN var_asignar_contenido SEMICOLON
    '''


def p_funcion_ejecucion(p):
   '''
   funcion_ejecucion : FUNCTION_NAME LPAREN params RPAREN funciones_cuerpo SEMICOLON
                    | FUNCTION_NAME LPAREN RPAREN funciones_cuerpo SEMICOLON
                    | VARIABLE LPAREN RPAREN SEMICOLON
                    | VARIABLE LPAREN params RPAREN SEMICOLON
   '''

def p_funcion_declaracion_anonima(p):
    '''
    funcion_declaracion_anonima : FUNCTION LPAREN params RPAREN funciones_cuerpo
                    | FUNCTION LPAREN RPAREN funciones_cuerpo
    '''

# una o mas variables separada por coma
def p_variables_por_comma(p):
    '''
    variables_por_comma : VARIABLE
                        | VARIABLE COMMA variables_por_comma
    '''


# End - Vivanco ###################################################

# Start - Jaramillo ###################################################
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
    map : NEW MAP LPAREN LBRACKET todos_clave_valor RBRACKET RPAREN
        | NEW MAP LPAREN RPAREN
    '''

def p_clave_valor(p):
    '''
    clave_valor : elemento_string ARROW param
                    | NUMBER ARROW param
    '''

def p_todos_clave_valor(p):
    '''
    todos_clave_valor : clave_valor
                            | clave_valor COMMA todos_clave_valor
    '''

# $vector = new \Ds\Vector (["a",1,"b",true]);
def p_vector(p):
    '''
    vector : NEW VECTOR LPAREN LBRACKET params RBRACKET RPAREN
                | NEW VECTOR LPAREN RPAREN
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
    set : NEW SET LPAREN LBRACKET params RBRACKET RPAREN
            | NEW SET LPAREN RPAREN
    '''


#FUNCIONES DE DATOS ESTRUCTURADOS
def p_funciones_datos_estructurados(p):
    '''
    funciones_datos_estructurados : funciones_map
                                        | funciones_set
                                        | funciones_vector
    '''

def p_funciones_map(p):
    '''
    funciones_map : key_map
                       | diff_map
    '''

def p_key_map(p):
    '''
    key_map : VAR_DUMP LPAREN VARIABLE SIMPLEARROW KEYS LPAREN RPAREN RPAREN SEMICOLON
    '''
    # key_map : VAR_DUMP LPAREN VARIABLE SIMPLEARROW KEYS LPAREN RPAREN RPAREN SEMICOLON

def p_diff_map(p):
    '''
    diff_map : VAR_DUMP LPAREN VARIABLE SIMPLEARROW DIFF LPAREN VARIABLE RPAREN RPAREN SEMICOLON
    '''

# End - Jaramillo ###################################################

# Start - Vivanco ###################################################
def p_funciones_vector(p):
    '''
    funciones_vector : find_vector
                        | push_vector
    '''

def p_find_vector(p):
    '''
    find_vector : VAR_DUMP LPAREN VARIABLE SIMPLEARROW FIND LPAREN param RPAREN RPAREN SEMICOLON
    '''

def p_push_vector(p):
    '''
    push_vector : VARIABLE SIMPLEARROW PUSH LPAREN param RPAREN SEMICOLON
                    | VARIABLE SIMPLEARROW PUSH LPAREN params RPAREN SEMICOLON
                    | VARIABLE SIMPLEARROW PUSH LPAREN LBRACKET params RBRACKET RPAREN SEMICOLON
    '''
# End - Vivanco ###################################################

# Start - Olvera ###################################################
def p_funciones_set(p):
    '''
    funciones_set : union_set
                    | remove_set
    '''

def p_union_set(p):
    '''
    union_set : VAR_DUMP LPAREN VARIABLE SIMPLEARROW UNION LPAREN VARIABLE RPAREN RPAREN SEMICOLON
    '''

def p_remove_set(p):
    '''
    remove_set :  VARIABLE SIMPLEARROW REMOVE LPAREN params_unitype RPAREN SEMICOLON
                    | VARIABLE SIMPLEARROW REMOVE LPAREN LBRACKET params_unitype RBRACKET RPAREN SEMICOLON
    '''
# End - Olvera ###################################################

#Start - Vivanco ###################################################
# var $variable = ...
def p_var_declarar(p):
    '''
    var_declarar : VAR var_asignar
    '''

# var variable = ...
def p_var_asignar(p):
    '''
    var_asignar : VARIABLE EQUALS var_asignar_contenido SEMICOLON
                | VARIABLE EQUALS funcion_declaracion_anonima
    '''

def p_var_asignar_contenido(p):
    '''
    var_asignar_contenido : VARIABLE
                    | elemento_numerico
                    | elemento_string
                    | elemento_logico
                    | datos_estructurados
                    | funciones_ingreso_datos
    '''

def p_var_plusminus(p):
    '''
    var_plusminus : VARIABLE PLUS PLUS SEMICOLON
                | VARIABLE MINUS MINUS SEMICOLON
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
                    | elemento_logico comparador elemento_logico
                    | NOTLOGICAL elemento_logico
                    | VARIABLE
                    | elemento_numerico comparador elemento_numerico
                    | elemento_string comparador elemento_string
    '''

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

# End - Vivanco ###################################################

# Error rule for syntax errors
def p_error(p):
    if p == None:
        token = "invalid syntax"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"
        print(f"Syntax error: Unexpected {token}")
        syntax_out.update( {p.lineno : f'Syntax error: {p.type}({p.value})'})

# Build the parser
parser = yacc.yacc()

def sintaxis_test(data):
    '''Recibe un string para validarlo y retorna un diccionario con los resultados'''
    syntax_out.clear()
    lexer.lineno = 1
    result = parser.parse(data)
    return dict(syntax_out)