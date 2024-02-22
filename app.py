from typing import List


def BusquedaBinariaIterativa(nums: List[int], target : int)-> bool:
    
    #pointers leeft and right
    left, right = 0, len(nums) - 1
    
    #iterative process
    while left <= right:
        # find mid point
        mid= left +(right-left)//2
        
        if nums[mid] == target:
            return True
        
       # target number is right side
        elif nums[mid] > target:
            right=mid -1
            
        # target number is left side
        else: 
            left = mid + 1
            
    #target number doesn't exists will return False
    return False
            
    #pass

if __name__ == "__main__":
    
    nums= [1, 2, 3, 4, 5, 6, 7]
    target = 2
    
    result = BusquedaBinariaIterativa(nums=nums,  target=target)
    
    print(result)