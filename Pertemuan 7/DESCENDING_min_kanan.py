#DATA TERKECIL DI TARUH DI INDEKS TERAKHIR

def selectionSort(Data):
    print('Data Awal=',Data)
    langkah = 0
    for i in range (len(Data)-1, 0, -1):
        print("Langkah ke-",langkah)
        m = 0
        for j in range(1, i+1):
            #print("IKIIIII", Data[j] , Data[m])
            if Data[j] < Data[m]:
                m = j
        temp = Data[i]
        Data[i] = Data[m]
        Data[m] = temp

        langkah += 1
        print(Data)


#a=[5,2,1,3,4]
a=[2,10,8,1,7,6,4]
selectionSort(a)