grammar Algebra;

algebra_expr:	projecao
    |	selecao
    |	algebra_expr '|X|' condJuncaoTheta algebra_expr
    |	'(' algebra_expr ')'
    |   tabela
    |   ID
    ;




/***************/
t_s: coluna comparison_op coluna;
condSelecao:  t_s
           | t_s boolean_op condSelecao;
selecao: 'S' condSelecao '('algebra_expr')';
/***************/

condProjecao: coluna
            | coluna ',' condProjecao;
projecao: 'P' condProjecao '('algebra_expr')';

/***************/
//
t_theta: coluna '=' coluna;
condJuncaoTheta: t_theta
                |t_theta 'and' condJuncaoTheta;
//juncao_theta:

/************/
tabela: ID;
coluna: tabela'.'ID;

boolean_op: BOOLEAN_OP;
comparison_op: COMPARISON_OP;

ID : ('a'..'z' |'A'..'Z' )+;
NEWLINE : [\r\n]+ ;

COMPARISON_OP:  '<'|'>'| '=';
BOOLEAN_OP:  'and'|'or';

