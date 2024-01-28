
import graphviz

# f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
# f.attr(rankdir='LR', size='8,5')

# f.attr('node', shape='doublecircle')
# f.node('LR_0')
# f.node('LR_3')
# f.node('LR_4')
# f.node('LR_8')

# f.attr('node', shape='circle')
# f.edge('LR_0', 'LR_2', label='SS(B)')
# f.edge('LR_0', 'LR_1', label='SS(S)')
# f.edge('LR_1', 'LR_3', label='S($end)')
# f.edge('LR_2', 'LR_6', label='SS(b)')
# f.edge('LR_2', 'LR_5', label='SS(a)')
# f.edge('LR_2', 'LR_4', label='S(A)')
# f.edge('LR_5', 'LR_7', label='S(b)')
# f.edge('LR_5', 'LR_5', label='S(a)')
# f.edge('LR_6', 'LR_6', label='S(b)')
# f.edge('LR_6', 'LR_5', label='S(a)')
# f.edge('LR_7', 'LR_8', label='S(b)')
# f.edge('LR_7', 'LR_5', label='S(a)')
# f.edge('LR_8', 'LR_6', label='S(b)')
# f.edge('LR_8', 'LR_5', label='S(a)')

# f.view()

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


