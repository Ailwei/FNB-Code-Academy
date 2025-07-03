try:
    print(x)
    
    
# except NameError:
#     print("an exceprtion ocuured")
    
except NameError:
    print("variable x is not defined ")
    
# finally:
#     print("The try except is finished")
else:
    print("Everything went wrong!!")
    
    
x = -1
if x < 0:
    raise Exception("sorry , no numbers below zero")