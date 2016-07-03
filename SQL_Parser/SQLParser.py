# Generated from SQL.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO


from SQL_Parser.QueryTree import *
query_tree = QueryTree()

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\23")
        buf.write("\u0085\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5\3\5\3\5\5\5\64\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6=\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7J\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\\")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\nm\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\5\13y\n\13\3\f\3\f\3\r\7\r~\n\r\f\r\16")
        buf.write("\r\u0081\13\r\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\2\4\3\2\3\7\3\2\t\n\u0082\2\32\3\2\2\2\4\"\3")
        buf.write("\2\2\2\6,\3\2\2\2\b\63\3\2\2\2\n<\3\2\2\2\fI\3\2\2\2\16")
        buf.write("K\3\2\2\2\20[\3\2\2\2\22l\3\2\2\2\24x\3\2\2\2\26z\3\2")
        buf.write("\2\2\30\177\3\2\2\2\32\33\7\f\2\2\33\34\5\n\6\2\34\35")
        buf.write("\7\r\2\2\35\36\5\22\n\2\36\37\5\b\5\2\37 \5\30\r\2 !\b")
        buf.write("\2\1\2!\3\3\2\2\2\"#\t\2\2\2#\5\3\2\2\2$%\5\24\13\2%&")
        buf.write("\5\26\f\2&\'\5\6\4\2\'(\b\4\1\2(-\3\2\2\2)*\5\24\13\2")
        buf.write("*+\b\4\1\2+-\3\2\2\2,$\3\2\2\2,)\3\2\2\2-\7\3\2\2\2./")
        buf.write("\7\16\2\2/\60\5\6\4\2\60\61\b\5\1\2\61\64\3\2\2\2\62\64")
        buf.write("\b\5\1\2\63.\3\2\2\2\63\62\3\2\2\2\64\t\3\2\2\2\65\66")
        buf.write("\7\22\2\2\66\67\7\b\2\2\678\5\n\6\289\b\6\1\29=\3\2\2")
        buf.write("\2:;\7\22\2\2;=\b\6\1\2<\65\3\2\2\2<:\3\2\2\2=\13\3\2")
        buf.write("\2\2>?\7\22\2\2?@\7\7\2\2@A\7\22\2\2AB\5\26\f\2BC\5\f")
        buf.write("\7\2CD\b\7\1\2DJ\3\2\2\2EF\7\22\2\2FG\7\7\2\2GH\7\22\2")
        buf.write("\2HJ\b\7\1\2I>\3\2\2\2IE\3\2\2\2J\r\3\2\2\2KL\7\23\2\2")
        buf.write("LM\7\17\2\2MN\7\23\2\2NO\7\20\2\2OP\5\f\7\2PQ\5\20\t\2")
        buf.write("QR\b\b\1\2R\17\3\2\2\2ST\7\17\2\2TU\7\23\2\2UV\7\20\2")
        buf.write("\2VW\5\f\7\2WX\5\20\t\2XY\b\t\1\2Y\\\3\2\2\2Z\\\b\t\1")
        buf.write("\2[S\3\2\2\2[Z\3\2\2\2\\\21\3\2\2\2]^\7\23\2\2^_\7\b\2")
        buf.write("\2_`\5\22\n\2`a\b\n\1\2am\3\2\2\2bc\5\16\b\2cd\b\n\1\2")
        buf.write("dm\3\2\2\2ef\5\16\b\2fg\7\b\2\2gh\5\22\n\2hi\b\n\1\2i")
        buf.write("m\3\2\2\2jk\7\23\2\2km\b\n\1\2l]\3\2\2\2lb\3\2\2\2le\3")
        buf.write("\2\2\2lj\3\2\2\2m\23\3\2\2\2no\7\22\2\2op\5\4\3\2pq\7")
        buf.write("\22\2\2qr\b\13\1\2ry\3\2\2\2st\7\22\2\2tu\5\4\3\2uv\7")
        buf.write("\21\2\2vw\b\13\1\2wy\3\2\2\2xn\3\2\2\2xs\3\2\2\2y\25\3")
        buf.write("\2\2\2z{\t\3\2\2{\27\3\2\2\2|~\13\2\2\2}|\3\2\2\2~\u0081")
        buf.write("\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3")
        buf.write("\2\2\2\u0081\177\3\2\2\2\u0082\u0083\b\r\1\2\u0083\31")
        buf.write("\3\2\2\2\n,\63<I[lx\177")
        return buf.getvalue()


class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'>='", "'<='", "'>'", "'<'", "'='", "','", 
                     "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "SELECT", "FROM", "WHERE", "JOIN", 
                      "ON", "ATRIBUTO", "COLUNA", "TABELA" ]

    RULE_sql_expr = 0
    RULE_comparisonOp = 1
    RULE_conditionsWhere = 2
    RULE_where = 3
    RULE_clausulaSelect = 4
    RULE_conditionsJoin = 5
    RULE_joins = 6
    RULE_joins_ = 7
    RULE_clausulaFrom = 8
    RULE_termo = 9
    RULE_conector = 10
    RULE_anythingElse = 11

    ruleNames =  [ "sql_expr", "comparisonOp", "conditionsWhere", "where", 
                   "clausulaSelect", "conditionsJoin", "joins", "joins_", 
                   "clausulaFrom", "termo", "conector", "anythingElse" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    WS=9
    SELECT=10
    FROM=11
    WHERE=12
    JOIN=13
    ON=14
    ATRIBUTO=15
    COLUNA=16
    TABELA=17

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Sql_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.sl = None # ClausulaSelectContext
            self.fr = None # ClausulaFromContext
            self.w = None # WhereContext
            self.r = None # AnythingElseContext

        def SELECT(self):
            return self.getToken(SQLParser.SELECT, 0)

        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def clausulaSelect(self):
            return self.getTypedRuleContext(SQLParser.ClausulaSelectContext,0)


        def clausulaFrom(self):
            return self.getTypedRuleContext(SQLParser.ClausulaFromContext,0)


        def where(self):
            return self.getTypedRuleContext(SQLParser.WhereContext,0)


        def anythingElse(self):
            return self.getTypedRuleContext(SQLParser.AnythingElseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_sql_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_expr" ):
                listener.enterSql_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_expr" ):
                listener.exitSql_expr(self)




    def sql_expr(self):

        localctx = SQLParser.Sql_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sql_expr)

        number = 0
        valid_query = False
        projection = None
        query_tree.set_root(None)

        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(SQLParser.SELECT)
            self.state = 25
            localctx.sl = self.clausulaSelect()
            self.state = 26
            self.match(SQLParser.FROM)
            self.state = 27
            localctx.fr = self.clausulaFrom( [] )
            self.state = 28
            localctx.w = self.where()
            self.state = 29
            localctx.r = self.anythingElse()
            projection = ProjectionNode(localctx.sl.columns)
            theta_join = localctx.fr.tj



            if(localctx.sl.columns is None):
                selectingTables = []
            else:
                selectingTables = [x.split('.')[0] for x in localctx.sl.columns]
            if(localctx.w.terms is None):
                whereTables = []
            else:
                whereTables = [x[0].split('.')[0] for x in localctx.w.terms]
            valid_query = 1


            if(localctx.sl.columns is None):
                projection = None
                valid_query = 0

            if(localctx.fr.tj is None):
                valid_query = 0
                projection = None

            if(not localctx.fr.tables is None):
                for t in selectingTables:
                    if(not t in localctx.fr.tables):
                        print("Selecting unknow table " + t)
                        valid_query = 0
                        projection = None

                for t in whereTables:
                    if(not t in localctx.fr.tables):
                        print("Unknown table " + t + " being used in where clause")
                        valid_query = 0
                        projection = None


            if(localctx.w.terms is None):
                valid_query = 0

            if valid_query:
                if len(localctx.w.terms) > 0:
                    selection = SelectionNode(localctx.w.terms, localctx.w.conectors)
                    selection.set_child(theta_join)
                    projection.set_child(selection)

                else:
                    projection.set_child(theta_join)

            else:
                projection = None

            if localctx.r.trailing_str == None or localctx.r.trailing_str.strip(" ") == "":
                pass
            else:
                projection = None
                print("Not viable input at ", localctx.r.trailing_str)



            query_tree.set_root(projection)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)




    def comparisonOp(self):

        localctx = SQLParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.T__0) | (1 << SQLParser.T__1) | (1 << SQLParser.T__2) | (1 << SQLParser.T__3) | (1 << SQLParser.T__4))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionsWhereContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.terms = None
            self.conectors = None
            self.t = None # TermoContext
            self.c = None # ConectorContext
            self.cnd = None # ConditionsWhereContext

        def termo(self):
            return self.getTypedRuleContext(SQLParser.TermoContext,0)


        def conector(self):
            return self.getTypedRuleContext(SQLParser.ConectorContext,0)


        def conditionsWhere(self):
            return self.getTypedRuleContext(SQLParser.ConditionsWhereContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_conditionsWhere

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionsWhere" ):
                listener.enterConditionsWhere(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionsWhere" ):
                listener.exitConditionsWhere(self)




    def conditionsWhere(self):

        localctx = SQLParser.ConditionsWhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conditionsWhere)
        try:
            self.state = 42
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                localctx.t = self.termo()
                self.state = 35
                localctx.c = self.conector()
                self.state = 36
                localctx.cnd = self.conditionsWhere()
                localctx.terms = localctx.cnd.terms
                localctx.terms.append(localctx.t.term)
                localctx.conectors = localctx.cnd.conectors
                localctx.conectors.append((None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                localctx.t = self.termo()
                localctx.terms = [localctx.t.term]
                localctx.conectors = []
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhereContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.terms = None
            self.conectors = None
            self.c = None # ConditionsWhereContext

        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def conditionsWhere(self):
            return self.getTypedRuleContext(SQLParser.ConditionsWhereContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_where

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere" ):
                listener.enterWhere(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere" ):
                listener.exitWhere(self)




    def where(self):

        localctx = SQLParser.WhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_where)
        try:
            self.state = 49
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(SQLParser.WHERE)
                self.state = 45
                localctx.c = self.conditionsWhere()
                localctx.terms = localctx.c.terms
                localctx.conectors = localctx.c.conectors
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                localctx.terms = []
                localctx.conectors = []
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClausulaSelectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.columns = None
            self.c = None # Token
            self.c1 = None # ClausulaSelectContext

        def COLUNA(self):
            return self.getToken(SQLParser.COLUNA, 0)

        def clausulaSelect(self):
            return self.getTypedRuleContext(SQLParser.ClausulaSelectContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_clausulaSelect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClausulaSelect" ):
                listener.enterClausulaSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClausulaSelect" ):
                listener.exitClausulaSelect(self)




    def clausulaSelect(self):

        localctx = SQLParser.ClausulaSelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_clausulaSelect)
        try:
            self.state = 58
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                localctx.c = self.match(SQLParser.COLUNA)
                self.state = 52
                self.match(SQLParser.T__5)
                self.state = 53
                localctx.c1 = self.clausulaSelect()
                localctx.columns = localctx.c1.columns
                localctx.columns.append((None if localctx.c is None else localctx.c.text))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(SQLParser.COLUNA)
                localctx.columns = [self._input.getText((localctx.start, self._input.LT(-1)))]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionsJoinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.terms = None
            self.conectors = None
            self.c1 = None # Token
            self.c2 = None # Token
            self.c = None # ConectorContext
            self.cnd = None # ConditionsJoinContext

        def COLUNA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COLUNA)
            else:
                return self.getToken(SQLParser.COLUNA, i)

        def conector(self):
            return self.getTypedRuleContext(SQLParser.ConectorContext,0)


        def conditionsJoin(self):
            return self.getTypedRuleContext(SQLParser.ConditionsJoinContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_conditionsJoin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionsJoin" ):
                listener.enterConditionsJoin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionsJoin" ):
                listener.exitConditionsJoin(self)




    def conditionsJoin(self):

        localctx = SQLParser.ConditionsJoinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditionsJoin)
        try:
            self.state = 71
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                localctx.c1 = self.match(SQLParser.COLUNA)
                self.state = 61
                self.match(SQLParser.T__4)
                self.state = 62
                localctx.c2 = self.match(SQLParser.COLUNA)
                self.state = 63
                localctx.c = self.conector()
                self.state = 64
                localctx.cnd = self.conditionsJoin()
                localctx.terms = localctx.cnd.terms
                localctx.terms.append(((None if localctx.c1 is None else localctx.c1.text),"=",(None if localctx.c2 is None else localctx.c2.text)))
                localctx.conectors = localctx.cnd.conectors
                localctx.conectors.append((None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                localctx.c1 = self.match(SQLParser.COLUNA)
                self.state = 68
                self.match(SQLParser.T__4)
                self.state = 69
                localctx.c2 = self.match(SQLParser.COLUNA)
                localctx.terms = [((None if localctx.c1 is None else localctx.c1.text), "=", (None if localctx.c2 is None else localctx.c2.text))]
                localctx.conectors = []
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JoinsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, tablesSoFar=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tablesSoFar = None
            self.tj = None
            self.tables = None
            self.t1 = None # Token
            self.t2 = None # Token
            self.c = None # ConditionsJoinContext
            self.j = None # Joins_Context
            self.tablesSoFar = tablesSoFar

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def TABELA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.TABELA)
            else:
                return self.getToken(SQLParser.TABELA, i)

        def conditionsJoin(self):
            return self.getTypedRuleContext(SQLParser.ConditionsJoinContext,0)


        def joins_(self):
            return self.getTypedRuleContext(SQLParser.Joins_Context,0)


        def getRuleIndex(self):
            return SQLParser.RULE_joins

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoins" ):
                listener.enterJoins(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoins" ):
                listener.exitJoins(self)




    def joins(self, tablesSoFar):

        localctx = SQLParser.JoinsContext(self, self._ctx, self.state, tablesSoFar)
        self.enterRule(localctx, 12, self.RULE_joins)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            localctx.t1 = self.match(SQLParser.TABELA)
            self.state = 74
            self.match(SQLParser.JOIN)
            self.state = 75
            localctx.t2 = self.match(SQLParser.TABELA)
            self.state = 76
            self.match(SQLParser.ON)
            self.state = 77
            localctx.c = self.conditionsJoin()
            self.state = 78
            localctx.j = self.joins_(localctx.tablesSoFar + [(None if localctx.t1 is None else localctx.t1.text)] + [(None if localctx.t2 is None else localctx.t2.text)])
            join1 = ThetaJoinNode(Table((None if localctx.t1 is None else localctx.t1.text)), Table((None if localctx.t2 is None else localctx.t2.text)), localctx.c.terms, localctx.c.conectors)
            print(localctx.tablesSoFar)
            localctx.tables = [(None if localctx.t1 is None else localctx.t1.text), (None if localctx.t2 is None else localctx.t2.text)] + localctx.j.table
            if (localctx.j.table == []):
                localctx.tj = join1
            else:
                last_join = join1
                for i in range(len(localctx.j.table)):
                    last_join = ThetaJoinNode(last_join, Table(localctx.j.table[i]), localctx.j.terms[i], localctx.j.conectors[i])
                    localctx.tj = last_join

            for term in localctx.c.terms:
                table1 = term[0].split('.')[0]
                table2 = term[2].split('.')[0]
                if table1 not in (localctx.tablesSoFar + [(None if localctx.t1 is None else localctx.t1.text)] + [(None if localctx.t2 is None else localctx.t2.text)]):
                    print("Unknown table " + table1 + " referenced in JOIN condition")
                    localctx.tj = None
                if table2 not in (localctx.tablesSoFar + [(None if localctx.t1 is None else localctx.t1.text)] + [(None if localctx.t2 is None else localctx.t2.text)]):
                    print("Unknown table " + table2 + " referenced in JOIN condition")
                    localctx.tj = None

            if None in localctx.j.table:
                localctx.tj = None

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Joins_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, tablesSoFar=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tablesSoFar = None
            self.table = None
            self.terms = None
            self.conectors = None
            self.t = None # Token
            self.c = None # ConditionsJoinContext
            self.j = None # Joins_Context
            self.tablesSoFar = tablesSoFar

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def TABELA(self):
            return self.getToken(SQLParser.TABELA, 0)

        def conditionsJoin(self):
            return self.getTypedRuleContext(SQLParser.ConditionsJoinContext,0)


        def joins_(self):
            return self.getTypedRuleContext(SQLParser.Joins_Context,0)


        def getRuleIndex(self):
            return SQLParser.RULE_joins_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoins_" ):
                listener.enterJoins_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoins_" ):
                listener.exitJoins_(self)




    def joins_(self, tablesSoFar):

        localctx = SQLParser.Joins_Context(self, self._ctx, self.state, tablesSoFar)
        self.enterRule(localctx, 14, self.RULE_joins_)
        try:
            self.state = 89
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(SQLParser.JOIN)
                self.state = 82
                localctx.t = self.match(SQLParser.TABELA)
                self.state = 83
                self.match(SQLParser.ON)
                self.state = 84
                localctx.c = self.conditionsJoin()
                self.state = 85
                localctx.j = self.joins_(localctx.tablesSoFar + [(None if localctx.t is None else localctx.t.text)])
                localctx.table = (None if localctx.t is None else localctx.t.text)
                print(localctx.tablesSoFar)
                localctx.terms = [localctx.c.terms] + localctx.j.terms
                localctx.conectors = [localctx.c.conectors] + localctx.j.conectors
                localctx.table = [(None if localctx.t is None else localctx.t.text)] + localctx.j.table
                for term in localctx.c.terms:
                    table1 = term[0].split('.')[0]
                    table2 = term[2].split('.')[0]

                    if table1 not in (localctx.tablesSoFar + [(None if localctx.t is None else localctx.t.text)]):
                        print("Unknown table " + table1 + " referenced in JOIN condition")
                        localctx.table += [None]
                    if table2 not in (localctx.tablesSoFar + [(None if localctx.t is None else localctx.t.text)]):
                        print("Unknown table " + table2 + " referenced in JOIN condition")
                        localctx.table += [None]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                localctx.table = []
                localctx.terms = []
                localctx.conectors = []
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClausulaFromContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, tablesSoFar=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tablesSoFar = None
            self.tj = None
            self.tables = None
            self.t1 = None # Token
            self.c = None # ClausulaFromContext
            self.j = None # JoinsContext
            self.t = None # Token
            self.tablesSoFar = tablesSoFar

        def TABELA(self):
            return self.getToken(SQLParser.TABELA, 0)

        def clausulaFrom(self):
            return self.getTypedRuleContext(SQLParser.ClausulaFromContext,0)


        def joins(self):
            return self.getTypedRuleContext(SQLParser.JoinsContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_clausulaFrom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClausulaFrom" ):
                listener.enterClausulaFrom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClausulaFrom" ):
                listener.exitClausulaFrom(self)




    def clausulaFrom(self, tablesSoFar):

        localctx = SQLParser.ClausulaFromContext(self, self._ctx, self.state, tablesSoFar)
        self.enterRule(localctx, 16, self.RULE_clausulaFrom)
        try:
            self.state = 106
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                localctx.t1 = self.match(SQLParser.TABELA)
                self.state = 92
                self.match(SQLParser.T__5)
                self.state = 93
                localctx.c = self.clausulaFrom(localctx.tablesSoFar)
                tab = Table((None if localctx.t1 is None else localctx.t1.text))

                if localctx.c.tj is None:
                    join = None
                else:
                    join = ThetaJoinNode(tab, localctx.c.tj, [','], [])
                localctx.tj = join
                localctx.tables = [(None if localctx.t1 is None else localctx.t1.text)] + localctx.c.tables
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                localctx.j = self.joins(localctx.tablesSoFar)
                localctx.tj = localctx.j.tj
                localctx.tables = localctx.j.tables
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                localctx.j = self.joins(localctx.tablesSoFar)
                self.state = 100
                self.match(SQLParser.T__5)
                self.state = 101
                localctx.c = self.clausulaFrom(localctx.j.tables + localctx.tablesSoFar )


                if localctx.c.tj is None or localctx.j.tj is None:
                    localctx.tj = None
                else:
                    localctx.tj = ThetaJoinNode(localctx.j.tj, localctx.c.tj, [','], [])
                localctx.tables = localctx.j.tables + localctx.c.tables
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                localctx.t = self.match(SQLParser.TABELA)
                table = Table(self._input.getText((localctx.start, self._input.LT(-1))))
                localctx.tj = table
                localctx.tables = [(None if localctx.t is None else localctx.t.text)]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.term = None
            self.t1 = None # Token
            self.o = None # ComparisonOpContext
            self.t2 = None # Token
            self.t = None # Token
            self.a = None # Token

        def COLUNA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COLUNA)
            else:
                return self.getToken(SQLParser.COLUNA, i)

        def comparisonOp(self):
            return self.getTypedRuleContext(SQLParser.ComparisonOpContext,0)


        def ATRIBUTO(self):
            return self.getToken(SQLParser.ATRIBUTO, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = SQLParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_termo)
        try:
            self.state = 118
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                localctx.t1 = self.match(SQLParser.COLUNA)
                self.state = 109
                localctx.o = self.comparisonOp()
                self.state = 110
                localctx.t2 = self.match(SQLParser.COLUNA)
                localctx.term = ((None if localctx.t1 is None else localctx.t1.text),(None if localctx.o is None else self._input.getText((localctx.o.start,localctx.o.stop))),(None if localctx.t2 is None else localctx.t2.text))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                localctx.t = self.match(SQLParser.COLUNA)
                self.state = 114
                localctx.o = self.comparisonOp()
                self.state = 115
                localctx.a = self.match(SQLParser.ATRIBUTO)
                localctx.term = ((None if localctx.t is None else localctx.t.text),(None if localctx.o is None else self._input.getText((localctx.o.start,localctx.o.stop))),(None if localctx.a is None else localctx.a.text))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConectorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_conector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConector" ):
                listener.enterConector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConector" ):
                listener.exitConector(self)




    def conector(self):

        localctx = SQLParser.ConectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_conector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not(_la==SQLParser.T__6 or _la==SQLParser.T__7):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AnythingElseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.trailing_str = None
            self.t = None # Token


        def getRuleIndex(self):
            return SQLParser.RULE_anythingElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnythingElse" ):
                listener.enterAnythingElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnythingElse" ):
                listener.exitAnythingElse(self)




    def anythingElse(self):

        localctx = SQLParser.AnythingElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_anythingElse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.T__0) | (1 << SQLParser.T__1) | (1 << SQLParser.T__2) | (1 << SQLParser.T__3) | (1 << SQLParser.T__4) | (1 << SQLParser.T__5) | (1 << SQLParser.T__6) | (1 << SQLParser.T__7) | (1 << SQLParser.WS) | (1 << SQLParser.SELECT) | (1 << SQLParser.FROM) | (1 << SQLParser.WHERE) | (1 << SQLParser.JOIN) | (1 << SQLParser.ON) | (1 << SQLParser.ATRIBUTO) | (1 << SQLParser.COLUNA) | (1 << SQLParser.TABELA))) != 0):
                self.state = 122
                localctx.t = self.matchWildcard()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.trailing_str = (None if localctx.t is None else localctx.t.text)
             
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





