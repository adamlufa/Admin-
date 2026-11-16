# Construct an expression tree from a prefix expression,
# perform non-recursive post-order traversal, and delete the tree.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_operator(char):
    return char in "+-*/"


def construct_expression_tree(prefix):
    stack = []

    # Process prefix expression from right to left.
    for char in reversed(prefix.replace(" ", "")):
        node = Node(char)
        if is_operator(char):
            if len(stack) < 2:
                raise ValueError("Invalid prefix expression")
            node.left = stack.pop()
            node.right = stack.pop()
        stack.append(node)

    if len(stack) != 1:
        raise ValueError("Invalid prefix expression")
    return stack[0]


def postorder_non_recursive(root):
    if root is None:
        return []

    stack = []
    result = []
    last_visited = None
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek = stack[-1]
            if peek.right is not None and last_visited is not peek.right:
                current = peek.right
            else:
                result.append(peek.value)
                last_visited = stack.pop()

    return result


def delete_tree(root):
    if root is None:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
        node.left = None
        node.right = None


def main():
    prefix = input("Enter prefix expression (example: +--a*bc/def): ")
    try:
        root = construct_expression_tree(prefix)
        print("Post-order traversal (non-recursive):",
              " ".join(postorder_non_recursive(root)))
        delete_tree(root)
        print("Tree deleted.")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
