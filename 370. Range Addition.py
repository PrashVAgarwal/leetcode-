# RANGE CACHING
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        #we will use RANGE CACHING here
        #so we just add the value to the start element of the array
        #we do this as after going through all the operations, we will do prefix sum over the entire array so the values will be cumulatively added to the following elements
        
        #One thing we need to take care of is that a value should not be added beyond the end element. 
            #For this we subtract the value from the end+1 element to stop the value's propagation beyond its end element.
            
            arr=[0]*length
            
            for start,end,val in updates:
                arr[start]+=val
                if end+1<length:
                    arr[end+1]-=val
                    
            for i in range(1,length):
                arr[i]+=arr[i-1]
                
            return arr
