# Generated from teste.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\17")
        buf.write("K\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\6\b+\n\b\r\b\16\b,\3\t\3\t\5\t\61\n\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\5\138\n\13\3\f\3\f\3\f\3\f\3\r\3\r\7\r@\n\r")
        buf.write("\f\r\16\rC\13\r\3\16\6\16F\n\16\r\16\16\16G\3\16\3\16")
        buf.write("\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\3\2\7\4\2\f\f\17\17\4\2>>@@\4\2C\\c")
        buf.write("|\5\2\62;C\\c|\5\2\13\f\17\17\"\"O\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37")
        buf.write("\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2")
        buf.write("\17*\3\2\2\2\21\60\3\2\2\2\23\62\3\2\2\2\25\67\3\2\2\2")
        buf.write("\279\3\2\2\2\31=\3\2\2\2\33E\3\2\2\2\35\36\7*\2\2\36\4")
        buf.write("\3\2\2\2\37 \7+\2\2 \6\3\2\2\2!\"\7\60\2\2\"\b\3\2\2\2")
        buf.write("#$\7.\2\2$\n\3\2\2\2%&\7R\2\2&\f\3\2\2\2\'(\7U\2\2(\16")
        buf.write("\3\2\2\2)+\t\2\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2")
        buf.write("\2\2-\20\3\2\2\2.\61\t\3\2\2/\61\5\23\n\2\60.\3\2\2\2")
        buf.write("\60/\3\2\2\2\61\22\3\2\2\2\62\63\7?\2\2\63\24\3\2\2\2")
        buf.write("\648\5\27\f\2\65\66\7q\2\2\668\7t\2\2\67\64\3\2\2\2\67")
        buf.write("\65\3\2\2\28\26\3\2\2\29:\7c\2\2:;\7p\2\2;<\7f\2\2<\30")
        buf.write("\3\2\2\2=A\t\4\2\2>@\t\5\2\2?>\3\2\2\2@C\3\2\2\2A?\3\2")
        buf.write("\2\2AB\3\2\2\2B\32\3\2\2\2CA\3\2\2\2DF\t\6\2\2ED\3\2\2")
        buf.write("\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\b\16\2\2")
        buf.write("J\34\3\2\2\2\b\2,\60\67AG\3\b\2\2")
        return buf.getvalue()


class testeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    NEWLINE = 7
    COMPARISON_OP = 8
    EQUAL = 9
    BOOLEAN_OP = 10
    AND = 11
    ID = 12
    WS = 13

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'.'", "','", "'P'", "'S'", "'='", "'and'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "COMPARISON_OP", "EQUAL", "BOOLEAN_OP", "AND", "ID", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "NEWLINE", 
                  "COMPARISON_OP", "EQUAL", "BOOLEAN_OP", "AND", "ID", "WS" ]

    grammarFileName = "teste.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


