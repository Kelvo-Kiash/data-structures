def search_recursively(key, node):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return search_recursively(key, node.left)
    else:
        return search_recursively(key, node.right)



#iterative
def search_iteratively(key, node):
    current_node = node
    while current_node is not None:
        if key == current_node.key:
            return current_node
        elif key < current_node.key:
            current_node = current_node.left
        else:
            current_node = current_node.right
    return current_node
