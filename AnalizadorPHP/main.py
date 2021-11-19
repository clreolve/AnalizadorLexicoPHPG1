#importacion tokens
import tokens
lexer = tokens.lexer

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

test_tokens()