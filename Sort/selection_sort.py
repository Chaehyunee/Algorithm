def selection_sort(array):
    for i in range(len(array)):
        min = 9999
        # 매번 가장 작은 수를 구한다
        for j in range(i, 10):
            if min > array[j]:
                min = array[j]
                idx = j
        
        array[i], array[idx] = array[idx], array[i]
    
    print(*array)
    
num = [2, 10, 5, 8, 7, 6, 4, 3, 1, 9]
selection_sort(num)