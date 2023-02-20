#DESCENDING MIN MAX (DATA KECIL KIRI, DATA BESAR KANAN)
def selectionSort(data):
     print('Data Awal=',data)
     nomor = 1
     for i in range (len(data)):
         #UNTUK CARI MIN
        print("Iterasi ke-",nomor)
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i],data[min_idx]=data[min_idx],data[i]
        print("MIN : ",data)
        
        #UNTUK CARI MAX
        for k in range(len(data)-1, 1, -1):
            max_idx = k
            if data[k-1] > data[max_idx]:
                max_idx = k - 1
                break
        data[k],data[max_idx] = data[max_idx],data[k]
        print("MAX : ",data)
        nomor += 1
        if data == sorted(data):
            break
     print("Data telah urut : ",data)

#a=[5,2,1,3,4]
#a=[2,10,8,1,7,6,4]
a = [10,3,9,1,2] #HARUS INI (1)
selectionSort(a)