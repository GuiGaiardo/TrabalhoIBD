from SQL_Parser.QueryTree import *


class ProjectionOptimizer:

    def __init__(self, tree):
        self.root = tree.root

    def optimize(self):
        self._optimize(self.root, [])
        return self.root

    def _optimize(self, node, dependencies_so_far):
        if isinstance(node, ProjectionNode):
            self._optimize(node.children, list(set(dependencies_so_far + node.columns)))

        elif isinstance(node, ThetaJoinNode):
            term = node.terms[0]
            print(node.get_description())
            if len(term) == 1:
                new_projection0, current_columns0 = self._optimize(node.children[0], dependencies_so_far)
                new_projection1, current_columns1 = self._optimize(node.children[1], dependencies_so_far)

            else:

                columns = [term[0], term[2]]
                new_projection0, current_columns0 = self._optimize(node.children[0], list(set(dependencies_so_far + columns)))
                new_projection1, current_columns1 = self._optimize(node.children[1], list(set(dependencies_so_far + columns)))

            if new_projection0 is not None:
                node.children[0] = new_projection0
            if new_projection1 is not None:
                node.children[1] = new_projection1

            current_columns = current_columns0 + current_columns1
            new_columns_to_select = [x for x in current_columns if x in dependencies_so_far]


            if len(new_columns_to_select) < len(current_columns) and len(new_columns_to_select) > 0:
                temp = ProjectionNode(new_columns_to_select)
                temp.set_child(node)
                return temp, new_columns_to_select

            else:
                return None, new_columns_to_select

        elif isinstance(node, SelectionNode):
            print("selection " + str([x[0] for x in node.terms]))
            new_projection, current_columns = self._optimize(node.children, list(set(dependencies_so_far + [x[0] for x in node.terms])))
            if new_projection is not None:
                node.children = new_projection
            newColumnsToSelect = [x for x in current_columns if x in dependencies_so_far]

            if len(newColumnsToSelect) < len(current_columns) and len(newColumnsToSelect) > 0:
                temp = ProjectionNode(newColumnsToSelect)
                temp.set_child(node)
                return temp, newColumnsToSelect

            else:
                return None, newColumnsToSelect

        elif isinstance(node, Table):
            temp = None
            if len([x for x in dependencies_so_far if x.split('.')[0] == node.name]) > 0:
                temp = ProjectionNode([x for x in dependencies_so_far if x.split('.')[0] == node.name])
                temp.set_child(node)

            return temp, [x for x in dependencies_so_far if x.split('.')[0] == node.name]
        else:
            print("?")