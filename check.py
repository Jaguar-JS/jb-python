from app.main import Car, CarWashStation

print("1. Checking classes Car, CarWashStation, serve_cars - method")
bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')

print(bmw.clean_mark)  # 3

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])

print(income)  # 6.3
print(bmw.clean_mark)  # 6

print("2. Checking If audi.clean_mark was below wash_station.clean_power\n then audi would have been washed as well and the income would have raised:")

bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=2, brand='Audi')

print(bmw.clean_mark)  # 3
print(audi.clean_mark) # 2

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])

print(income)  # 17.5

print(bmw.clean_mark)  # 6
print(audi.clean_mark) # 6

print("3. Checking method rate_service\n")

wash_station = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11
)

print(wash_station.average_rating)    # 3.9
print(wash_station.count_of_ratings)  # 11

wash_station.rate_service(5)

print(wash_station.average_rating)    # 4.0
print(wash_station.count_of_ratings)  # 12

print("4. Checking methods CarWashStation\n")

bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([
    bmw,
    audi,
    mercedes
])
assert income == 41.6, f"Expected income to be 41.6, but got {income}"

assert bmw.clean_mark == 8, f"Expected BMW's clean mark to be 8, but got {bmw.clean_mark}"
assert audi.clean_mark == 9, f"Expected Audi's clean mark to be 9, but got {audi.clean_mark}"  # audi wasn't washed
assert mercedes.clean_mark == 8, f"Expected Mercedes' clean mark to be 8, but got {mercedes.clean_mark}"  # all other cars are washed to '8'

ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford)
# only calculating cost, not washing
assert wash_cost == 9.1, f"Expected wash cost for Ford to be 9.1, but got {wash_cost}"
assert ford.clean_mark == 1, f"Expected Ford's clean mark to remain 1, but got {ford.clean_mark}"

ws.rate_service(5)

assert ws.count_of_ratings == 12, f"Expected count of ratings to be 12, but got {ws.count_of_ratings}"
ws.average_rating == 4.0, f"Expected average rating to be 4.0, but got {ws.average_rating}"
