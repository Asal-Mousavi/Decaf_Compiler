import ply.yacc as yacc
from phase1_lexer_plyLib import tokens
INPUT_FILE = 'test.txt'
OUTPUT_FILE = 'parser_out'
print("----------------------------------")

def p_program(p):
    """
    program : decl_list
    """
    pass

def p_decl_list(p):
    """
    decl_list : decl_list decl
              | decl
    """
    pass

def p_decl(p):
    """
    decl : var_decl
         | fun_decl
    """
    pass

def p_var_decl(p):
    """
    var_decl : type_spec ID SEMICOLON
             | type_spec ID RBRACKET LBRACKET SEMICOLON
             | empty
    """
    pass
def p_type_spec(p):
    """
    type_spec : VOID
              | BOOL
              | INT
              | FLOAT
              | DOUBLE
              | CHAR
              | LONG
              | STATIC
              | SIGNED
              | UNSIGNED
    """

    pass

def p_fun_decl(p):
    """
    fun_decl : type_spec ID RPRAN params LPRAN compound_stmt
    """
    pass

def p_params(p):
    """
    params : param_list
           | VOID
           | INT
           | FLOAT
           | CHAR
           | LONG
           | UNSIGNED
           | SIGNED
           | BOOL
           | DOUBLE
           | empty
    """
    pass


def p_param_list(p):
    """
    param_list : param_list COMMA param
               | param
    """
    pass

def p_param(p):
    """
    param : type_spec ID
          | type_spec ID RBRACKET LBRACKET
    """
    pass

def p_compound_stmt(p):
    """
    compound_stmt : RCBRACE local_decls stmt_list LCBRACE
    """
    pass

def p_local_decls(p):
    """
    local_decls : local_decls local_decl
                | empty
    """
    pass

def p_local_decl(p):
    """
    local_decl : type_spec ID SEMICOLON
               | type_spec ID RBRACKET LBRACKET SEMICOLON
    """
    pass

def p_stmt_list(p):
    """
    stmt_list : stmt_list stmt
              | empty
    """
    pass
def p_continue_stmt(p):
    """
    continue_stmt : CONTINUE SEMICOLON
                 | empty
    """
    pass

def p_break_stmt(p):
    """
    break_stmt : BREAK SEMICOLON
               | empty
    """
    pass

def p_stmt(p):
    """
    stmt : expr_stmt
         | compound_stmt
         | if_stmt
         | while_stmt
         | return_stmt
         | break_stmt
         | continue_stmt
    """
    pass

def p_expr_stmt(p):
    """
    expr_stmt : expr SEMICOLON
              | SEMICOLON
    """
    pass

def p_while_stmt(p):
    """
    while_stmt : WHILE RPRAN expr LPRAN stmt
    """
    pass


def p_if_stmt(p):
    """
    if_stmt : IF RPRAN expr LPRAN stmt
            | IF RPRAN expr LPRAN stmt ELSE stmt
    """
    pass

def p_return_stmt(p):
    """
    return_stmt : RETURN SEMICOLON
                | RETURN expr SEMICOLON
    """
    pass
def p_expr(p):

    """
    expr : ID EQUAL expr
         | expr DEQUAL expr
         | expr GREATEREQUAL expr
         | expr LESSEQUAL expr
         | expr OR expr
         | expr AND expr
         | expr EQUAL expr
         | expr NOTEQUAL expr
         | expr LESSTHAN expr
         | expr GREATERTHAN expr
         | expr PLUS expr
         | expr MINUS expr
         | expr DIV expr
         | expr MUL expr
         | expr REMAINDER expr
         | MINUS expr
         | PLUS expr
         | RPRAN expr LPRAN
         | ID
         | ID RBRACKET expr LBRACKET
         | ID RPRAN args LPRAN
         | ID POINT SIZE
         | NEW type_spec RBRACKET expr LBRACKET
         | NUMBER
    """

    pass

def p_arg_list(p):
    """
    arg_list : arg_list COMMA expr
             | expr
    """
    pass

def p_args(p):
     """
     args : arg_list
          | empty
     """
     pass
def p_empty(p):
    """ empty : """
    pass


def p_error(p):
    if p == None :
        tok = 'end of file !'
    else :
        tok = f"{p.type}({p.value})on line {(p.lineno - 16 )}"
    print(f"Synyax error : Uexpexted {tok}")
# Build the parser
parser = yacc.yacc()

def read_input_file(input_file: str = INPUT_FILE) -> str:
    try:
        with open(input_file, 'r') as file:
            result = file.read()

            return result
    except FileNotFoundError as e:
        print(e)
parser.parse(read_input_file(INPUT_FILE))
print("----------------------------------")

if parser.errorok:
    print("compiled successfully")

