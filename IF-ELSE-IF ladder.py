#Given a variable D (distance) write a program to print the cost associated with it as shown  :
#Assign a value to double variable cost depending on the value of integer variable distance as follows
 #     Distance                                         cost
 #-------------------------------------         ----------------
 #0 through 100                                         5.00
 #More than 100 but not more than 500                   8.00
 #more than 500 but less than 1,000                    10.00
 #1,000 or more                                        12.00
def print_cost(distance):
  if ("distance>=0 && distance<=100"):
    print(5.00)
  elif ("distance>=100 && distance<=500"):
    print(8.00)
  elif ("distance>=500 && distance<=100"):
    print(10.00)
  else:
    print(12.00)
