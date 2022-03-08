temp = {'1':1,'2':2,'3':1}
for k,v in temp.items():
    print(f'Key: {k} , Value: {v}')
pass

s='abcdefga' 
t='bacdaefg'
record = [0] * 26
for i in range(len(s)):
    record[ord(s[i]) - ord("a")] += 1
for i in t:
    record[ord(i) - ord('a')] -= 1
for i in record:
    if i != 0:
        assert False,'Is not same between s and t'
print('True')

pass

def Fib(n): #堆疊練習
    if n<=1:
        return(n)
    else:
        return(Fib(n-1)+Fib(n-2))
        
def Towers(n,A,C,B): # 河內塔
    if n==1:
        print("Move disk",n,"from",A,"to",C)
    else:
        Towers(n-1,A,B,C)
        print("Move disk",n,"from",A,"to",C)
        Towers(n-1,B,C,A)

def bubbleshort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]> nums[j+1]:
                nums[j]=nums[j]+nums[j+1]
                nums[j+1]= nums[j]-nums[j+1]
                nums[j]= nums[j]-nums[j+1]
                #nums[j+1],nums[j] = nums[j],nums[j+1]
    return nums

def sortedSquares(nums:list[int])->list[int]: #雙指針練習
    n= len(nums)
    i,j,k = 0 ,n-1,n-1
    ans = [-1] * n
    while i <= j:
        lm = nums[i] ** 2
        rm = nums[j] ** 2
        if lm > rm:
            ans[k] = lm
            i += 1
        else:
            ans[k] = rm
            j -= 1
        k -= 1
    return ans

sortedSquares([-4,-3,-1,2,3,6,7])
Towers(4,'A','C','B')