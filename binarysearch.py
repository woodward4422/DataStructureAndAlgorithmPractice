def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper: 
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            print(x)
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x


binary_search([1,5,8,10], 8)           


    

