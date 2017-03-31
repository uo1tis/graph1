import Queue

import networkx as nx
import matplotlib.pyplot as plt


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
        self.graph_orientation = 0
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

    def bfs(self, v):
        used = [False for i in xrange(self.n)]
        q = Queue()
        if (used[v]):
            return
        q.put(v)
        used[v] = True
        ans = []
        while (not q.empty()):
            v = q.get()
            ans.append(v+1)
            for w in self.findV(v):
                if (used[w]):
                    continue
                q.put(w)
                used[w] = True
        return ans
    def findV(self, v):
        h = []
        h.append(int(self.H[v]))
        i = 0
        while (self.L[h[i]] != -1):
            h.append(self.L[h[i]])
            i+=1
        ans = []
        for i in h:
            ans.append(int(self.J[i]))
        return ans

    def dfs(self):
        pass

    def dekstr(self):
        pass
    def color(self):
        pass
    def draw(self):
        if(self.graph_orientation):
            g = nx.Graph()
            g.add_weighted_edges_from(self.arcs)
            nx.draw_networkx(g)
            plt.show()
        else:
            g = nx.DiGraph()
            g.add_weighted_edges_from(self.arcs)
            nx.draw_networkx(g)
            plt.show()

    def makeNotOrientation(self):
        self.graph_orientation = 1
        self.IJ = []
        for i in xrange(self.m):
            self.IJ.append(self.I[i])
        for i in xrange(self.m, self.m *2):
            self.IJ.append(self.J[i-self.m])