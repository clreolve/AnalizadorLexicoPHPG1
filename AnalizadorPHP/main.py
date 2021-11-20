#importacion tokens
from lexico import lexer
from sintaxis import parser

# TEST tokens
def test_tokens():
    data = '''
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

def test_texto():
    data = '''
            $var = readline();
            $var = readline(“Ingresa :”);
            $var = readline(‘Ingresa :’);
            $var = readline($mensaje_str);
        '''
    try:
        s = input(data)
    except EOFError:
        print('error')
    result = parser.parse(s)
    print(result)

def test_lexico_cli():
    while True:
        try:
            s = input('Python > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)

#test_texto()

test_lexico_cli()