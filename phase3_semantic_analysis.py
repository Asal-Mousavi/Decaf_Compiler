import ply.yacc as yacc
from phase1_lexer_plyLib import tokens

INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'parser_out'
print("----------------------------------")
symbol_table = {}


def add_to_symbol_table(name, var_type):
    if name in symbol_table:
        print(f"Semantic error : Variable '{name}' already declared.")
        parser.errorok = False
    symbol_table[name] = {"type": var_type}


def check_symbol_table(name):
    if name in symbol_table:
        return symbol_table[name]
    print(f"Semantic error : Variable '{name}' not declared.")
    parser.errorok = False


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
    if len(p) == 2:  # Single identifier
        add_to_symbol_table(p[1], p[-1])


def p_method_decl(p):
    """
        method_decl : type_or_void IDENTIFIER O_PAR type_and_id C_PAR block
                    | method_decl NEWLINE
                    | method_decl method_decl
                    | empty
    """
    pass


def p_type_and_id(p):
    """
    type_and_id : type IDENTIFIER
                | type_and_id COMMA type_and_id
    """
    if len(p) == 3:  # Single type and identifier
        add_to_symbol_table(p[2], p[1])


def p_type_or_void(p):
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
    if len(p) == 2:  # Single identifier
        add_to_symbol_table(p[1], p[-1])


def p_type(p):
    """type : INT
                | BOOLEAN"""
    p[0] = p[1]


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
    if parser.errorok:
        if len(p) > 3 and p[2] == '=':  # Assignment
            var_name = p[1]
            var = check_symbol_table(var_name)
            var_type = var['type']
            expr_type = p[3]
            if var_type != expr_type:
                print(f"Type mismatch: for Variable {var_name} type {var_type} expected, got {expr_type}.")
                parser.errorok = False


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
    """
    method_call : method_name  O_PAR arg C_PAR
           | CALLOUT O_PAR string_literal C_PAR
           | CALLOUT O_PAR string_literal COMMA call COMMA C_PAR
    """
    pass


def p_method_name(p):
    """method_name : IDENTIFIER"""
    pass


def p_arg(p):
    """
    arg : expr
      | expr COMMA arg
   """
    pass


def p_location(p):
    """ location : IDENTIFIER
           | IDENTIFIER O_BRACKET expr C_BRACKET"""
    var_name = p[1]
    check_symbol_table(var_name)
    p[0] = var_name


def p_expr(p):
    """
    expr : location
         | literal
         | expr bin_op expr
         | NEGATIVE expr
         | EXCL expr
         | O_PAR expr C_PAR
    """
    if len(p) == 2:  # Single element like location or literal
        p[0] = p[1]  # Pass the type or identifier from location/literal
    elif len(p) == 4:
        if p[2] in ('+', '-', '*', '/'):  # Binary operation
            left_type = p[1]
            right_type = p[3]
            if left_type != 'int' or right_type != 'int':
                raise TypeError(f"Arithmetic operations require integers: {left_type} and {right_type}")
            p[0] = 'int'  # Result of arithmetic operations is an int
        elif p[1] == '(' and p[3] == ')':  # Parentheses
            p[0] = p[2]  # Propagate inner expression type
    elif len(p) == 3:  # Unary operators like NEGATIVE or EXCL
        p[0] = p[2]  # Type remains the same for unary operations


def p_call(p):
    """
    call : callout_arg
     | callout_arg call
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
    p[0] = p[1]


def p_int_literal(p):
    """
    int_literal : DECIMAL
                    | HEXDECIMAL
    """
    p[0] = 'int'


def p_bool_literal(p):
    """
    bool_literal : TRUE
                    | FALSE
    """
    p[0] = 'boolean'


def p_char_literal(p):
    """
    char_literal : CHAR
    """
    p[0] = 'char'


def p_string_literal(p):
    """
    string_literal : STRING
    """
    p[0] = 'char[]'


def p_empty(p):
    """ empty : """
    pass


def p_error(p):
    line_number = 0
    if p is None:
        tok = 'end of file !'
    else:
        file = open(INPUT_FILE, "r")
        for line_number, line in enumerate(file, start=1):
            pass
        tok = f"{p.type}({p.value})on line {(p.lineno - line_number + 1)}"
    print(f"Syntax error : unexpected {tok}")


# Build the parser
parser = yacc.yacc()


def read_input_file(input_file: str = INPUT_FILE) -> str:
    try:
        with open('input.txt', 'r') as file:
            result = file.read()
            return result
    except FileNotFoundError as e:
        print(e)


parser.parse(read_input_file(INPUT_FILE))
print("----------------------------------")

if parser.errorok:
    print("compiled successfully")
    print(symbol_table)
