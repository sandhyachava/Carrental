#cutomer class customer.ipynb file
class customer:
    def __init__(self,customer_id):
        self.customer_id=customer_id
  
  #create method to rent car for a customer
 
    def rentcar(self):
        car = input("Enter the car you want : ")
        car_quantity = int(input("Please enter the number of cars you want : "))
        return car,car_quantity
   
  #create method to return car
 
    def returncar(self):
        car = input('Enter the car you want to return : ')
        return car
