def uniqueList(dataList):
    comparisonList = []
    for element in dataList :
        if element not in comparisonList :
            comparisonList.append(element)
    for element in comparisonList :
        print(f'{element}\n')

uniqueList([2,3,4,5,2,6])
print(' ------- ')
uniqueList([2,3,4,5,8,6, 7, 1, 5, 4])
print(' ------- ')
uniqueList([2,3,4,5,2,6])