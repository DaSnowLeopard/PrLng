import cars_h


num_cars = int(input("Enter the number of cars: "))

car_list = cars_h.get_car_data(num_cars)
selected_cars = cars_h.color_year_select(car_list)

print("\nSelected Cars:")
for car in selected_cars:
    print(car)


