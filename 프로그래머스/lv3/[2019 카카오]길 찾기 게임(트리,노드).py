import sys

sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, key, x):
        self.key = key
        self.x = x
        self.right, self.left = None, None


class Tree:
    def __init__(self, head, x):
        self.head = Node(head, x)

    def insert(self, key, x):
        cur_node = self.head
        while True:
            if cur_node.x > x:  # left down
                if cur_node.left == None:
                    cur_node.left = Node(key, x)
                    break
                else:
                    cur_node = cur_node.left
            elif cur_node.x < x:  # right down
                if cur_node.right == None:
                    cur_node.right = Node(key, x)
                    break
                else:
                    cur_node = cur_node.right

    def preorder(self):
        res = []

        def order(node):
            nonlocal res
            res.append(node.key)
            if node.left != None:
                order(node.left)
            if node.right != None:
                order(node.right)

        order(self.head)
        return res

    def postorder(self):
        res = []

        def order(node):
            nonlocal res
            if node.left != None:
                order(node.left)
            if node.right != None:
                order(node.right)
            res.append(node.key)

        order(self.head)
        return res


def solution(nodeinfo):
    answer = []
    for i in range(len(nodeinfo)):
        nodeinfo[i] = [i + 1] + nodeinfo[i]
    # print(nodeinfo)
    nodeinfo.sort(key=lambda x: (x[2]), reverse=True)
    tree = Tree(nodeinfo[0][0], nodeinfo[0][1])
    for i in nodeinfo[1:]:
        tree.insert(i[0], i[1])
    answer.append(tree.preorder())
    answer.append(tree.postorder())
    return answer
