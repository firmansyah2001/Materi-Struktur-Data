#DATA TERBESAR DI TARUH DI INDEKS AWAL

def selectionSort(Data):
    print('Data Awal=',Data)
    for i in range (len(Data)):
        max_idx = i
        for j in range(i+1, len(Data)):
            if Data[max_idx] < Data[j]:
                max_idx = j
        Data[i],Data[max_idx]=Data[max_idx],Data[i]
        print("MAX : ",Data)



a=[5,2,1,3,4]
#a=[2,10,8,1,7,6,4]
selectionSort(a)