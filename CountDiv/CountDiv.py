def solution(A, B, K):
    #find the number of multiples up to B
    last = B // K

    #find the number of multiples before A
    first = (A-1) // K

    #calculate the number of multiples in the range
    count = last - first

    #return the total count
    return count