# Decaf Compiler — Python-Based Educational Compiler

This project implements a fully functional compiler for the Decaf programming language — a simplified, Java-like language designed for teaching compiler construction. The compiler is structured into four main phases: Lexical Analysis, Parsing, Semantic Analysis, and groundwork for Code Generation.

It demonstrates fundamental compiler design concepts through modular, readable, and testable Python code.
> 🗓️ Created: December 2024 | 🎓 5th Semester, Compiler Design Project: A Full Pipeline for a Simplified Java-like Language  

---

## Project Structure

| File | Description                                    |
|------|------------------------------------------------|
| `phase0_lexer_manual.py` | Manual lexer built using regular expressions   |
| `phase1_lexer_plyLib.py` | Lexer using the PLY (Python Lex-Yacc) library  |
| `phase2_parser_yacc.py` | Parser built using CFG and PLY's yacc module   |
| `phase3_semantic_analysis.py` | Performs semantic checks, builds symbol tables |
| `decaf.txt`, `input.txt` | Sample Decaf programs for input testing        |
| `grammar.txt`, `updated_grammar.txt` | Define Decaf grammar used by parser            |
| `parsetab.py` | Auto-generated parse table (PLY-generated)     |
| `TABLE1.csv` | token metadata for manual lexer                |

---

## Compiler Phases Overview

### 🔹 Phase 0: Manual Lexical Analyzer (`phase0_lexer_manual.py`)
- Implements tokenization logic manually using regular expressions.
- Identifies Decaf keywords, operators, identifiers, literals, and delimiters.
- Ideal for educational demonstration of how a lexer operates under the hood.

### 🔹 Phase 1: Lexer with PLY (`phase1_lexer_plyLib.py`)
- Uses the PLY library to define token rules.
- Simplifies tokenization via Python classes and pattern-matching.
- Outputs structured tokens including type and line number metadata.

### 🔹 Phase 2: Syntax Parser (`phase2_parser_yacc.py`)
- Parses tokens using a Context-Free Grammar defined in Python.
- Constructs a parse tree with full structure of the input program.
- Handles constructs like classes, methods, conditionals, loops, and expressions.

### 🔹 Phase 3: Semantic Analyzer (`phase3_semantic_analysis.py`)
- Walks the parse tree to validate type rules, function calls, variable scopes.
- Tracks declared identifiers and their scopes via symbol tables.
- Reports semantic errors with descriptive messages and location info.

---

## Technologies Used

| Area | Tools |
|------|-------|
| Programming Language | Python 3 |
| Lexer | Regular Expressions, PLY (Python Lex-Yacc) |
| Parser | PLY Yacc |
| Semantic Analysis | Custom logic in Python |
| Input/Output | Text-based input files, console output |

---

## Sample Decaf Input

Here's a sample Decaf program (from `decaf.txt`):

```java
class program {
  int x, y;
  
  void foo(int a, int b) {
    if (x == 10) {
      return;
    }
    
    while (y >= 5) {
      // do something
    }

    return;
  }
}
