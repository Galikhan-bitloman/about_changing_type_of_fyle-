a = [6,7,4,2,8,9,0,3,1,5]

def sort(a):
    N = len(a)
    for i in range(1, N):
        while i > 0 and a[i-1]>a[i]:
            a[i], a[i-1] = a[i-1], a[i]
            i-=1
            print(a)
sort(a)