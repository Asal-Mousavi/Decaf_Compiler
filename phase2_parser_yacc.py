from itertools import count

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
    """field_decl : type field_decl_1 SEMI
                    | field_decl field_decl
                    | field_decl NEWLINE
                    | empty
                    """
    pass

def p_field_decl_1(p):
    """field_decl_1 : IDENTIFIER
                    | IDENTIFIER O_BRACKET int_literal C_BRACKET
                    | field_decl_1 COMMA field_decl_1

    """

def p_method_decl(p):
    """
        method_decl : type_or_void IDENTIFIER O_PAR type_and_id C_PAR block
                    | method_decl NEWLINE
                    | method_decl method_decl
                    | empty
    """
    pass

def p_type_and_id (p):
    """
    type_and_id : type IDENTIFIER
                | type_and_id COMMA type_and_id
    """
    pass

def p_type_or_void (p):
    """
        type_or_void : type
                    | VOID
    """
    pass

def p_block(p):
    """
    block : OPEN var_decl statement CLOSE
    | OPEN CLOSE
    """
    pass

def p_var_decl(p):
    """var_decl : type var_decl_1 SEMI
                | var_decl var_decl NEWLINE
                | empty
                """
    pass

def p_var_decl_1(p):
    """var_decl_1 : IDENTIFIER
                | var_decl_1 COMMA var_decl_1"""
    pass

def p_type(p):
    """type : INT
                | BOOLEAN"""
    pass

def p_statement(p):
    """statement : location ASSIGN expr SEMI
           | method_call SEMI
           | IF O_PAR expr C_PAR block NEWLINE else_or_empty
           | WHILE O_PAR expr C_PAR block
           | RETURN expr_or_empty SEMI
           | BREAK SEMI
           | CONTINUE SEMI
           | block
           | statement statement
           | statement NEWLINE
           | empty

    """
    pass

def p_expr_or_empty(p):
    """
    expr_or_empty : expr
                    | empty
    """

def p_else_or_empty(p):
    """else_or_empty : ELSE block
                    | else_or_empty else_or_empty
                    | empty
    """
    pass

def p_method_call(p):
    """method_call : method_name  O_PAR expr C_PAR
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
           | expr expr
           | expr NEWLINE
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
    line_number = 0
    if p == None :
        tok = 'end of file !'
    else :
        file = open("decaf.txt", "r")
        for line_number, line in enumerate(file, start=1):
            pass
        tok = f"{p.type}({p.value})on line {(p.lineno - line_number + 1)}"
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
