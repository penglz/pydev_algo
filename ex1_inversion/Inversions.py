def merge_and_count(iA, iB, nInv):
    result = []
    i = 0
    j = 0
    while i < len(iA) and j < len(iB):
        if (iA[i] < iB[j]):
            result.append(iA[i])
            i+=1
        else:
            result.append(iB[j])
            j+=1
            nInv = nInv + len(iA) - i
    while i < len(iA):
        result.append(iA[i])
        i+=1
    while j < len(iB):
        result.append(iB[j])
        j+=1
        
    return (result, nInv)
            
def sort_and_count(iArray, nInv):
    result = []
    if len(iArray) == 1:
        return (iArray, nInv)
    if len(iArray) == 2:
        if (iArray[0] < iArray[1]):
            return (iArray, nInv)
        else:
            result.append(iArray[1])
            result.append(iArray[0])
            nInv += 1
            return (result, nInv)
    pivot = len(iArray)/2

    left,nInv = sort_and_count(iArray[0:pivot], nInv)
    right,nInv = sort_and_count(iArray[pivot:len(iArray)], nInv)
    result,nInv = merge_and_count(left, right, nInv)
    return (result, nInv)
    

with open('./IntegerArray.txt', 'r') as f:
    myarray = [int(line) for line in f]
#myarray = [1,3,4,2,8,5,6,7]
nInv = 0
myarray, nInv = sort_and_count(myarray, nInv)
print nInv
    
    
