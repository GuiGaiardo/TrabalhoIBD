# Generated from SQL.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


from SQL_Parser.QueryTree import *
query_tree = QueryTree()


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\23")
        buf.write("\u00f0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\n\6\np\n\n\r\n\16\nq\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\20\3\20\6\20\u0092\n\20\r\20\16\20\u0093")
        buf.write("\3\20\3\20\6\20\u0098\n\20\r\20\16\20\u0099\3\20\3\20")
        buf.write("\6\20\u009e\n\20\r\20\16\20\u009f\3\20\5\20\u00a3\n\20")
        buf.write("\5\20\u00a5\n\20\3\21\3\21\7\21\u00a9\n\21\f\21\16\21")
        buf.write("\u00ac\13\21\3\21\3\21\3\21\7\21\u00b1\n\21\f\21\16\21")
        buf.write("\u00b4\13\21\3\22\3\22\7\22\u00b8\n\22\f\22\16\22\u00bb")
        buf.write("\13\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3")
        buf.write("\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\3,\3,\2\2-\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\2\'\2)\2+\2-")
        buf.write("\2/\2\61\2\63\2\65\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\2K")
        buf.write("\2M\2O\2Q\2S\2U\2W\2\3\2\37\5\2\13\f\17\17\"\"\4\2C\\")
        buf.write("c|\5\2\62;C\\c|\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GG")
        buf.write("gg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2")
        buf.write("NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4")
        buf.write("\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{")
        buf.write("{\4\2\\\\||\u00de\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\3Y\3\2\2\2\5\\\3\2\2\2\7_\3\2\2\2\ta\3\2")
        buf.write("\2\2\13c\3\2\2\2\re\3\2\2\2\17g\3\2\2\2\21k\3\2\2\2\23")
        buf.write("o\3\2\2\2\25u\3\2\2\2\27|\3\2\2\2\31\u0081\3\2\2\2\33")
        buf.write("\u0087\3\2\2\2\35\u008c\3\2\2\2\37\u00a4\3\2\2\2!\u00a6")
        buf.write("\3\2\2\2#\u00b5\3\2\2\2%\u00bc\3\2\2\2\'\u00be\3\2\2\2")
        buf.write(")\u00c0\3\2\2\2+\u00c2\3\2\2\2-\u00c4\3\2\2\2/\u00c6\3")
        buf.write("\2\2\2\61\u00c8\3\2\2\2\63\u00ca\3\2\2\2\65\u00cc\3\2")
        buf.write("\2\2\67\u00ce\3\2\2\29\u00d0\3\2\2\2;\u00d2\3\2\2\2=\u00d4")
        buf.write("\3\2\2\2?\u00d6\3\2\2\2A\u00d8\3\2\2\2C\u00da\3\2\2\2")
        buf.write("E\u00dc\3\2\2\2G\u00de\3\2\2\2I\u00e0\3\2\2\2K\u00e2\3")
        buf.write("\2\2\2M\u00e4\3\2\2\2O\u00e6\3\2\2\2Q\u00e8\3\2\2\2S\u00ea")
        buf.write("\3\2\2\2U\u00ec\3\2\2\2W\u00ee\3\2\2\2YZ\7@\2\2Z[\7?\2")
        buf.write("\2[\4\3\2\2\2\\]\7>\2\2]^\7?\2\2^\6\3\2\2\2_`\7@\2\2`")
        buf.write("\b\3\2\2\2ab\7>\2\2b\n\3\2\2\2cd\7?\2\2d\f\3\2\2\2ef\7")
        buf.write(".\2\2f\16\3\2\2\2gh\7c\2\2hi\7p\2\2ij\7f\2\2j\20\3\2\2")
        buf.write("\2kl\7q\2\2lm\7t\2\2m\22\3\2\2\2np\t\2\2\2on\3\2\2\2p")
        buf.write("q\3\2\2\2qo\3\2\2\2qr\3\2\2\2rs\3\2\2\2st\b\n\2\2t\24")
        buf.write("\3\2\2\2uv\5I%\2vw\5-\27\2wx\5;\36\2xy\5-\27\2yz\5)\25")
        buf.write("\2z{\5K&\2{\26\3\2\2\2|}\5/\30\2}~\5G$\2~\177\5A!\2\177")
        buf.write("\u0080\5=\37\2\u0080\30\3\2\2\2\u0081\u0082\5Q)\2\u0082")
        buf.write("\u0083\5\63\32\2\u0083\u0084\5-\27\2\u0084\u0085\5G$\2")
        buf.write("\u0085\u0086\5-\27\2\u0086\32\3\2\2\2\u0087\u0088\5\67")
        buf.write("\34\2\u0088\u0089\5A!\2\u0089\u008a\5\65\33\2\u008a\u008b")
        buf.write("\5? \2\u008b\34\3\2\2\2\u008c\u008d\5A!\2\u008d\u008e")
        buf.write("\5? \2\u008e\36\3\2\2\2\u008f\u0091\7)\2\2\u0090\u0092")
        buf.write("\t\3\2\2\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\3\2\2\2")
        buf.write("\u0095\u00a5\7)\2\2\u0096\u0098\4\62;\2\u0097\u0096\3")
        buf.write("\2\2\2\u0098\u0099\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a")
        buf.write("\3\2\2\2\u009a\u00a2\3\2\2\2\u009b\u009d\7\60\2\2\u009c")
        buf.write("\u009e\4\62;\2\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a3\3")
        buf.write("\2\2\2\u00a1\u00a3\3\2\2\2\u00a2\u009b\3\2\2\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u008f\3\2\2\2\u00a4")
        buf.write("\u0097\3\2\2\2\u00a5 \3\2\2\2\u00a6\u00aa\t\3\2\2\u00a7")
        buf.write("\u00a9\t\4\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2")
        buf.write("\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\3")
        buf.write("\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\7\60\2\2\u00ae")
        buf.write("\u00b2\t\3\2\2\u00af\u00b1\t\4\2\2\u00b0\u00af\3\2\2\2")
        buf.write("\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3")
        buf.write("\2\2\2\u00b3\"\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b9")
        buf.write("\t\3\2\2\u00b6\u00b8\t\4\2\2\u00b7\u00b6\3\2\2\2\u00b8")
        buf.write("\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2")
        buf.write("\u00ba$\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd\t\5\2")
        buf.write("\2\u00bd&\3\2\2\2\u00be\u00bf\t\6\2\2\u00bf(\3\2\2\2\u00c0")
        buf.write("\u00c1\t\7\2\2\u00c1*\3\2\2\2\u00c2\u00c3\t\b\2\2\u00c3")
        buf.write(",\3\2\2\2\u00c4\u00c5\t\t\2\2\u00c5.\3\2\2\2\u00c6\u00c7")
        buf.write("\t\n\2\2\u00c7\60\3\2\2\2\u00c8\u00c9\t\13\2\2\u00c9\62")
        buf.write("\3\2\2\2\u00ca\u00cb\t\f\2\2\u00cb\64\3\2\2\2\u00cc\u00cd")
        buf.write("\t\r\2\2\u00cd\66\3\2\2\2\u00ce\u00cf\t\16\2\2\u00cf8")
        buf.write("\3\2\2\2\u00d0\u00d1\t\17\2\2\u00d1:\3\2\2\2\u00d2\u00d3")
        buf.write("\t\20\2\2\u00d3<\3\2\2\2\u00d4\u00d5\t\21\2\2\u00d5>\3")
        buf.write("\2\2\2\u00d6\u00d7\t\22\2\2\u00d7@\3\2\2\2\u00d8\u00d9")
        buf.write("\t\23\2\2\u00d9B\3\2\2\2\u00da\u00db\t\24\2\2\u00dbD\3")
        buf.write("\2\2\2\u00dc\u00dd\t\25\2\2\u00ddF\3\2\2\2\u00de\u00df")
        buf.write("\t\26\2\2\u00dfH\3\2\2\2\u00e0\u00e1\t\27\2\2\u00e1J\3")
        buf.write("\2\2\2\u00e2\u00e3\t\30\2\2\u00e3L\3\2\2\2\u00e4\u00e5")
        buf.write("\t\31\2\2\u00e5N\3\2\2\2\u00e6\u00e7\t\32\2\2\u00e7P\3")
        buf.write("\2\2\2\u00e8\u00e9\t\33\2\2\u00e9R\3\2\2\2\u00ea\u00eb")
        buf.write("\t\34\2\2\u00ebT\3\2\2\2\u00ec\u00ed\t\35\2\2\u00edV\3")
        buf.write("\2\2\2\u00ee\u00ef\t\36\2\2\u00efX\3\2\2\2\f\2q\u0093")
        buf.write("\u0099\u009f\u00a2\u00a4\u00aa\u00b2\u00b9\3\2\3\2")
        return buf.getvalue()


class SQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    WS = 9
    SELECT = 10
    FROM = 11
    WHERE = 12
    JOIN = 13
    ON = 14
    ATRIBUTO = 15
    COLUNA = 16
    TABELA = 17

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'>='", "'<='", "'>'", "'<'", "'='", "','", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "SELECT", "FROM", "WHERE", "JOIN", "ON", "ATRIBUTO", "COLUNA", 
            "TABELA" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "WS", "SELECT", "FROM", "WHERE", "JOIN", "ON", 
                  "ATRIBUTO", "COLUNA", "TABELA", "A", "B", "C", "D", "E", 
                  "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
                  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

    grammarFileName = "SQL.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


