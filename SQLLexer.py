# Generated from SQL.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\r")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\5\6\5#\n\5\r\5\16\5$\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\7\13E\n\13\f\13\16\13H\13\13\3\13\3\13\3\13\7\13")
        buf.write("M\n\13\f\13\16\13P\13\13\3\f\3\f\7\fT\n\f\f\f\16\fW\13")
        buf.write("\f\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\3\2\5\5\2\13\f\17\17\"\"\4\2C\\c|\5\2\62;C\\c|[")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\33\3\2")
        buf.write("\2\2\7\35\3\2\2\2\t\"\3\2\2\2\13(\3\2\2\2\r/\3\2\2\2\17")
        buf.write("\64\3\2\2\2\21:\3\2\2\2\23?\3\2\2\2\25B\3\2\2\2\27Q\3")
        buf.write("\2\2\2\31\32\7.\2\2\32\4\3\2\2\2\33\34\7?\2\2\34\6\3\2")
        buf.write("\2\2\35\36\7c\2\2\36\37\7p\2\2\37 \7f\2\2 \b\3\2\2\2!")
        buf.write("#\t\2\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%&")
        buf.write("\3\2\2\2&\'\b\5\2\2\'\n\3\2\2\2()\7U\2\2)*\7G\2\2*+\7")
        buf.write("N\2\2+,\7G\2\2,-\7E\2\2-.\7V\2\2.\f\3\2\2\2/\60\7H\2\2")
        buf.write("\60\61\7T\2\2\61\62\7Q\2\2\62\63\7O\2\2\63\16\3\2\2\2")
        buf.write("\64\65\7Y\2\2\65\66\7J\2\2\66\67\7G\2\2\678\7T\2\289\7")
        buf.write("G\2\29\20\3\2\2\2:;\7L\2\2;<\7Q\2\2<=\7K\2\2=>\7P\2\2")
        buf.write(">\22\3\2\2\2?@\7Q\2\2@A\7P\2\2A\24\3\2\2\2BF\t\3\2\2C")
        buf.write("E\t\4\2\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3")
        buf.write("\2\2\2HF\3\2\2\2IJ\7\60\2\2JN\t\3\2\2KM\t\4\2\2LK\3\2")
        buf.write("\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\26\3\2\2\2PN\3\2\2")
        buf.write("\2QU\t\3\2\2RT\t\4\2\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2U")
        buf.write("V\3\2\2\2V\30\3\2\2\2WU\3\2\2\2\7\2$FNU\3\2\3\2")
        return buf.getvalue()


class SQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    WS = 4
    SELECT = 5
    FROM = 6
    WHERE = 7
    JOIN = 8
    ON = 9
    COLUNA = 10
    TABELA = 11

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'='", "'and'", "'SELECT'", "'FROM'", "'WHERE'", "'JOIN'", 
            "'ON'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "SELECT", "FROM", "WHERE", "JOIN", "ON", "COLUNA", "TABELA" ]

    ruleNames = [ "T__0", "T__1", "T__2", "WS", "SELECT", "FROM", "WHERE", 
                  "JOIN", "ON", "COLUNA", "TABELA" ]

    grammarFileName = "SQL.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


