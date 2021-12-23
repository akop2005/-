'''
n=int(input())
mx=0
mx2=0
mx13=0
mx26=0
for i in range(n):
    x=int(input())
    if x%26!=0 and x>=mx26:
        mx=mx26
        mx26=x
    elif x%26!=0 and x>mx:
        mx=x
        
    elif x%13==0 and x%2!=0:
        mx13=max(mx13,x)
    elif x%2==0 and x%13!=0:
        mx2=max(mx2,x)
l=int(input())
#print(mx26,mx,mx2,mx13)
k=max(mx26*mx,mx26*mx2,mx26*mx13)
if k!=0:
    print('Вычисленное контрольное значение:',end=' ')
    print(k)
if k==l:
    print('Контроль пройден.')
else:
    print('Контроль не пройден.')
'''


'''
n=int(input())
razn=10**8
summ=0
for i in range(n):
    try:
       x,y=map(int,input().split())
    except Exception:
       x,y=map(int,input().split())
    summ+=max(x,y)
    k=abs(x-y)
    if k!=0 and k%4!=0:
        razn=min(razn,k)
if summ%4==0:
    if razn!=10**8:
        summ-=razn
        print(summ)
    else:
        print(0)
else:
    print(summ)
    '''

'''
s=input()
st=''
new=''
mas=[0]*10
p=0
kol=0
w=''
mid=''
j=True
for k in s:
    if k.isdigit()==True:
        kol+=1
        w=k
        mas[int(k)]+=1
if kol!=1:
    for i in range(1,10):
        if mas[i]!=0:
            if mas[i]%2==1:
                mid=str(i)
                p+=1
                if p>1:
                    j=False
                    break
                new+=str(i)*(mas[i]//2)
            else:
                new+=str(i)*(mas[i]//2)
    if mas[0]!=0:
        if (mas[0]%2==1 and p+1<=1):
            mid='0'
            new=new[:1]+'0'*(mas[0]//2)+new[1:]
        elif mas[0]%2==0:
            new=new[:1]+'0'*(mas[0]//2)+new[1:]

    if new!='' and j!=False and new.count('0')!=len(new):
        print("YES")
        print(new+mid+new[::-1])
    else:
        print('NO')
else:
    print('YES')
    print(w)
'''

'''
n=int(input())
mx=0
mx2=0
mx3=0
mx6=0
for i in range(n):
    x=int(input())
    if x%6==0:
        mx6+=1
    elif x%2==0 and x%3!=0:
        mx2+=1
    elif x%3==0 and x%2!=0:
        mx3+=1
    else:
        mx+=1
print(mx*mx6+mx2*mx3+mx2*mx6+mx3*mx6+mx6*(mx6-1)//2)
'''


'''
n=int(input())
mx=0
mx2=0
mx3=0
mx6=0
for i in range(n):
    x=int(input())
    if x%6==0:
        mx6+=1
    elif x%2==0 and x%3!=0:
        mx2+=1
    elif x%3==0 and x%2!=0:
        mx3+=1
    else:
        mx+=1
print(mx2*mx+mx3*mx+mx*(mx-1)//2+mx2*(mx2-1)//2+mx3*(mx3-1)//2)

'''

'''
n = int(input())
l1 = []
o = 0
for i in range(2):
    l1.append(int(input()))
l = [0]*12
for i in range(n-2):
    a = int(input())
    o+=l[(12-a%12)%12]
    b = l1.pop(0)
    l[b%12]+=1
    l1.append(a)
print(o)
'''

'''
n=int(input())
kol=0
mas=[0]*12
summ=0
for i in range(n):
    x=int(input())
    mas[x%12]+=1
for i in range(1,6):
    summ+=mas[i]*mas[12-i]
summ+=mas[6]*(mas[6]-1)//2+mas[0]*(mas[0]-1)//2
print(summ)

'''


'''
n = int(input())
l1 = []
o = 0
for i in range(2):
    l1.append(int(input()))
k2 = 0
k3 = 0
k6 = 0
k = 0
for i in range(n-2):
    a = int(input())
    if a%6==0:
        o+=k+k2+k3+k6
    elif a%2==0:
        o+=k3+k6
    elif a%3==0:
        o+=k2+k6
    else:
        o+=k6
    b = l1.pop(0)
    if b%6==0:
        k6+=1
    elif b%2==0:
        k2+=1
    elif b%3==0:
        k3+=1
    else:
        k+=1
    l1.append(a)
print(o)
'''
'''
from itertools import permutations
n = int(input())
l = [0]*12
s = 0
for i in range(n):
    a = int(input())
    l[a%12]+=1
k = []
for i in range(12): 
    for j in range(12):
        for z in range(12):
            if (i+j+z)%12==0 and [i, j,z] not in k:
                for f in permutations([i, j, z], 3):
                    k.append(list(f))
                if i!=j!=z:
                    s+=l[i]*l[j]*l[z]
                elif i==j!=z:
                    s+=(l[i]*(l[i]-1)//2)*l[z]
                elif i==z!=j:
                    s+=(l[i]*(l[i]-1)//2)*l[j]
                elif j==z!=i:
                    s+=(l[z]*(l[z]-1)//2)*l[i]
                elif i==j==z:
                    s+=(l[i]*(l[i]-1)*(l[i]-2))//6
print(s)
'''
'''
n = int(input())
a = [0]*80
b = [0]*80
s = 0
for i in range(n):
    p = int(input())
    if p>50:
        if p%80==0:
            s += a[0]
        else:
            s += a[80-p%80]
    else:
        s += b[80-p%80]
    if p>50:
        b[p%80]+= 1
        a[p%80]+=1
    else:
        a[p%80]+=1
print(s)
'''

'''
n = int(input())
ch13=0
nch13=0
ch=0
nch=0
for i in range(n):
    x=input()
    if x!='':
        x=int(x)
    else:
        x=1
    if x%13==0:
        if x%2==0:
            ch13+=1
        else:
            nch13+=1
    else:
        if x%2==0:
            ch+=1
        else:
            nch+=1
print(ch13*(ch13-1)//2+ch13*ch+nch13*nch+nch13*(nch13-1)//2)
    
'''
'''
n = int(input())
ch13=0
nch13=0
ch=0
nch=0
s=0
mas=[]
for i in range(4):
    mas.append(int(input()))
for i in range(n-4):
    try:
        x=int(input())
    except Exception:
        x=int(input())
    if x%13==0:
        if x%2==0:
            s+=ch13+ch
        else:
            s+=nch13+nch
    else:
        if x%2==0:
            s+=ch13
        else:
            s+=nch13
    b=mas.pop(0)
    if b%13==0:
        if b%2==0:
            ch13+=1
        else:
            nch13+=1
    else:
        if b%2==0:
            ch+=1
        else:
            nch+=1
    mas.append(x)
print(s)
'''

'''
k2 = 0
k13 = 0
k26 = 0
k = 0 
s = 0
n = int(input())
l1 = [int(input()) for i in range(5)]
for i in range(5):
    a = l1[i]
    if a%26==0:
        k26+=1
    elif a%13==0:
        k13+=1
    elif a%2==0:
        k2+=1
    else:
        k+=1
s+=(k13*k+k13*(k13-1)//2+k26*k2+k26*(k26-1)//2)
for i in range(n-5):
    try:
        a = int(input())
    except Exception:
        a = int(input())
    b = l1.pop(0)
    if b%26==0:
        k26-=1
    elif b%13==0:
        k13-=1
    elif b%2==0:
        k2-=1
    else:
        k-=1
    if a%26==0:
        s+=k2+k26
        k26+=1
    elif a%13==0:
        s+=k+k13
        k13+=1
    elif a%2==0:
        s+=k26
        k2+=1
    else:
        s+=k13
        k+=1
    l1.append(a)
print(s)
'''

'''
n = int(input())
ch5=0
nch5=0
ch=0
nch=0
for i in range(n):
    x=int(input())
    if x%5==0:
        if x%2==0:
            ch5=max(ch5,x)
        else:
            nch5=max(nch5,x)
    else:
        if x%2==0:
            ch=max(ch,x)
        else:
            nch=max(nch,x)
print(max(nch5*ch5,nch5*ch,ch5*nch))
        '''

'''
from itertools import permutations
l = [[0]*7 for i in range(2)]
for i in range(int(input())):
    a = int(input())
    l[a%2][a%7]+=1
l1, s = [], 0
for i in range(7):
    for j in range(7):
        for z in range(7):
            if (i+j+z)%7==0 and [i, j, z] not in l1:
                l1.extend([list(k) for k in permutations([i, j, z])])
                if i!=j!=z:
                    s+=l[0][i]*l[0][j]*l[1][z]
                    s+=l[0][i]*l[1][j]*l[0][z]
                    s+=l[1][i]*l[0][j]*l[0][z]
                    s+=l[1][i]*l[1][j]*l[1][z]
                elif i==j!=z:
                    s+=(l[0][i]*(l[0][i]-1)//2)*l[1][z]
                    s+=(l[1][i]*(l[1][i]-1)//2)*l[1][z]
                    s+=(l[0][i]*(l[1][i]))*l[0][z]
                elif i==z!=j:
                    s+=(l[0][i]*(l[0][i]-1)//2)*l[1][j]
                    s+=(l[1][i]*(l[1][i]-1)//2)*l[1][j]
                    s+=(l[0][i]*(l[1][i]))*l[0][j]
                elif z==j!=i:
                    s+=(l[0][z]*(l[0][z]-1)//2)*l[1][i]
                    s+=(l[1][z]*(l[1][z]-1)//2)*l[1][i]
                    s+=(l[0][z]*(l[1][z]))*l[0][i]
                elif z==i==j:
                    s+=(l[0][i]*(l[0][i]-1)//2)*l[1][i]
                    s+=l[1][i]*(l[1][i]-1)*(l[1][i]-2)//6
print(s)
'''


