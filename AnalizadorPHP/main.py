import ply.lex as lex
from ply.lex import TOKEN

reserved = {
    #inicia - Vivanco
    'and' : 'AND',
    'as' : 'AS',
    'case' : 'CASE',
    'class' : 'CLASS',
    'do' : 'DO',
    'echo' : 'ECHO',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'endfor' : 'ENDFOR',
    'endforeach' : 'ENDFOREACH',
    'endif' : 'ENDIF',
    'endswitch' : 'ENDSWITCH',
    'endwhile' : 'ENDWHILE',
    'for' : 'FOR',
    'foreach' : 'FOREACH',
    'function' : 'FUNCTION',
    'global' : 'GLOBAL',
    'if' : 'IF',
    'implements' : 'IMPLEMENTS',
    'interface': 'INTERFACE',
    'new' : 'NEW',
    'or' : 'OR',
    'print' : 'PRINT',
    'private' : 'PRIVATE',
    'protected' : 'PROTECTED',
    'public' : 'PUBLIC',
    'return' : 'RETURN',
    'static' : 'STATIC',
    'switch' : 'SWITCH',
    'throw' : 'THROW',
    'while' : 'WHILE',
    'var' : 'VAR',
    'xor' : 'XOR',
    'catch' : 'CATCH',
    'final' : 'FINAL',
    'extends' : 'EXTENDS',
    #Termina - VIVANCO

}

#REYNALDO OLVERA
tokens = (
    'ID',
    'PHPSTART',
    'PHPEND',
    'NUMBER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EXPONENTIAL',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LCURLY',
    'RCURLY',
    'DOUBLEPOINT', #    :
    'COMMA',
    'SEMICOLON',
    'STRING',
    'STRINGCC',
    'EQUALS',
    'EQUALSLOGICAL', #  ==
    'IDENTICAL',         # ===
    'DIFFERENT',        # diferente que , no igual
    'NOTIDENTICAL',     # !==
    'GREATERTHAN', #    > Mayor que
    'LESSTHAN', # <     Menor Que
    'GREATEREQUAL', #   >=
    'LESSEQUAL', #      <=
    'ANDlOGICAL',
    'ORLOGICAL',
    'NOTLOGICAL',
    'ARROW',


) + tuple(reserved.values())
# Reynaldo end

t_PHPSTART = r'\<\?php\s$'
t_PHPEND = r'\s\?\>$'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONENTIAL = r'\*\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
T_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_DOUBLEPOINT = r':'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_FLOAT = r'\d+\.\d+'
t_NUMBER = r'\d+'
t_STRING = r'\'.*\''
t_STRINGCC = r'".*"'
t_EQUALS = r'\='
t_EQUALSLOGICAL = r'=='
t_DIFFERENT = r'!='
t_IDENTICAL = r'==='
t_NOTIDENTICAL = r'!=='
t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_GREATEREQUAL = r'\>='
t_LESSEQUAL = r'\<='
t_ANDlOGICAL = r'&&'
t_ORLOGICAL = r'\|\|'
t_NOTLOGICAL= r'!'
t_ARROW = r'=\>'

# 3ro

phpVar = r'\$[A-Za-z_]+\w?'
@TOKEN(phpVar)

# Palabras Reservadas
def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_COMMENT(t):
    r'(\#.*)|(\/\/.*)|(\/\*(.|\s)*\*\/)'
    pass

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def getTokens(lexer):
    lista=[]
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
        lista.append(tok)
    return lista
# Build the lexer
lexer = lex.lex()

def leer(linea):
    lexer.input(linea)
    lista=getTokens(lexer)
    # Tokenize
    print("Succesfull")
    return lista

# TEST

# Test it out
data = '''
  ECHO '<p>Hola Mundo</p>';
 '''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)