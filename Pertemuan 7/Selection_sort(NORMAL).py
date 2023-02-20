def selectionSort(listData):
    print('Algoritma Selection Sort konvensional')
    print('Data Awal=',listData)
    for outIter in range(len(listData)-1):
        minIndex=outIter
        for i in range(outIter+1,len(listData)):
            if listData[i]<listData[minIndex]:
                minIndex=i
        temp=listData[outIter]
        listData[outIter]=listData[minIndex]
        listData[minIndex]=temp
        # listData[outIter] = listData[minIndex]
        # listData[minIndex] = listData[outIter]
        print('Iterasi ke-',outIter+1,':',listData)
    print('Data Urut=',listData)

a=[5,2,1,3,4]
#a=[10,2,5,8,1,7,12,4]
selectionSort(a)