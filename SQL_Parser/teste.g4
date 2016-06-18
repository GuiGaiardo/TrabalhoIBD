grammar teste;

algebra_expr: selecao
    | '(' algebra_expr ')'
    | projecao
    | tabela
    //| algebra_expr '|X|' condJuncaoTheta algebra_expr
    ;

tabela: ID;
coluna: tabela'.'ID;


/*************************/
condProjecao: coluna
            | coluna ',' condProjecao;

projecao: 'P' condProjecao '('algebra_expr')';
/*************************/

/***************/
t_s: coluna comparison_op coluna;
condSelecao: t_s boolean_op condSelecao
           | t_s;
selecao: 'S' condSelecao '('algebra_expr')';
/***************/


//
t_theta: coluna EQUAL coluna;
condJuncaoTheta: t_theta
                |t_theta AND condJuncaoTheta;
//juncao_theta: juncao_theta_temp;
//juncao_theta_temp: algebra_expr '|X|' condJuncaoTheta algebra_expr;


comparison_op: COMPARISON_OP;
boolean_op : BOOLEAN_OP;




NEWLINE : [\r\n]+ ;

COMPARISON_OP:  '<'|'>'| EQUAL;
EQUAL: '=';




BOOLEAN_OP:  AND|'or';
AND: 'and';
ID : ('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9')*;


WS: [ \n\t\r]+ -> skip;
//Space
//  :  (' ' | '\t' | '\n' | 'r')+ {pass}
//  ;
