import graph
import networkx as nx
import matplotlib.pyplot as plt



def main():
    with open('test.txt') as f:
        n, m = map(int, f.readline().split())
        arcs = []
        for k in xrange(m):
            i, j, weight = map(int, f.readline().split())
            l = [i,j,weight]
            # print l
            arcs.append(l)


    g1 = graph.Graph(arcs,n)
    # g1.makeNotOrientation()
    # print g1.IJ
    g1.draw()


if __name__ == '__main__':
    main()
