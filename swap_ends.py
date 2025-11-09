def swap_ends(L, k):
    if not L or k <= 0 or k > len(L)//2:
        return (L.copy(),0)
    new_list=L.copy()
    n=len(new_list)
    if n%2==0:
        new_list[:k],new_list[-k:]=new_list[-k:],new_list[:k]
    else:
        new_list[:k],new_list[-k:]=new_list[-k:],new_list[:k]
    return (new_list,k)