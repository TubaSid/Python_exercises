def swap_case(s):
    l=len(s)
    sc=''
    for i,n in enumerate(s):
        if n.isupper():
            swap=(n).lower()
        else:
            swap=(n).upper()
        sc=sc+swap
    return sc

if __name__ == '__main__':
