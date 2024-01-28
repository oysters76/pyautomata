Q = {'A', 'B', 'C', 'D', 'E', 'F'};     # all states
q0 = 'A';                               # start state
E = {'0', '1'};                         # state inputs
F = {'C', 'D', 'E'};                    # all final states
D = {                                   # transition function 
    'A0':'B',
    'A1':'C',
    'B0':'A',
    'B1':'D',
    'C0':'E',
    'C1':'F',
    'D0':'E',
    'D1':'F',
    'E0':'E',
    'E1':'F',
    'F0':'F',
    'F1':'F',
};

MARK = 1 
UNMARK = 0

def gen_table(Q):
    table = {} 
    for q1 in Q:
        for q2 in Q:
            key = q1 + q2
            keyi = q2 + q1
            if q1 != q2 and key not in table.keys() and keyi not in table.keys():
                table[key] = UNMARK
    return table

def mark(table, F):
    for key in table.keys():
        q1, q2 = key[0], key[1]
        if q1 in F and q2 not in F:
            table[key] = MARK 
        elif q1 not in F and q2 in F:
            table[key] = MARK
    return table

def check(table, D, E, F):
    changes = 0
    for key in table.keys(): 
        if table[key] == MARK:
            continue
        q1, q2 = key[0], key[1]
        changed_key = ""
        for a in E:
            t1 = q1 + a 
            t2 = q2 + a 
            q3 = D[t1] + D[t2] 
            q3i = D[t2] + D[t1] 

            if q3 in table.keys():
                if table[q3] == MARK:
                    changed_key = q3 
            if q3i in table.keys():
                if table[q3i] == MARK:
                    changed_key = q3i 

            if changed_key != "":
                changes += 1
                table[key] = MARK
                break 
    return table, changes

def filter_unmarked(table):
    filtered = [] 
    for key in table.keys():
        if table[key] == UNMARK:
            filtered.append(key) 
    return filtered

def remove_duplicates(all_sets):
    l = []
    for s in all_sets:
        if s not in l:
            l.append(s) 
    return l
    

def combine(unmarked):
    all_sets = [] 
    for i, unmark in enumerate(unmarked):
        q1, q2 = unmark[0], unmark[1] 
        r = [q1, q2] 
        for j, key in enumerate(unmarked):
            if i == j:
                continue 
            q3, q4 = key[0], key[1]
            if q1 == q3 or q1 == q4 or q2 == q3 or q2 == q4:
                r.append(q3) 
                r.append(q4)
        all_sets.append(set(r)) 
    return remove_duplicates(all_sets)

def remain(unmarked, Q):
    l = [] 
    for q in Q:
        is_uniq = True
        for s in unmarked:
            if q in s:
                is_uniq = False 
                break
        if is_uniq:
            l.append(q)
    return set(l)



def gen_new_D(unmarked, remained, D, E):
    newD = {} 
    for unmark in unmarked:
        for e in E:
            new_key = "".join(unmark) + e 
            mapped = ""
            for k in unmark:
                ck = k + e 
                m_q = D[ck]
                for other in unmarked:
                    if m_q in other:
                        mapped = "".join(other)
                        break
                if mapped == "":
                    for rem in remained:
                        if m_q in rem:
                            mapped = "".join(rem) 
                            break 
                break
            newD[new_key] = mapped 

    for rem in remained:
        for e in E:
            new_key = "".join(rem) + e
            m_k = D[new_key]
            mapped = ""
            for other in unmarked:
                if m_k in other:
                    mapped = "".join(other) 
                    break 
            if mapped == "":
                for other in remained:
                    if m_k in other:
                        mapped = "".join(other) 
                        break 
            newD[new_key] = mapped 
    return newD

def min(Q, q0, E, F, D):
    table = gen_table(Q) 
    table = mark(table, F)
    changes = 1 
    while changes > 0:
        table, changes = check(table, D, E, F)
    unmarked = combine(filter_unmarked(table))
    remained = remain(unmarked, Q)
    newD = gen_new_D(unmarked, remained, D, E)
    return newD

print("Before min: ", D)
print("After min: ", min(Q, q0, E, F, D))

