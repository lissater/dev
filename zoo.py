# class Donkey:
#     def __init__(self, age, has_tail):
#         self.age = age(int)
#         self.has_tail = has_tail(bool)

#     def make_sound(self):
#         if self.has_tail is False:
#             print("ia-ia-ia")
#         else:
#             print("The tail is still here")   
# #

class Giraffe:
    def __init__(self, age, neck_length):
        self.age = age
        self.neck_length = neck_length
      
        self.age = int(age)
        self.neck_length = int(neck_length)
        age == 0

#         if neck_length == "is short":
#             self.age <  1
#             if neck_length == "is medium":  
#                 self.age =  2
#             else:
#                 self.age >  2
        
#     def make_sound(self):
#         if self.age <= 1:
#             print("me-me-meeee")
#         if self.age == 2:
#             print("me-re-reeee")
#         else:
#             print("murrrr")    
        


grff1 = Giraffe(5, 10)
grff2 = Giraffe(2, 13)
grff3 = Giraffe(1, 3)      

giraffes = [grff1, grff2, grff3]



longest_neck_giraffe = giraffes[0]  # Assume the first giraffe has the longest neck initially

for giraffe in giraffes:
    if giraffe.neck_length > longest_neck_giraffe.neck_length:
        longest_neck_giraffe = giraffe

# Print information about the giraffe with the longest neck
print(f"The giraffe with the longest neck has age {longest_neck_giraffe.age} and neck length {longest_neck_giraffe.neck_length}.")





# # Find the giraffe with the longest neck
# longest_neck_giraffe = max(giraffes, key=lambda x: x.neck_length)

# # Print information about the giraffe with the longest neck
# print(f"The giraffe with the longest neck has age {longest_neck_giraffe.age} and neck length {longest_neck_giraffe.neck_length}.")

    # print("If neck " + grff.neck_length + " says: ")
    # grff.make_sound()

    #print(giraffes)


# class Penguin:
#     def __init__(self, age, is_cold):
#         self.age = age(int)
#         self.neck_length = is_cold(int)  





















