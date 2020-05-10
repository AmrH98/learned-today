def partition_last(arr, low,high):  #84317
    pivot = arr[high]               #164123(1) 160361(0)
    i = low - 1
    global num
    # num = 0
    # temp = 0
    for j in range(low,high):
        num+=1
        if arr[j] < pivot:
            i+=1

            arr[i],arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high], arr[i+1]

    # print(arr)
    # arr[i],arr[high] = arr[high], arr[i]


    # temp = arr[high-1]
    # arr[high-1] = arr[i+1]
    # arr[i+1] = temp
    # print(arr)
    return (i+1)

def partition_first(arr,low,high):
    pivot = arr[low]
    i = low - 1
    # num = 0
    # temp = 0
    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            # num+=1
            arr[i],arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high], arr[i+1]
    return (i+1)

def partition_med(arr,low,high):
    index = int(findmed(arr))
    pivot = arr[index]
    # # i = low - 1
    # s = 0
    # f = 0
    # for j in range(low,high):
    #     if arr[j] < pivot:
    #         s+=1
    #         # num+=1
    #         arr[index-s]= arr[j]
    #     elif arr[j] > pivot:
    #         f+=1
    #         arr[index+f] = arr[j]
    i = low - 1
    # num = 0
    # temp = 0
    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            # num+=1
            arr[i],arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high], arr[i+1]

    return i+1

def findmed(arr):
    H = len(arr)
    if (H % 2) == 0:
        mid = H / 2
        # print(int(mid))
    else:
        mid = float(H/2)
        # print(int(mid))
    return mid

def quicksort(arr,low,high):
    if low<high:
        p = partition_last(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)
#
# arr = [10, 80, 30, 90, 40, 50, 70]
# high = len(arr)
# num = 0
#
# # partition_med(arr,low,high)
# # partition_last(arr,low,high)
# quicksort(arr,0,high-1)
# -------------------------
with open('/Users/amr/Downloads/Coursera/Stanford/Machine Learning/Week 3/_32387ba40b36359a38625cbb397eee65_QuickSort.txt','r') as f:
    temp = [int(x) for x in f]
high = len(temp)
num = 0
quicksort(temp,0,high-1)
print(num)
print('Sorted array is ',temp)