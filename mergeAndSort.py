# Given you are passed two sorted arrays, merge and sort them in O(n)

def merge_arrays(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1            
    result += a[i:]
    result += b[j:]
    for i in result:
        print i,