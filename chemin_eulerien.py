def oriente(adj):
    """
    :type adj: list[list[int]]
    """
    n = len(adj)
    nimpair = 0
    entrees = [0]*n
    sorties = [0]*n
    for u in range(n):
        cnt = 0
        for v in adj[u]:
            if v != u:
                cnt += 1
                entrees[v] += 1
        sorties[u] = cnt
    i = -1
    f = -1
    for u in range(n):
        if sorties[u] == entrees[u]+1:
            if i == -1:
                i = u
            else:
                return False
        elif entrees[u] == sorties[u]+1:
            if f == -1:
                f = u
            else:
                return False
        elif entrees[u] != sorties[u]:
            return False
        if (i,f) == (-1,-1): # cycle eulerien (ps: si i vaut -1, f vaut nécessairement -1 et vice-versa)
            i,f = 0,0
    curr = [i]
    chemin = []
    while curr != []:
        u = curr[-1]
        if adj[u] != []:
            v = adj[u].pop()
            curr.append(v)
        else:
            chemin.append(curr.pop())
    chemin.reverse()
    return chemin

def non_oriente(adj):
    """
    :type adj: list[list[int]]
    """
    n = len(adj)
    nimpair = 0
    i = 0
    for u in range(n):
        cnt = 0
        for v in adj[u]:
            if v != u:
                cnt += 1
        if cnt % 2 == 1:
            nimpair += 1
            i = u
            if nimpair > 2:
                return False
    curr = [i]
    chemin = []
    while curr != []:
        u = curr[-1]
        if adj[u] != []:
            v = adj[u].pop()
            adj[v].remove(u)
            curr.append(v)
        else:
            chemin.append(curr.pop())
    chemin.reverse()
    return chemin


adj1 = [[1, 2],
           [3, 3],
           [1, 0],
           [0, 2]]
adj2 = [ [], [0], [3], [1] ]
adj2 = [ [], [0], [3], [1] ]
print(oriente(adj2))

adju = [ [1,2,3],
        [3,3,0,2],
        [1,0,3],
        [1,1,0,2] ]
print(non_oriente(adju))