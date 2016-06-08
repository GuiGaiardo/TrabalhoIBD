grammar SQL;


sql_expr locals [
        lista = []
        ]: SELECT {print ($SELECT.text)
$lista += [1]
print($lista)}  clausulaSelect
        | FROM
        ;

clausulaSelect : COLUNA  c1=clausulaSelect {print($clausulaSelect.text)}| ;


WS: [ \n\t\r]+ -> channel(HIDDEN);

SELECT : 'SELECT';
FROM   : 'FROM';
WHERE  : 'WHERE';


COLUNA : ('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9')*'.'('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9')*;
TABELA : ('a'..'z' |'A'..'Z' )('a'..'z' |'A'..'Z' | '0' .. '9')*;

