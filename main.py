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

    # G = nx.DiGraph()
    # G.add_weighted_edges_from(g1.getList())
    # nx.draw_networkx(G)
    # plt.show()


    G1 = nx.Graph()
    test = g1.kraskala()

    G1.add_weighted_edges_from(test)
    nx.draw_networkx(G1)
    plt.show()

if __name__ == '__main__':
    main()
