# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    #find distance
    distance = Y - X
    #calculate the minimum number of jumps needed to reach or pass Y
    jumps = (distance + D - 1) // D

    return jumps 
    
