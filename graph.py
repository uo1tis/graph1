class Graph:
    # def __init__(self, I, J, n):
    #     self.I = I
    #     self.J = J
    #     self.m = len(I)
    #     self.n = n

    def __init__(self, arcs, n):
        self.n = n
        self.m = len(arcs)
        self.I = []
        self.J = []
        self.arcs = arcs
        for i in xrange(self.m):
            self.I.append(self.arcs[i][0])
            self.J.append(self.arcs[i][1])
        self.create()

    # def addList(self, I, J):
    #     self.I = I
    #     self.J = J

    def addArc(self, x, y, weight):
        self.m += 1
        self.I.append(x)
        self.J.append(y)
        self.arcs.append([x, y, weight])
        h = self.H[x]
        self.H[x] = self.m - 1
        self.L.append(h)

    def deleteArc(self, v, x):
        if self.H[v] == x:
            h = int(self.H[v])
            self.H[v] = self.L[self.H[v]]
            self.L[h] = -1
        else:
            i = self.H[v]
            while i != -1:
                if self.L[i] == x:
                    h = self.L[i]
                    self.L[i] = self.L[self.L[i]]
                    self.L[h] = -1
                i = self.L[i]

    def create(self):
        self.H = [-1] * self.n
        self.L = [0] * self.m
        for k in xrange(self.m):
            i = int(self.I[k])
            self.L[k] = self.H[i]
            self.H[i] = k

    def getList(self):
        list = []
        for i in xrange(self.m):
            list.append((self.I[i], self.J[i], self.arcs[i][2]))
        return list

    def copy(self):
        return Graph(self.arcs, self.n)

    def kraskala(self):
        gr = self.copy()
        gr.arcs.sort(key=lambda x: x[2])
        sel = [i for i in xrange(self.n)]
        ans = []
        for i, j, w in gr.arcs:
            if (sel[i] != sel[j]):
                a = sel[i]
                b = sel[j]
                ans.append([i, j, w])
                for k in xrange(self.n):
                    if (sel[k] == b):
                        sel[k] = a
        return ans

    def bfs(self):
        pass

    def dfs(self):
        pass

    def dekstr(self):
        pass
