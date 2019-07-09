import ply.lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'printf',
)
tokens = reservada + (
    'impresion',
    'parentesisApertura',
    'string',
    'identificador',
    'parentesisCierre',
    'sFin',
    'ERROR'
)


t_sFin = ';'
t_parentesisApertura = r'\('
t_parentesisCierre = r'\)'
t_impresion = 'printf'



def t_identificador(t):
    r'\w+(_\d\w)*'
    return t

def t_string(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t


def t_error( t):
    global resultado_lexema
    estado = "** Token {:16} no valido".format( str(t.value))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Lexema {:16} Token {:16} ".format(str(tok.type) ,str(tok.value) )
        resultado_lexema.append(estado)
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)