''' 
Given 4 numbers: A, B, C, D
Generate latest time possible, and if not possible return "NOT POSSIBLE"
'''

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, C, D):
    # first: need one either 012
    # second: 0123456789
    # third: 012345
    # fourth: 0123456789
    if A < 0 or B < 0 or C < 0 or D < 0 or A > 9 or B > 9 or C > 9 or D > 9:
        return "NOT POSSIBLE"
    nums = [A, B, C, D]
    hour1_copy = []
    hour2_copy =[]
    min1_copy =[]
    min2_copy =[]
    times = []
    
    for num in nums:
        if num >= 0 and num <= 2:
            hour1_copy.append(num)
        if num >= 0 and num <= 9:
            hour2_copy.append(num)
        if num >= 0 and num <= 5:
            min1_copy.append(num)
        if num >=0 and num <= 9:
            min2_copy.append(num)

    while len(hour1_copy) > 0:
        h1 = max(hour1_copy)
        hour1 = hour1_copy
        hour2 = hour2_copy
        min1 = min1_copy
        min2 = min2_copy
        if h1 in hour2:
            hour2.remove(h1)
        if h1 in min1:
            min1.remove(h1)
        if h1 in min2:
            min2.remove(h1)
        if h1 == 2:
            for num in hour2:
                if num > 3:
                    hour2.remove(num)
                
        if checkSize(hour1, hour2, min1, min2):
            while len(hour2) > 0:
                h2 = max(hour2)
                if h2 in min1:
                    min1.remove(h2)
                if h2 in min2:
                    min2.remove(h2)
                if checkSize(hour1, hour2, min1, min2):
                    while len(min1) > 0:
                        m1 = max(min1_copy)
                        if m1 in min2:
                            min2.remove(m1)
                        if checkSize(hour1, hour2, min1, min2):
                             while len(min2) > 0: 
                                m2 = max(min2)
                                return "" + str(h1) + str(h2) + ":" + str(m1) + str(m2)
                        else:
                            min1.remove(m1)
                else:
                    hour2.remove(h2)
        else:
            hour1_copy.remove(h1)
    return "NOT POSSIBLE"
            
def checkSize(arr1, arr2, arr3, arr4):
    return len(arr1)>0 and len(arr2)>0 and len(arr3)>0 and len(arr4) > 0
    
        
    
    
    