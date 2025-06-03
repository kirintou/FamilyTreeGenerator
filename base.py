import networkx as nx
from graphviz import Digraph
from IPython.display import Image
import os
title="base"
os.makedirs(os.path.dirname(os.path.realpath(__file__))+"\\png", exist_ok=True)
downloadfolfer=os.path.dirname(os.path.realpath(__file__))+"\\png\\"

def generategraph(Child,Spouse,graphtitle):
    C=nx.DiGraph(Child)
    GViz = Digraph(comment='The Directed Graph-Tree')
    GViz.attr('node', shape='box', fontname='MS Gothic',charset="UTF-8",rank = 'diff') # ←★ここのfontnameで日本語対応フォントを設定★
    
    for n in Spouse:
        with GViz.subgraph() as s:
            for nn in n:
                s.node(nn)
            s.attr(rank="same")
            s.edge(n[0], n[1] ,arrowhead = 'none', color = "red:invis:red")
    
    for n in C.nodes():
        GViz.node(n)
    for e in C.edges():
        GViz.edge(e[0], e[1])
    

    GViz.render(graphtitle,downloadfolfer, format='png', cleanup=True)
    Image(downloadfolfer+graphtitle+'.png')




Child = {
    '祖母': ['父'],
    '母': ['息子'],

}

Spouse = {
    ('祖母', '祖父'),
    ('父', '母'),
}


generategraph(Child,Spouse,title)
