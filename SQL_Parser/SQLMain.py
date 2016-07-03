import sys

from SQL_Parser.SQLLexer import SQLLexer
from antlr4 import *
from antlr4.Parser import DefaultErrorStrategy





from SQL_Parser.SQLParser import *
from SQL_Parser.SQLListener import SQLListener
# from SQLLexer import SQLLexer
# from antlr4 import *
# from SQLParser import *
# from SQLListener import SQLListener

errors = []

class ERol(DefaultErrorStrategy):
    def recover(self, recognizer, e):
        query_tree.valid = False
        return super(ERol, self).recover(recognizer, e)

    def recoverInline(self, recognizer):
        query_tree.valid = False
        return super(ERol, self).recoverInline(recognizer)

    def sync(self, recognizer):
        super(ERol, self).sync(recognizer)

    def reportNoViableAlternative(self, recognizer, e):
        tokens = recognizer.getTokenStream()
        if tokens is not None:
            if e.startToken.type == Token.EOF:
                input = "<EOF>"
            else:
                input = tokens.getText((e.startToken, e.offendingToken))
        else:
            input = "<unknown input>"
        msg = "no viable alternative at input " + super(ERol, self).escapeWSAndQuote(input)

        global errors
        errors.append([msg])

        recognizer.notifyErrorListeners(msg, e.offendingToken, e)

    def reportInputMismatch(self, recognizer, e):
        msg = "mismatched input " + super(ERol, self).getTokenErrorDisplay(e.offendingToken) \
              + " expecting " + e.getExpectedTokens().toString(recognizer.literalNames, recognizer.symbolicNames)

        global errors
        errors.append([msg])

        recognizer.notifyErrorListeners(msg, e.offendingToken, e)

    def reportFailedPredicate(self, recognizer, e):
        ruleName = recognizer.ruleNames[recognizer._ctx.getRuleIndex()]
        msg = "rule " + ruleName + " " + e.message

        global errors
        errors.append([msg])

        recognizer.notifyErrorListeners(msg, e.offendingToken, e)

    def reportUnwantedToken(self, recognizer):
        if super(ERol, self).inErrorRecoveryMode(recognizer):
            return

        super(ERol, self).beginErrorCondition(recognizer)
        t = recognizer.getCurrentToken()
        tokenName = super(ERol, self).getTokenErrorDisplay(t)
        expecting = super(ERol, self).getExpectedTokens(recognizer)
        msg = "extraneous input " + tokenName + " expecting " \
              + expecting.toString(recognizer.literalNames, recognizer.symbolicNames)

        global errors
        errors.append([msg])

        recognizer.notifyErrorListeners(msg, t, None)

    def reportMissingToken(self, recognizer):
        if super(ERol, self).inErrorRecoveryMode(recognizer):
            return
        super(ERol, self).beginErrorCondition(recognizer)
        t = recognizer.getCurrentToken()
        expecting = super(ERol, self).getExpectedTokens(recognizer)
        msg = "missing " + expecting.toString(recognizer.literalNames, recognizer.symbolicNames) + " at " + super(ERol, self).getTokenErrorDisplay(t)

        global errors
        errors.append([msg])

        recognizer.notifyErrorListeners(msg, t, None)

class KeyPrinter(SQLListener):
    # Enter a parse tree produced by SQLParser#sql_expr.
    def enterSql_expr(self, ctx: SQLParser.Sql_exprContext):
        pass

    # Exit a parse tree produced by SQLParser#sql_expr.
    def exitSql_expr(self, ctx: SQLParser.Sql_exprContext):
        pass


def main(input):
    global errors
    errors = []
    with open("tmp", "w") as input_file:
        input_file.write(input)

    query_tree.valid = True
    query_tree.errors = []
    input_file = FileStream("tmp")
    lexer = SQLLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = SQLParser(stream)
    parser._errHandler = ERol()
    tree = parser.sql_expr()
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    if(not query_tree.valid):
        query_tree.set_root(None)

    return query_tree, errors


#
# print("\n\n")
# print(tree.getChildCount())
#
# print("\n\n")

# visitor = MyVisitor()
# visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
