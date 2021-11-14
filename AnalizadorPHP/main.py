import ply.lex as lex
from ply.lex import TOKEN

reseverd = {
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

