

# O(n)
def findPeak(arr):
    for i in range(len(arr)):arr
        if i == 0:
            if arr[i] > arr[i+1]:
                return arr[i]
        elif i > 0:
            if arr[i-1] =< arr[i] >= arr[i+1]:
                return arr[i]
        else:
            pass


#O(lgn) for one dimensional array
def findPeak_lgn(arr):
    if arr[len(arr)/2] < arr[(len(arr)/2) - 1]:
        return findPeak_lgn(arr[:(len(arr)/2)-1])]
    elif arr[len(arr)/2] < arr[(len(arr)/2) + 1]:
        return findPeak_lgn(arr[(len(arr)/2)-1]):]
    else:
        return arr[(len(arr)/2)]


#O(lgn) for two dimensional array




    