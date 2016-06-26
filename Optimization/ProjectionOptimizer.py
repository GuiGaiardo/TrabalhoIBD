from SQL_Parser.QueryTree import *

#Classe usada para otimização da projeção
class ProjectionOptimizer:

    #Construtor, passa a raiz da árvore a ser otimizada
    def __init__(self, tree):
        self.root = tree.root

    #Função a ser chamada cara fazer a otimização
    def optimize(self):
        self._optimize(self.root, [])
        return self.root

    #Função que efetivamente realiza a ordenação (in-place)
    #Percorre a árvore de cima para baixo acumulando as colunas referenciadas (dependências de cada nível) até chegar nas folhas
    #(Colunas). Então cria um projeção com todos os atributos conhecidos daquela tabela e retorna uma
    #Projeção e uma lista de tabelas conhecidas até o momento. No retorno da recursão, compara as tabelas conhecidas
    #com as dependências e remove as que são desnecessárias

    def _optimize(self, node, dependencies_so_far):
        if isinstance(node, ProjectionNode):
            self._optimize(node.children, list(set(dependencies_so_far + node.columns)))


        elif isinstance(node, ThetaJoinNode):
            term = node.terms[0]
            columns = []
            if len(term) == 1:
                new_projection0, current_columns0 = self._optimize(node.children[0], dependencies_so_far)
                new_projection1, current_columns1 = self._optimize(node.children[1], dependencies_so_far)

            else:
                for t in node.terms:
                    print(t)
                    columns += [t[0], t[2]]
                new_projection0, current_columns0 = self._optimize(node.children[0], list(set(dependencies_so_far + columns)))
                new_projection1, current_columns1 = self._optimize(node.children[1], list(set(dependencies_so_far + columns)))

            if new_projection0 is not None:
                node.children[0] = new_projection0
            if new_projection1 is not None:
                node.children[1] = new_projection1

            current_columns = current_columns0 + current_columns1
            new_columns_to_select = [x for x in current_columns if x in dependencies_so_far]

            # Se possui mais tabelas do que precisa nas dependências, Projeta, senão retorna
            if len(new_columns_to_select) < len(current_columns) and len(new_columns_to_select) > 0:
                temp = ProjectionNode(new_columns_to_select)
                temp.set_child(node)
                return temp, new_columns_to_select

            else:
                return None, new_columns_to_select

        elif isinstance(node, SelectionNode):
            new_projection, current_columns = self._optimize(node.children, list(set(dependencies_so_far + [x[0] for x in node.terms])))
            if new_projection is not None:
                node.children = new_projection
            newColumnsToSelect = [x for x in current_columns if x in dependencies_so_far]

            # Se possui mais tabelas do que precisa nas dependências, Projeta, senão retorna
            if len(newColumnsToSelect) < len(current_columns) and len(newColumnsToSelect) > 0:
                temp = ProjectionNode(newColumnsToSelect)
                temp.set_child(node)
                return temp, newColumnsToSelect

            else:
                return None, newColumnsToSelect

        elif isinstance(node, Table):
            temp = None

            if len([x for x in dependencies_so_far if x.split('.')[0] == node.name]) > 0:
                #Projeta todas as colunas conhecidas na tabela
                temp = ProjectionNode([x for x in dependencies_so_far if x.split('.')[0] == node.name])
                temp.set_child(node)

            return temp, [x for x in dependencies_so_far if x.split('.')[0] == node.name]
        else:
            print("?")