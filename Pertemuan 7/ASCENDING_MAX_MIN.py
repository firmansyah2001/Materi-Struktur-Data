#ASECENDING MAX MIN (DATA BESAR KANAN, DATA KECIL KIRI)
def selectionSort(Data):
    print('Data Awal=',Data)
    langkah = 1
    for i in range (len(Data)-1, 0, -1):
        print("Langkah ke-",langkah)
        m = 0
        #CARI MAX
        for j in range(1, i+1):
            if Data[j] > Data[m]:
                m = j
        Data[i],Data[m] = Data[m],Data[i]
        print("MAX : ",Data)
        
        #CARI MIN
        for k in range(0, len(Data)-1, 1):
            min_idx = k
            if Data[k+1] < Data[min_idx]:
                min_idx = k+1
                break
        Data[k],Data[min_idx] = Data[min_idx],Data[k]
        print("MIN : ",Data)
        langkah += 1
        if Data == sorted(Data):
            break
    print("Data telah urut : ",Data)
        
        
#a=[5,2,1,3,4]
#a=[2,10,8,7,4,6,1] #ATAU INI(2)
a = [10,3,9,2,1] #HARUS INI (1)
selectionSort(a)