export = {
    "cars":[
          { "brand": "Ford",   "model" : "Focus",  "year": 2020, "fuel type": "petrol",  "consumptions": [ 4.1, 5.2, 4.5, 5.3, 4.7]},
          { "brand": "Ford",   "model" : "Modeo","year": 2020, "fuel type": "diesel",  "consumptions": [ 6.1, 6.2, 5.5, 6.9, 9.1]},
          { "brand": "Opel",   "model" : "Astra",   "year": 2016, "fuel type": "petrol",  "consumptions": [ 5.2, 5.1, 5.5, 4.9, 4.9]},
          { "brand": "VW",     "model" : "Golf",    "year": 2021, "fuel type": "diesel",   "consumptions": [ 4.8, 4.8, 4.9, 5.1, 4.8]},
          { "brand": "Honda","model" : "Civic",   "year": 2018, "fuel type": "petrol",  "consumptions": [ 8.5, 7.3, 6.2, 6.7, 7.5]},
          { "brand": "Fiat",     "model" : "500",     "year": 2022, "fuel type": "petrol",  "consumptions": [ 4.9, 4.7, 4.8, 4.7, 5.1]}
             ],
     "motorbikes" : [
          { "brand": "KTM",        "model" : "Duke",      "year": 2022, "type": "naked",   "consumptions": [ 3.1, 3.2, 3.5, 3.3, 2.7]},
          { "brand": "BMW",      "model" : "F1200GS", "year": 2020, "type": "enduro", "consumptions": [ 4.1, 5.2, 4.5, 4.3, 5.2]},
          { "brand": "Kawasaki","model" : "Z400",       "year": 2019, "type": "naked",   "consumptions": [ 3.1, 3.4, 2.5, 3.3, 3.2]},
          { "brand": "Yamaha",  "model" : "MT-07",    "year": 2020, "type": "enduro", "consumptions": [ 3.7, 3.4, 2.9, 3.4, 3.2]},
          { "brand": "Honda",    "model" : "CBR650R","year": 2021, "type": "sport",    "consumptions": [ 4.7, 4.4, 4.9, 5.4, 5.2]},
     ]
}





class Vehicle:
    def __init__(self,brand,model,year, consumptions):
        self.brand=brand
        self.model=model
        self.year=year
        self.consumptions=consumptions
    def getAverageConsumption(self):
        return sum(self.consumptions)/len(self.consumptions)

class Car(Vehicle):
    def __init__(self,brand,model,year, consumptions,fuel_type):
        Vehicle.__init__(self,brand,model,year, consumptions)
        self.fuel_type = fuel_type

    def __str__(self):
        return f'The car is a {self.fuel_type} {self.brand} {self.model}, made in {self.year} with an average consumption of {self.getAverageConsumption()}'


class Motorbikes(Vehicle):
    def __init__(self,brand,model,year, consumptions,_type):
        Vehicle.__init__(self,brand,model,year, consumptions)
        self._type = _type

    def __str__(self):
        return f'The bike is a  {self.brand} {self.model}, ({self._type}) made in {self.year} with an average consumption of {self.getAverageConsumption()}'




vehicles = []

for car in export["cars"]:
    vehicles.append(Car(car["brand"],car["model"],car["year"],car["consumptions"],car["fuel type"]))

for bike in export["motorbikes"]:
    vehicles.append(Motorbikes(bike["brand"],bike["model"],bike["year"],bike["consumptions"],bike["type"]))


for vehicle in vehicles:
    print(vehicle)
