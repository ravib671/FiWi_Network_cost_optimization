def MaximizeUserDPA(values,weights,capacity):
    n = len(values)
    tab = [[0]*(capacity + 1) for y in range(n + 1)]
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                include_item = values[i-1] + tab[i-1][w-weights[i-1]]
                exclude_item = tab[i-1][w]
                tab[i][w] = max(include_item, exclude_item)
            else:
                tab[i][w] = tab[i-1][w]
    
    # for row in tab:
    #       print(row)
    i = n 
    j = capacity
    selected_onu = []
    while i > 0:
        if tab[i][j] > tab[i-1][j]:
            selected_onu.append(i-1)
            j = j - weights[i-1]
        i = i -1

    return tab[n][capacity], selected_onu

