import ply.lex as lex

tokens = (
    'NEWLINE',
    'KEYWORD',
    'ASSIGN',
    'ARITH_OP',
    'REP_OP',
    'EQ_OP',
    'COND_OP',
    'IDENTIFIER',
    'DECIMAL',
    'HEXDECIMAL',
    'CHAR',
    'STRING',
    'COMMENT',
    'TAB'

)

t_NEWLINE = r"(\n)"
t_KEYWORD = r"\b((if)|(else)|(while)|(int)|(char)|(boolean)|(return)|(break)|(continue)|" \
            r"(callout)|(void)|(class)|(true)|(false))\b"
t_ASSIGN = r"(=)"
t_ARITH_OP = r"(\+ | - | \* | \/ | % | << | >> | >>>)(?![\/\/])"
t_REP_OP = r"(>|<)(=|)"
t_EQ_OP = r"== | !="
t_COND_OP = r"&& | \|\|"
t_IDENTIFIER = r"(\.|\b([a-zA-Z_]))([a-zA-Z_]|\d)*(?!['\"])\b"
t_DECIMAL = r"\b[0-9]+\b"
t_HEXDECIMAL = r"\b0x[0-9a-fA-F]+\b"
t_CHAR = r"\'.\'"
t_STRING = r"\".*?\""
t_COMMENT = r"\/\/.*"
t_TAB = r"(\t)"


def t_error(t):
    if t.value[0] != " ":
        print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

file = open("decaf.txt")
text = file.read()
lexer.input(text)


while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
