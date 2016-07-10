import math
import queue


class Tree(object):
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.data = data
        self.right = right

    def depth(self, t):
        if t is None:
            return 0
        return 1 + max(self.depth(t.left), self.depth(t.right))

    def depthbal(self, t):
        if t is None:
            return True
        return abs(self.depth(t.left) - self.depth(t.right)) <= 1 and (self.depthbal(t.left) and self.depthbal(t.right))

    def slope(self, t):
        if t is None:
            return 0
        return self.depth(t.left) - self.depth(t.right)

    def rebal(self, t):
        if self.slope(t) == 2:
            return self.shiftr(t)
        elif self.slope(t) == -2:
            return self.shiftl(t)
        else:
            return t

    def shiftr(self, t):
        if self.slope(t.left) == -1:
            return self.rotr(Tree(t.data, self.rotl(t.left), t.right))
        else:
            return self.rotr(t)

    def shiftl(self, t):
        if self.slope(t.right) == 1:
            return self.rotl(Tree(t.data, t.left, self.rotr(t.right)))
        else:
            return self.rotl(t)

    def rotr(self, t):
        return Tree(t.left.data, t.left.left, Tree(t.data, t.left.right, t.right))

    def rotl(self, t):
        return Tree(t.right.data, Tree(t.data, t.left, t.right.left), t.right.right)

    def binsert(self, e, t):
        if t is None or t.data is None:
            return Tree(e, None, None)
        elif e < t.data:
            return self.rebal(Tree(t.data, self.binsert(e, t.left), t.right))
        elif e == t.data:
            return t
        else:
            return self.rebal(Tree(t.data, t.left, self.binsert(e, t.right)))

    def depthN(self, n, t):
        if n == 0 or t is None:
            return []
        elif n == 1 and t is not None:
            return [t.data]
        else:
            return self.depthN(n-1, t.left) + self.depthN(n-1, t.right)

    def level_by_level(self, t):
        if t is not None:
            n = self.depth(t)
            for i in range(1, n+1):
                print(i, " -> ", self.depthN(i, t))

    def delete(self, e, t):
        if t is None:
            return None
        elif e < t.data:
            return Tree(t.data, self.delete(e, t.left), t.right)
        elif e == t.data:
            return self.join(t.left, t.right)
        else:
            return Tree(t.data, t.left, self.delete(e, t.right))

    def join(self, t1, t2):
        if t1 is None:
            return t2
        else:
            p = self.split(t1.data, t1.left, t1.right)
            return Tree(p[0], p[1], t2)

    def split(self, e, t1, t2):
        if t2 is None:
            return e, t1
        else:
            p = self.split(t2.data, t2.left, t2.right)
            return p[0], Tree(e, t1, p[1])

    def leaves(self, t):
        if t is not None:
            if t.left is None and t.right is None:
                return [t.data]
            elif t.left is None and t.right is not None:
                return self.leaves(t.right)
            elif t.left is not None and t.right is None:
                return self.leaves(t.left)
            else:
                return self.leaves(t.left) + self.leaves(t.right)

    def insert(self, e, t):
        if t is None or t.data is None:
            return Tree(e, None, None)
        elif e <= t.data:
            return Tree(t.data, self.insert(e, t.left), t.right)
        else:
            return Tree(t.data, t.left, self.insert(e, t.right))

    def in_order(self, t):
        if t is not None:
            self.in_order(t.left)
            print(str(t.data) + " ", end="")
            self.in_order(t.right)

    def reverse_order(self, t):
        if t is not None:
            self.reverse_order(t.right)
            print(str(t.data) + " ", end="")
            self.reverse_order(t.left)

    @staticmethod
    def bfs(t):
        que = queue.Queue()
        que.enqueue(t)
        while not que.is_empty():
            child = list()
            v = que.dequeue()
            print(str(v.data) + " ", end="")
            child.append(v.left)
            child.append(v.right)
            for i in [0, 1]:
                if child[i] is not None:
                    que.enqueue(child[i])

    @staticmethod
    def dfs(t):
        if t is not None:
            print(str(t.data) + " ", end="")
            children = list()
            children.append(t.left)
            children.append(t.right)
            for child in children:
                Tree.dfs(child)

    def post_order(self, t):
        if t is not None:
            self.post_order(t.left)
            self.post_order(t.right)
            print(str(t.data) + " ", end="")

    def pre_order(self, t):
        if t is not None:
            print(str(t.data) + " ", end="")
            self.pre_order(t.left)
            self.pre_order(t.right)
            

def main():
    print()
    t = Tree()
    for n in range(1, 16):
        t = t.binsert(n, t)

    t.level_by_level(t)

    print(t.depthbal(t))
    print(t.slope(t))
    print("\nbreath first search")
    Tree.bfs(t)
    print("\ndepth first search")
    Tree.dfs(t)


y = [3, 2, 6, 4, 1, 10, 12, 7, 9, 5]
aTree = Tree()
for x in y:
    aTree = aTree.insert(x, aTree)

aTree.level_by_level(aTree)
print("-- after --")

aTree = aTree.delete(9, aTree)
if aTree is not None:
    aTree.level_by_level(aTree)
'''
print(aTree.depthbal(aTree))
print(aTree.slope(aTree))
print("\n\nbreath first search")
Tree.bfs(aTree)

print("\nin_order")
aTree.in_order(aTree)
print()
print("leaves are " + str(aTree.leaves(aTree)))

print("depth = " + str(aTree.depth(aTree)))

print("reverse order")
aTree.reverse_order(aTree)

print("\n\npost order")
aTree.post_order(aTree)

print("\n\npre order")
aTree.pre_order(aTree)
print("\n\n---- Below ----")
'''
main()


