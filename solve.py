def threeConsecutiveOdds(arr):
    '''
    Input: arr = [1,2,34,3,4,5,7,23,12]
    1 is odd, 2 is not odd, 34 is not odd, 
    '''
    parity = 0
    for i in arr:
        if i % 2 != 0:
            parity += 1
            if parity == 3:
                return True
        else:
            parity = 0
            
    return False
        
            

def main():
    print(threeConsecutiveOdds(arr = [1,2,34,3,4,5,7,23,12]))
    print(threeConsecutiveOdds(arr = [2,6,4,1]))
main()