class CarModels:
    def __init__(self):
        self.__Name = ''
        self.__Year = int()
        self.__Color = ''
        self.__Max_speed = ''
        self.__Body_type = ''
        self.__Price = ''


    def get(self):
        return (self.__Name + ', ' + self.__Year + ', ' + self.__Color + ', '
                + self.__Max_speed + ', ' + self.__Body_type + ', ' + self.__Price)

    def get_Name(self, Name):
        return self.__Name

    def get_Year(self, Year):
        return self.__Year

    def get_Color(self, Color):
        return self.__Color

    def get_Max_speed(self, Max_speed):
        return self.__Max_speed

    def get_Body_type(self, Body_type):
        return self.__Body_type

    def get_Price(self, Price):
        return self.__Price

    def get_car_data(self, num_cars):
        car_list = []
        for i in range(num_cars):
            print(f"Enter data for car {i + 1}:")
            self.__Name = input("name: ")
            self.__Year = input("year: ")
            self.__Color = input("color: ")
            self.__Max_speed = input("max speed: ")
            self.__Body_type = input("body type: ")
            self.__Price = input("price: ")
        return car_list

    def color_year_select(car_list):
        color = str(input("color to sort: "))
        year = int(input("minimum year: "))

        selected_cars = [car for car in car_list if car.get_Color() == color and int(car.get_Year()) >= year]
        return selected_cars