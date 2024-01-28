
import graphviz

def sort(l):
    if len(l) == 1: 
        return l 
    return "".join(sorted(list(l)))


def draw(title, fname, Q, E, F, D):
    fname = fname + '.gv'
    f = graphviz.Digraph(title, filename=fname) 
    
    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='doublecircle')
    for fstate in F:
        f.node(sort(fstate))

    f.attr('node', shape='circle')
    for q in Q:
        for e in E:
            key = q + e 
            q2 = D[key]

            f.edge(sort(q), sort(q2), label=e)
    
    f.view()


