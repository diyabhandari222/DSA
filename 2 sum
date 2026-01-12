def two_sum(arr):
    target=10
    for i in range(len(arr)):
        for j in range(1,len(arr)):
           # if i==j:
                #continue
            if arr[i]+arr[j]==target:
                 return i,j#arr[i],arr[j]
        
arr=[2,4,5,6,7]   
print(two_sum(arr))     
#better approach
def two_sum(arr):
    target = 10
    hashmap = {}  # stores value -> index

    for i in range(len(arr)):
        comp = target - arr[i]
        if comp in hashmap:
            return hashmap[comp], i
        hashmap[arr[i]] = i
arr=[1,2,3,4,5,6,7]
print(two_sum(arr))
#optimal solution
def two_sum(arr,target):
    
    arr.sort()
    left=0
    right=len(arr)-1
    while left<right:
        total=arr[left]+arr[right]
        if total==target:
            return "yes"
        elif total<target:
            left +=1
        else:
            right -=1
    return "no" 
arr=[1,2,3,4,5,6,7]
target=10
print(two_sum(arr, target )) 
#for index

      
