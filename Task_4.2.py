import random


def get_number_tickets(min, max, quantity):
     
      if min < 1 or max >= 1000:
            print("Invalid number, try again.")
            return []
      
      if quantity > (max - min + 1) or quantity > 1000:
          print("Invalid number, try again.")
          return []
      combination = random.sample(range(min, max + 1), quantity)
      combination.sort()
      return combination
result = get_number_tickets(9,18,7)

print("The winning combination is:", result)


