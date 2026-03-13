def getUnionOfTwoSets(set1, set2):
    result = set()
    for elementA in set1 :
        result.add(elementA)
    for elementA in set2:
        result.add(elementA)        
    return result


# Tests:
# Should_ReturnUnion_WhenBothSetsAreProvided
# Should_ReturnSetA_WhenSetBIsEmptyOrNull
# Should_ReturnSetB_WhenSetAIsEmptyOrNull
# Should_ReturnNull_WhenBothSetsAreEmptyOrNull

#Set A = {1,2,3,4,5,6}
#Set B = {2,3,4,5,6,7,8}
A = {1,2,3,4,5,6}
B = {2,3,4,5,6,7,8}
print(getUnionOfTwoSets(A, B))