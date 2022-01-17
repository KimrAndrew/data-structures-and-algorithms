from hashtable.hashtable import HashTable

def left_join(left:HashTable,right:HashTable):
    values = left.get_values()
    for value in values:
        if right.contains(value[0]):
            value.append(right.get(value[0]).value)
        else:
            value.append(None)
    return values