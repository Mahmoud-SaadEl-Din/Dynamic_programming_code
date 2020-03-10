import math
  
# Returns the best obtainable price for a rod of length n and 
# price[] as prices of different pieces 
def cutRod(price_list, total_length): 
    Best_value_for_cut = [0 for x in range(total_length+1)] 
    Best_value_for_cut[0] = 0
  
    # Build the table val[] in bottom up manner and return 
    # the last entry from the table 
    for length in range(1, total_length+1): 
        max_val = price_list[length-1] 
        for shorter_length in range(1,length+1):
            try_cut_at = shorter_length
            remaining_piece_after_cut = length - try_cut_at  
            max_val = max(max_val, Best_value_for_cut[try_cut_at] + Best_value_for_cut[remaining_piece_after_cut]) 
        Best_value_for_cut[length] = max_val 

    print(Best_value_for_cut)
    return Best_value_for_cut[total_length]

arr = [1, 5, 8, 9, 10, 17, 17, 20] 
size = len(arr) 
print("Maximum Obtainable Value is " + str(cutRod(arr, size))) 



