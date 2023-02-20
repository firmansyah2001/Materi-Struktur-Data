#DATA TERKECIL DI TARUH DI INDEKS AWAL

def selectionSort(Data):
    print('Data Awal=',Data)
    for i in range (len(Data)):
        min_idx = i
        for j in range(i+1, len(Data)):
            if Data[j] < Data[min_idx]:
                min_idx = j
        Data[i],Data[min_idx]=Data[min_idx],Data[i]
        print("MIN : ",Data)



a=[5,2,1,3,4]
#a=[2,10,8,1,7,6,4]
selectionSort(a)