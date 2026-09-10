class EGraphCongruenceClosure:
    """
    Congruence Closure (Nelson-Oppen / E-Graph).
    Maintains equivalence relations over terms: a == b => f(a) == f(b).
    """
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            return True
        return False

    def merge_congruence(self, f_x, f_y, arg_x, arg_y):
        if self.find(arg_x) == self.find(arg_y):
            self.union(f_x, f_y)
