def union_and_intersection (array_1, array_2):
    union = list(set(array_1) | set(array_2))
    intersection = [x for x in array_1 if x in array_2]
    return union, intersection

if __name__ == '__main__':
    array_1 = [1,3,5,7,9,11,13]
    array_2 = [2,4,6,8,10,13]
    union, intersection = union_and_intersection (array_1, array_2)
    print('Union :',union)
    print('Intersection :',intersection)