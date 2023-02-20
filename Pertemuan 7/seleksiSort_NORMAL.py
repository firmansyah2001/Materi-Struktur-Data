def seleksi_sort(data):
    for i in range (0, len(data)-1):
        min_idx = len(data)-1
        for j in range(len(data)-2, i-1, -1):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i],data[min_idx] = data[min_idx], data[i]
        print(data)
a=[5,2,1,3,4]
seleksi_sort(a)