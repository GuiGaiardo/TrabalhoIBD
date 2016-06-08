# Generated from SQL.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\b")
        buf.write(">\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\6\2\21\n\2\r\2\16\2\22\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\7\6+\n\6\f\6\16\6.\13\6\3\6\3\6\3\6\7\6\63\n")
        buf.write("\6\f\6\16\6\66\13\6\3\7\3\7\7\7:\n\7\f\7\16\7=\13\7\2")
        buf.write("\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2\5\5\2\13\f\17\17\"\"")
        buf.write("\4\2C\\c|\5\2\62;C\\c|A\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\20\3\2\2")
        buf.write("\2\5\26\3\2\2\2\7\35\3\2\2\2\t\"\3\2\2\2\13(\3\2\2\2\r")
        buf.write("\67\3\2\2\2\17\21\t\2\2\2\20\17\3\2\2\2\21\22\3\2\2\2")
        buf.write("\22\20\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24\25\b\2\2")
        buf.write("\2\25\4\3\2\2\2\26\27\7U\2\2\27\30\7G\2\2\30\31\7N\2\2")
        buf.write("\31\32\7G\2\2\32\33\7E\2\2\33\34\7V\2\2\34\6\3\2\2\2\35")
        buf.write("\36\7H\2\2\36\37\7T\2\2\37 \7Q\2\2 !\7O\2\2!\b\3\2\2\2")
        buf.write("\"#\7Y\2\2#$\7J\2\2$%\7G\2\2%&\7T\2\2&\'\7G\2\2\'\n\3")
        buf.write("\2\2\2(,\t\3\2\2)+\t\4\2\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2")
        buf.write("\2,-\3\2\2\2-/\3\2\2\2.,\3\2\2\2/\60\7\60\2\2\60\64\t")
        buf.write("\3\2\2\61\63\t\4\2\2\62\61\3\2\2\2\63\66\3\2\2\2\64\62")
        buf.write("\3\2\2\2\64\65\3\2\2\2\65\f\3\2\2\2\66\64\3\2\2\2\67;")
        buf.write("\t\3\2\28:\t\4\2\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2")
        buf.write("\2\2<\16\3\2\2\2=;\3\2\2\2\7\2\22,\64;\3\2\3\2")
        return buf.getvalue()


class SQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    WS = 1
    SELECT = 2
    FROM = 3
    WHERE = 4
    COLUNA = 5
    TABELA = 6

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'SELECT'", "'FROM'", "'WHERE'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "SELECT", "FROM", "WHERE", "COLUNA", "TABELA" ]

    ruleNames = [ "WS", "SELECT", "FROM", "WHERE", "COLUNA", "TABELA" ]

    grammarFileName = "SQL.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


