from hashtable.hashtable import HashTable

def push_tree_nodes_to_hashtable(tree,hashtable):
    """
    push each node in tree to hashtable
    """
    root = tree.root
    def walk(root,hashtable):
        if root is None:
            return
        
        if hashtable.contains(root.value):
            # TODO: Add update to HashTable class
            hashtable.storage[hashtable.hash(root.value)] += 1
        else: 
            hashtable.storage[hashtable.hash(root.value)] = 1

        walk(root.left,hashtable)
        walk(root.right,hashtable)
    walk(root,hashtable)

def tree_intersection(tree_one,tree_two):
    hash = HashTable()
    push_tree_nodes_to_hashtable(tree_one,hash)
    push_tree_nodes_to_hashtable(tree_two,hash)
    #TODO: find way to return all keys with a value greater than 0
