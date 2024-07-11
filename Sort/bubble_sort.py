def bubble_sort(array):
    for i in range(len(array)): # 맨 뒤에 정렬된 게 i개
        
        # 앞과 뒤를 비교, 더 작은 걸 앞으로
        for j in range(1, len(array)-i): # 앞에서부터 길이-i번째까지 비교, bubble 올리기
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
        
    print(*array)
    
num = [2, 10, 5, 8, 7, 6, 4, 3, 1, 9]
bubble_sort(num)