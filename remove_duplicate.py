nums=[0,0,1,1,1,2,2,3,3,4]
teste=[]
class Solution:
  
      def removeDuplicates(nums):
          
          a=-1254115421
      
          for i in range(len(nums)):
              
              
      
              for j in range(len(nums)):
                if a==nums[i]:
                  continue 
                
                elif j==0:
                  k=0 
                    
      
                elif (nums[i] == nums[j]) and i != j and k==0:

                  k+=1
                  a=nums[i]
                  teste.append(nums[i])
                  continue
      
      
                elif (j+1 == len(nums)) and k==0  :
      
                  teste.append(nums[i])

          
              
      
                else:
                     continue
              
          nums=teste

          return len(teste),nums
      

k = Solution.removeDuplicates(nums)

print(k)

            
    