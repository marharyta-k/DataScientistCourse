class Vehicle:
    
    def __init__(self, vehicle_type, max_speed, mileage):
        self.vehicle_type = str(vehicle_type)
        self.max_speed = float(max_speed)
        self.mileage = int(mileage)
    
    def get_data(self):
        print(f'Vehicle type: {self.vehicle_type}, maximum speed: {self.max_speed}, vehicle mileage: {self.mileage}')

    def rental_payment(self, seating_capacity = 0):
        self.seating_capacity = seating_capacity
        return self.seating_capacity**2
    
    def service_alert(self):
        if self.mileage < 10000:
            print('No Service Required!')
        else:
            n = self.mileage//10000
            print('Service Required! '*n)
    
    def drive(self, driven_miles):
        self.mileage += driven_miles
        return self.mileage
        


class Bus(Vehicle):
    
    def __init__(self, vehicle_type, max_speed, mileage, seating_capacity = 50):
        super(Bus, self).__init__(vehicle_type, max_speed, mileage)
        self.seating_capacity = int(seating_capacity)

    def get_data(self):
        super(Bus, self).get_data()
        print(f'Seating capacity: {self.seating_capacity}')

    def rental_payment(self):
        payment = self.seating_capacity**2
        if self.seating_capacity < 10:
            return payment 
        else:
            return 1.1*payment
    

class Car(Vehicle):

    def __init__(self, vehicle_type, max_speed, mileage, colour = 'White'):
        super(Car, self).__init__(vehicle_type, max_speed, mileage)
        self.colour = str(colour)

    def get_data(self):
        super(Car, self).get_data()
        print(f'Colour: {self.colour}')


