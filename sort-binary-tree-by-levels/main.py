# https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python

def tree_by_levels(root):
    arr = []

    if root is None:
        return arr

    queue = []
    queue.append(root)

    while len(queue) > 0:
        arr.append(queue[0].value)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return arr
