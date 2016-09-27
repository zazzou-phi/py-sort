def countsort(items, k):
    L = [0] * (k+1)
    for j in range(len(items)):
        L[items[j]] += 1
    output = []
    for i in range(k):
        output.extend([i] * L[i])
    return output   
