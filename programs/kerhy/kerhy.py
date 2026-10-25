p1=list(map(int,input().split()))
p2=list(map(int,input().split()))
p3=list(map(int,input().split()))

stůl=[]
arr=[]
arr2=[]
max=0
p33=[]
p22=[]
p11=[]

if len(p1)!=len(p2) and len(p2)!=len(p3):
    print("error")
else: 

    a=len(p1)

    for i in range(a):
        arr=[p1[i],p2[i],p3[i]]
        for k in range(len(arr)):
            print(k)
            if arr[k]>max:
                max=arr[k]

        print(max)
        b=arr.count(max)

        if b > 1:
            stůl += [p1[i],p2[i],p3[i]]
            continue
        else:

            stůl=stůl+[p1[i],p2[i],p3[i]]
            if p1[i]>p2[i] and p1[i]>p3[i]:
                p11=p11+stůl
            elif p2[i]>p1[i] and p2[i]>p3[i]:
                p22=p22+stůl
            elif p3[i]>p1[i] and p3[i]>p2[i]:
                p33=p33+stůl

            stůl=[]

    print((len(p11)),(len(p22)),(len(p33)))
    print(p11,p22,p33)
    print(stůl)