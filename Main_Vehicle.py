

import Vehilcle 



def main():
    user_car = Vehilcle.Automobiles('audi', 'a4', 100, 40000, 4)
    user_car1 = Vehilcle.Automobiles('nissan', 'gtr', 100, 120000, 2)

    print('Make: ', user_car.get_make())
    print('Model: ', user_car.get_model())
    print('Mileage: ', user_car.get_mileage())
    print('Price: ', user_car.get_price())
    print('Doors: ', user_car.get_doors())

    print('\n')
    

    print('Make: ', user_car1.get_make())
    print('Model: ', user_car1.get_model())
    print('Mileage: ', user_car1.get_mileage())
    print('Price: ', user_car1.get_price())
    print('Doors: ', user_car1.get_doors())

main()


