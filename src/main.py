import numpy as np

class main:
    
    
   def func(self):
       
       new_arr = np.array(input("Enter your numbers separated by commas: ").split(','), dtype=int)
       arr = np.array([])
       
       for spot in new_arr:
           
           if(spot < 0 or spot > 100):
               print("Invalid number, please enter a number between 0 and 100.")
               return
           else:
              arr = np.append(arr, spot)
              print(arr)
              
    
    
calculation = main()

result = calculation.func()
print(result)


    