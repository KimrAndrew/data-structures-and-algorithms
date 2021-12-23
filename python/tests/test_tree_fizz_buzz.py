from trees.trees import KAryTree, KTreeNode

def test_breadth_first():
    tree = KAryTree(3)
    tree.root = KTreeNode(3,1)
    second_level = [KTreeNode(3,2),KTreeNode(3,3),KTreeNode(3,4)]
    third_level_left = [KTreeNode(3,5),KTreeNode(3,6),KTreeNode(3,7)]
    third_level_mid = [KTreeNode(3,6),KTreeNode(3,7),KTreeNode(3,8)]
    third_level_right = [KTreeNode(3,9),KTreeNode(3,10),KTreeNode(3,11)]
    tree.root.connections = second_level
    tree.root.connections[0].connections = third_level_left
    tree.root.connections[1].connections =  third_level_mid
    tree.root.connections[2].connections = third_level_right
    tree.add(12)
    actual = tree.root.connections[0].connections[0].connections[0].value
    expected = 12
    #print([connection.value for connection in tree.root.connections[0].connections])
    #print(tree.root.connections[0].connections[0].connections[0].value)
    #print(actual)
    assert actual == expected

