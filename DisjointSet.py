from itertools import groupby


class DisjointSet:
    parents = {}
    depths = {}
    sizes = {}

    def __str__(self):
        return str([set(g) for _, g in groupby(self.parents, self.find)])

    def add(self, n):
        if n not in self.parents:
            self.parents[n] = n
            self.depths[n] = 0
            self.sizes[n] = 1

    def find(self, n):
        while self.parents[n] != n:
            n, self.parents[n] = self.parents[n], self.parents[self.parents[n]]

        return n

    def union(self, a, b):
        ra = self.find(a)
        da = self.depths[ra]
        rb = self.find(b)
        db = self.depths[rb]

        if ra != rb:
            if da <= db:
                da, db = db, da
                ra, rb = rb, ra

            self.parents[rb] = ra
            if da == db:
                self.depths[ra] = db + 1

            self.sizes[ra] += self.sizes[rb]

    def getset(self, n):
        return set(m for m in self.parents if self.parents[m] == self.parents[n])
