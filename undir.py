def euler(adj):
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
