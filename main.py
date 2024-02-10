#import methods form classrental,customer classes 
from carrental import available_cars,rent_cars_hourly,rent_cars_daily,rent_cars_weekly,return_car
from customer import rentcar,returncar
 
 
 #main method
def main():

    #Create instances of class

    rental_company = carrental({"Honda":10,"Tesla":5,"Mercedes":4})
 
    customer_1 = customer(1)
 
  #Display available options
 
    while True:
            print("\n1.Display available cars")
            print("2.Rent car")
            print("3.Return car")
            print("4.Exit")
        
        # get customer input from available options
            selection= int(input("\nPlease enter the your selection: "))
        
            if selection == 1:
                rental_company.available_cars()
            elif selection == 2:
                car,car_quantity=customer_1.rentcar()
                rental_time = datetime.now()
                v_hourly = 50
                v_daily = 100
                v_weekly = 500

                print("1.Hourly")
                print("2.Daily")
                print("3.Weekly")
            
                rental_selection = int(input("please enter your rental_mode : "))
            
                if rental_selection == 1:
                    rental_company.rent_cars_hourly(car,car_quantity,"hourly",rental_time,v_hourly)
                elif rental_selection == 2:  
                    rental_company.rent_cars_daily(car,car_quantity,"daily",rental_time,v_daily)
                elif rental_selection == 3:  
                    rental_company.rent_cars_weekly(car,car_quantity,"weekly",rental_time,v_weekly)  
                else:
                    print("please enter the right choice")
                    break
            
            elif   selection == 3:   
                car = customer_1.returncar()
                rental_company.return_car(car)
            elif selection == 4:
                break
            else:
                print("Please enter a valid choice")
   
if __name__ == "__main__":
    main()
