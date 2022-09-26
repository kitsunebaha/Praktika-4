s=list(map(int,input().split()))
r=int(input())
count=0
for i in range (len(s)):
    if r<=s[i]:
        count+=1
print(count+1)
for elem in s:
    if elem > r :
        s.insert(s.index(elem), r)
        break
    else :
        continue
print(s)