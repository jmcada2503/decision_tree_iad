from termcolor import colored


class DecisionTree():
    root = None
    _decision_criteria = None
    _probability_compute = None

    def __init__(self, root, decision_criteria, probability_compute):
        self.root = root
        self._decision_criteria = decision_criteria
        self._probability_compute = probability_compute
        self._computeLeafsValues(self.root, 0)
        self._computeNodeValue(self.root)

    def _computeNodeValue(self, node):
        if node.value is not None:
            return

        for posibility in node.posibilities:
            self._computeNodeValue(posibility.next_node)
        if isinstance(node, RandomNode):
            node.value = self._probability_compute(node)
        elif isinstance(node, DecisionNode):
            node.decision = self._decision_criteria(node)
            node.value = node.posibilities[node.decision].next_node.value

    def _computeLeafsValues(self, node, value):
        if isinstance(node, LeafNode):
            node.value = value
        else:
            for posibility in node.posibilities:
                self._computeLeafsValues(
                    posibility.next_node, value+posibility.value)

    def _recursivePrint(self, node, level, decision=False, best_way=False):
        if isinstance(node, LeafNode):
            return ("\t"*level)+colored(str(round(node.value, 3)), "white" if not decision else "green")+"\n"
        else:
            if isinstance(node, DecisionNode):
                actual_string = ("\t"*level)+colored(node.name, "blue")+colored(f" ({round(node.value, 3)})", "blue" if not decision else "green")+"\n"
            elif isinstance(node, RandomNode):
                actual_string = ("\t"*level)+colored(node.name, "red")+colored(f" ({round(node.value, 3)})", "red" if not decision else "green")+"\n"

            for posibility in node.posibilities:
                if isinstance(node, DecisionNode):
                    actual_string += self._recursivePrint(
                        posibility.next_node,
                        level+1,
                        posibility is node.posibilities[node.decision] and best_way,
                        posibility is node.posibilities[node.decision] and best_way
                        )
                else:
                    actual_string += self._recursivePrint(
                        posibility.next_node,
                        level+1,
                        False,
                        best_way
                        )

            return actual_string

    def __str__(self):
        return self._recursivePrint(self.root, 0, best_way=True)


class Posibility():
    name = ""
    next_node = None
    value = None
    probability = None

    def __init__(self, name, next_node, value=0, probability=None):
        self.name = name
        self.next_node = next_node
        self.value = value
        self.probability = probability


class LeafNode():
    value = None


class DecisionNode():
    name = ""
    value = None
    decision = None
    posibilities = []

    def __init__(self, name, posibilities):
        self.name = name
        self.posibilities = posibilities


class RandomNode():
    name = ""
    value = None
    posibilities = []

    def __init__(self, name, posibilities):
        self.name = name
        self.posibilities = posibilities
