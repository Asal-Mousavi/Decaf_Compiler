import ply.yacc as yacc
from phase1_lexer_plyLib import tokens
INPUT_FILE = 'decaf.txt'
OUTPUT_FILE = 'parser_out'
print("----------------------------------")

def p_program(p):
    """
    program : CLASS PROGRAM OPEN field_decl method_decl CLOSE
    """
    pass

def p_field_decl(p):
    """field_decl : type OPEN IDENTIFIER
                    | IDENTIFIER O_BRACKET OPEN int_literal C_BRACKET CLOSE  COMMA SEMI
                    | field_decl
                    | empty
                    """
    pass

def p_method_decl(p):
    """
        method_decl : OPEN type
                  | VOID CLOSE IDENTIFIER O_PAR O_BRACKET OPEN type IDENTIFIER CLOSE COMMA C_BRACKET C_PAR block
                  | method_decl
                  | empty
    """
    pass

def p_block(p):
    """
    block : OPEN var_decl statement CLOSE
    """
    pass

def p_var_decl(p):
    """var_decl : type IDENTIFIER COMMA SEMI
                | var_decl"""
    pass

def p_type(p):
    """type : INT
                | BOOLEAN"""
    pass

def p_statement(p):
    """statement : location ASSIGN expr SEMI
           | method_call SEMI
           | IF O_PAR expr C_PAR block O_BRACKET ELSE block C_BRACKET
           | WHILE O_PAR expr C_PAR block
           | RETURN O_BRACKET expr C_BRACKET SEMI
           | BREAK SEMI
           | CONTINUE SEMI
           | block
           | statement
    """
    pass

def p_method_call(p):
    """method_call : method_name O_PAR O_BRACKET expr COMMA C_BRACKET C_PAR
           | CALLOUT O_PAR string_literal O_BRACKET COMMA callout_arg COMMA C_BRACKET C_PAR"""
    pass

def p_method_name(p):
    """method_name : IDENTIFIER"""
    pass

def p_location(p):
    """ location : IDENTIFIER
           | IDENTIFIER O_BRACKET expr C_BRACKET"""
    pass

def p_expr(p):
    """
    expr : location
           | method_call
           | literal
           | expr bin_op expr
           | NEGATIVE expr
           | EXCL expr
           | O_PAR expr C_PAR
           | expr
    """
    pass

def p_callout_arg(p):
    """
    callout_arg : expr
                    | string_literal
                    | callout_arg
    """
    pass

def p_bin_op(p):
    """
     bin_op : ARITH_OP
           | REP_OP
           | EQ_OP
           | COND_OP
    """
    pass


def p_literal(p):
    """
    literal : int_literal
           | char_literal
           | bool_literal
    """
    pass

def p_int_literal(p):
    """
    int_literal : DECIMAL
                    | HEXDECIMAL
    """
    pass


def p_bool_literal(p):
    """
    bool_literal : TRUE
                    | FALSE
    """
    pass


def p_char_literal(p):
    """
    char_literal : CHAR
    """
    pass


def p_string_literal(p):
    """
    string_literal : STRING
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
