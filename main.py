from decision_tree import *

def maximum(decision_node):
    selection = 0
    for posibility in range(len(decision_node.posibilities)):
        if decision_node.posibilities[posibility].next_node.value > decision_node.posibilities[selection].next_node.value:
            selection = posibility
    return selection


def mean(random_node):
    mean = 0
    for posibility in random_node.posibilities:
        mean += posibility.next_node.value*posibility.probability
    return mean

def minimum(random_node):
    minimum = random_node.posibilities[0].next_node.value
    for posibility in random_node.posibilities:
        if posibility.next_node.value < minimum:
            minimum = posibility.next_node.value
    return minimum

def main():
    root = DecisionNode("offer", [
        Posibility("2.5 millions", RandomNode("auction", [
            Posibility("lose", LeafNode(), probability=0.45),
            Posibility("win", probability=0.55, value=-(2.5*0.15), next_node=DecisionNode("terrain use", posibilities=[
                Posibility("600 houses", value=((4000/1000000)*600) -
                           (2.5*0.85), next_node=LeafNode()),
                Posibility("wait", RandomNode("reclassification", [
                    Posibility("reclassified", value=-1, probability=0.6, next_node=DecisionNode("terrain use", [
                        Posibility("1500 apartments", RandomNode("sale", [
                            Posibility("real state company", probability=0.6, value=(
                                (4000/1000000)*1500)-(2.5*0.85), next_node=LeafNode()),
                            Posibility("individual sale", probability=0.4, value=(
                                (3000/1000000)*1500)-(2.5*0.85), next_node=LeafNode())
                        ])),
                        Posibility("medical tower", RandomNode("sale", [
                            Posibility("whole sale", value=4.5-(2.5*0.85),
                                       probability=0.7, next_node=LeafNode()),
                            Posibility("individual sale", value=4-(2.5*0.85),
                                       probability=0.3, next_node=LeafNode())
                        ])),
                        Posibility("mall", RandomNode("sale", [
                            Posibility("stores sale", value=5-(2.5*0.85),
                                       probability=0.24, next_node=LeafNode()),
                            Posibility("insurance sale", value=6-(2.5*0.85),
                                       probability=0.76, next_node=LeafNode())
                        ]))
                    ])),
                    Posibility("not reclassified", probability=0.4, next_node=DecisionNode("terrain use", [
                        Posibility("lose advance", next_node=LeafNode()),
                        Posibility("600 houses", value=(
                            (3800/1000000)*600)-(2.5*0.85), next_node=LeafNode())
                    ]))
                ]))
            ]))
        ])),
        Posibility("3 millions", RandomNode("auction", [
            Posibility("lose", LeafNode(), probability=0.25),
            Posibility("win", probability=0.75, value=-(3*0.15), next_node=DecisionNode("terrain use", posibilities=[
                Posibility("600 houses", value=((4000/1000000)*600) -
                           (3*0.85), next_node=LeafNode()),
                Posibility("wait", RandomNode("reclassification", [
                    Posibility("reclassified", value=-1, probability=0.6, next_node=DecisionNode("terrain use", [
                        Posibility("1500 apartments", RandomNode("sale", [
                            Posibility("real state company", probability=0.6, value=(
                                (4000/1000000)*1500)-(3*0.85), next_node=LeafNode()),
                            Posibility("individual sale", probability=0.4, value=(
                                (3000/1000000)*1500)-(3*0.85), next_node=LeafNode())
                        ])),
                        Posibility("medical tower", RandomNode("sale", [
                            Posibility("whole sale", value=4.5-(3*0.85),
                                       probability=0.7, next_node=LeafNode()),
                            Posibility("individual sale", value=4-(3*0.85),
                                       probability=0.3, next_node=LeafNode())
                        ])),
                        Posibility("mall", RandomNode("sale", [
                            Posibility("stores sale", value=5-(3*0.85),
                                       probability=0.24, next_node=LeafNode()),
                            Posibility("insurance sale", value=6-(3*0.85),
                                       probability=0.76, next_node=LeafNode())
                        ]))
                    ])),
                    Posibility("not reclassified", probability=0.4, next_node=DecisionNode("terrain use", [
                        Posibility("lose advance", next_node=LeafNode()),
                        Posibility("600 houses", value=(
                            (3800/1000000)*600)-(3*0.85), next_node=LeafNode())
                    ]))
                ]))
            ]))
        ]))
    ])

    # print("MaxiMin Tree:")
    # tree = DecisionTree(root, decision_criteria=maximum, probability_compute=minimum)
    # print(tree)

    print("\nHope Tree:")
    tree = DecisionTree(root, decision_criteria=maximum, probability_compute=mean)
    print(tree)


if __name__ == "__main__":
    main()
