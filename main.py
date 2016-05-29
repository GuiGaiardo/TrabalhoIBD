import query_parser

parse = query_parser.parse
query = input("digite a consulta: ")
match = parse(query)
print(match)
