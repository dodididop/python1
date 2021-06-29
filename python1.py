def flatten(myList, newList):
    for element in myList:
        if isinstance(element, list): #check type of elements. list or not.
            flatten(element, newList) #if it is list, then turn back to flatten function.
        else:
            newList.append(element) #otherwise add the element to newList.
    return newList	

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5], []))
#######################################################################
def reverse_nested_list(myList):
    output = []
    for element in myList:
        if isinstance(element, list):
            output.append(reverse_nested_list(element))
        else:
            output.append(element)
    output.reverse()
    return output

example = [[1, 2], [3, 4], [5, 6, 7]]
reversed(example)
