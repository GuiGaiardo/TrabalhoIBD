grammar Expr;		
prog:	(expr NEWLINE)* ;
expr:	expr high_prec_ops expr
    |	expr low_prec_ops expr
    |	INT
    |	'(' expr ')'
    ;
high_prec_ops : HIGH_PREC_OPS;
low_prec_ops : LOW_PREC_OPS;
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
HIGH_PREC_OPS  : '*'|'/';
LOW_PREC_OPS   : '+'|'-';