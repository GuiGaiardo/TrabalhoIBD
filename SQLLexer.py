# Generated from SQL.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\t")
        buf.write("B\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\3\6\3\25\n\3\r\3\16\3\26\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\7\7/\n\7\f\7\16\7\62\13\7\3\7")
        buf.write("\3\7\3\7\7\7\67\n\7\f\7\16\7:\13\7\3\b\3\b\7\b>\n\b\f")
        buf.write("\b\16\bA\13\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2")
        buf.write("\5\5\2\13\f\17\17\"\"\4\2C\\c|\5\2\62;C\\c|E\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\24\3\2\2\2\7\32")
        buf.write("\3\2\2\2\t!\3\2\2\2\13&\3\2\2\2\r,\3\2\2\2\17;\3\2\2\2")
        buf.write("\21\22\7.\2\2\22\4\3\2\2\2\23\25\t\2\2\2\24\23\3\2\2\2")
        buf.write("\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\30\3\2\2")
        buf.write("\2\30\31\b\3\2\2\31\6\3\2\2\2\32\33\7U\2\2\33\34\7G\2")
        buf.write("\2\34\35\7N\2\2\35\36\7G\2\2\36\37\7E\2\2\37 \7V\2\2 ")
        buf.write("\b\3\2\2\2!\"\7H\2\2\"#\7T\2\2#$\7Q\2\2$%\7O\2\2%\n\3")
        buf.write("\2\2\2&\'\7Y\2\2\'(\7J\2\2()\7G\2\2)*\7T\2\2*+\7G\2\2")
        buf.write("+\f\3\2\2\2,\60\t\3\2\2-/\t\4\2\2.-\3\2\2\2/\62\3\2\2")
        buf.write("\2\60.\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62\60\3\2\2")
        buf.write("\2\63\64\7\60\2\2\648\t\3\2\2\65\67\t\4\2\2\66\65\3\2")
        buf.write("\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29\16\3\2\2\2:8\3")
        buf.write("\2\2\2;?\t\3\2\2<>\t\4\2\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2")
        buf.write("\2?@\3\2\2\2@\20\3\2\2\2A?\3\2\2\2\7\2\26\608?\3\2\3\2")
        return buf.getvalue()


class SQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    WS = 2
    SELECT = 3
    FROM = 4
    WHERE = 5
    COLUNA = 6
    TABELA = 7

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'SELECT'", "'FROM'", "'WHERE'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "SELECT", "FROM", "WHERE", "COLUNA", "TABELA" ]

    ruleNames = [ "T__0", "WS", "SELECT", "FROM", "WHERE", "COLUNA", "TABELA" ]

    grammarFileName = "SQL.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


