from trees.trees import KAryTree, KTreeNode

# def test_tree_add():
#     tree = KAryTree(3)
#     tree.add(1)
#     tree.add(2)
#     tree.add(3)
#     tree.add(4)
#     second_level_left = tree.root.connections[0]
#     second_level_mid = tree.root.connections[1]
#     second_level_right = tree.root.connections[2]
#     tree.add(5)
#     tree.add(6)
#     tree.add(7)
#     tree.add(8)
#     # tree.add(9)
#     # tree.add(10)
#     # tree.add(11)
#     # tree.add(12)
#     # tree.add(13)
#     assert tree.root.value == 1
#     assert tree.root.connections[0].value == 2
#     assert tree.root.connections[1].value == 3
#     assert tree.root.connections[2].value == 4
#     assert second_level_left.connections[0].value == 5
#     assert second_level_left.connections[1].value == 6
#     assert second_level_left.connections[2].value == 7
#     assert second_level_mid.connections[0].value == 8
#     # assert second_level_mid.connections[1].value == 9
#     # assert second_level_mid.connections[2].value == 10
#     # assert second_level_right.connections[0].value == 11
#     # assert second_level_right.connections[1].value == 12
#     # assert second_level_right.connections[2].value == 13

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

