"""
Find Middle Number
Given a number (n) and an array of numbers (num_list) as input to a function, 
    -return True if the number is greater than the middle number of the array. 
    -Return False if the number is less than the middle number of the array.

Example Input: n = 6, array = [3,5,8, 10]
Example Output: True

Example Input: n = 105, array = [10,30,44,22,100]
Example Output: True
"""
def find_middle(a, num_list):

    middle_num = len(num_list) // 2
    indx_eve = len(num_list) % 2
    
    #even len list
    if indx_eve == 0:
        print("List len is even")
        print(f"Middle index - 1 is: {num_list[middle_num - 1]}")
        if a > num_list[middle_num - 1]:
            return True
        else:
            return False
    
    #odd list
    else:
        print("List len is odd")
        print(f"Middle index is: {num_list[middle_num]}")
        if a > num_list[indx_eve]:
            return True
        else:
            return False

print(find_middle(21, [10,30,44,22,100,102, 155]))        
# print(find_middle(105, [10,30,44,22,100]))
# print(find_middle(6, [3,5,8,10]))


#---------Matt's Answer-------------
# def middle_number(n,arr):
#     if len(arr) % 2 == 0:      
#         return True if n > arr[(len(arr) // 2)-1] else False
#     else:
#         return True if n > arr[(len(arr) // 2)] else False