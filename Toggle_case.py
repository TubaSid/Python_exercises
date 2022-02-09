def toggle_case(s):
    l=len(s)
    sc=''
    for i,n in enumerate(s):
        if i%2==0:
            swap=(n).lower()
        else:
            swap=(n).upper()
        sc=sc+swap
    return sc

if __name__ == '__main__':
