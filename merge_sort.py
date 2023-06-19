# copy merge sort algo and add len() function to algorithm
# for string lenght sort , short to longest

def merge_sort(items):

    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1

    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2

    return items

def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0

    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            if len(items[i_1]) < len(items[i_2]): # lenght of items added
                temporary_storage[i_t] = items[i_2] #items[i_1] change to i_2
                i_2 += 1 #change i_1 to i_2 
            else: # the_list[i_2] >= items[i_1]
                temporary_storage[i_t] = items[i_1] # i_2 change to i_1
                i_1 += 1 # i_2 change to i_1
            i_t += 1

        elif i_1 < end_1:
            for i in range(i_1, end_1):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
                i_t += 1

        else: # i_2 < end_2
            for i in range(i_2, end_2):
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
                i_t += 1

    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]     


# List 1

l1 = ['Make', 'my', 'day', 'please', 'or', 'when', 'it', 'suits', 'you', 'perfectly', 'man']

print('\nList 1:\n', l1)

sorted_l1 = merge_sort(l1)

print('\nSorted List 1 to string Length:\n', sorted_l1)



# List 2
l2 = ['33', '766363', 'Merry', 'please', 'or', 'Christmas', 'Volume', 'weight', '1', '12', '33333333']

print('\nList 2:\n', l2)

sorted_l2 = merge_sort(l2)

print('\nSorted List 2 to string Length:\n', sorted_l2)


# List 3

l3 = ['@@@@@@@@', '766363&E#@H&%#@^', 'one', '1', 'colour', 'Binary', 'five', 'new year', '', '__', 'matrix']

print('\nList 3:\n', l3)

sorted_l3 = merge_sort(l3)

print('\nSorted List 3 to string Length:\n', sorted_l3)