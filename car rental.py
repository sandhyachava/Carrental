from datetime import datetime,timedelta

class carrental:
    def __init__(self,available_car_list):
        self.available_car_list=available_car_list
        self.rented_car_list ={}
       
           
    def available_cars(self):
        print("\ncars_available_for rent\n")
        for car,quantity in self.available_car_list.items():        
            print(f"{car} : {quantity}")
           
   #create methods to rent cars hourly ,Daily, weekly  
  
   #Keeping the methods as-is though we ahev code repetition  in rent_car_* methods
   #Ideally define new method to combine code below and just call the method for different rental_mode
   
    def rent_cars_hourly(self,car,car_quantity,rental_mode,rental_time,v_hourly):
        if car_quantity >0 and car_quantity <= self.available_car_list[car]:
            self.available_car_list[car] =  self.available_car_list[car] - car_quantity
            self.rented_car_list[car]=(car_quantity,rental_mode,rental_time,v_hourly)
            print(f'Requested {car_quantity} {car} cars rented successfully for {rental_mode}')
            return True
        else:
            print("Requested car type or quattity is not available at this time")   
                
    def rent_cars_daily(self,car,car_quantity,rental_mode,rental_time,v_daily):
        if car_quantity >0 and car_quantity <= self.available_car_list[car]:
            self.available_car_list[car] =  self.available_car_list[car] -car_quantity
            self.rented_car_list[car]=(car_quantity,rental_mode,rental_time,v_daily)
            print(f'Requested {car_quantity} {car} cars rented successfully for {rental_mode}')
        else:
            print("Requested car type or quantity is not available at this time")    
            
    def rent_cars_weekly(self,car,car_quantity,rental_mode,rental_time,v_weekly):
        if car_quantity >0 and car_quantity <= self.available_car_list[car]:
            self.available_car_list[car] =  self.available_car_list[car] -car_quantity 
            #self.rented_car_list[car]={car_quantity,rental_mode,rental_time,v_weekly}
            self.rented_car_list[car]=(car_quantity,rental_mode,rental_time,v_weekly)
            print(f'\nRequested {car_quantity} {car} cars rented successfully for {rental_mode}')
        else:
            print("Requested car type or quantity is not available at this time")
    
  # create method for return car
    def return_car(self,car):
        if car in self.rented_car_list:
            car_quantity,rental_mode,rental_time,price = self.rented_car_list.pop(car)

            rental_end_time = datetime.now()
            rental_duration = rental_end_time-rental_time
           
            if rental_mode == "hourly":
                bill = (rental_duration.seconds/3600) * price * car_quantity
            elif rental_mode == "daily":  
                bill = rental_duration.days * price * car_quantity
            elif rental_mode == "weekly":
                 bill = (rental_duration.days//7) * price * car_quantity
                   
            self.available_car_list[car] =  self.available_car_list[car] +car_quantity
            print(f"Please pay the amount {bill}")
            print(f"\nThanks for returning {car_quantity} {car} cars")
        else:
            print('please try returning the car again')from datetime import datetime,timedelta


