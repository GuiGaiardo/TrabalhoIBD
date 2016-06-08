grammar SQL;


sql_expr locals [
        lista = []
        ]: SELECT {print ($SELECT.text);$lista += [1];print($lista)}  clausulaSelect
         FROM  clausulaFrom

        ;

clausulaSelect : COLUNA ',' c1=clausulaSelect {print($clausulaSelect.text)}| COLUNA {print($COLUNA.text)};

conditionsJoin : COLUNA '=' COLUNA 'and' conditionsJoin {print($text)} | COLUNA '=' COLUNA {print($text)};

joins : TABELA JOIN TABELA ON conditionsJoin joins_ ;
joins_: JOIN TABELA ON conditionsJoin
        | ;

clausulaFrom : TABELA ',' clausulaFrom | joins | joins ',' clausulaFrom |TABELA;


WS: [ \n\t\r]+ -> channel(HIDDEN);



SELECT : 'SELECT';
FROM   : 'FROM';
WHERE  : 'WHERE';
JOIN   : 'JOIN';
ON     : 'ON';

COLUNA : ('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9')*'.'('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9')*;
TABELA : ('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9')*;

