#importacion tokens
from lexico import lexer
from sintaxis import parser
# TEST tokens
def test_tokens():
    data = '''
    $set->remove(1);
      <?php
            if ($i == 0) {
                echo "$i es igual a 0";
            } elseif ($i == 1) {
                echo "i es igual a 1";
            } elseif ($i == 2) {
                echo "i es igual a 2";
            }

            switch ($i) {
                case 0:
                    echo "i es igual a 0";
                    break;
                case 1:
                    echo "i es igual a 1";
                    break;
                case 2:
                    echo "i es igual a 2";
                    break;
            }
        ?>
     '''
    #

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

def test_lexico_file():
    print("Prueba sintaxis text.py:")
    texto = ""
    with open("test.txt", "r") as archivo:
        for linea in archivo:
            if(linea == " " or linea == "\n"):
                texto = texto
            else:
                texto = texto + linea
        archivo.close()
    try:
        s = texto
        result = parser.parse(s)
        print(result)
    except EOFError:
        print('error')

    print("Prueba finalizada\n")


def test_lexico_cli():
    print("Pruebas por CLI:")
    while True:
        try:
            s = input('Python > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)

test_tokens()