# Мийка автомобілів

Перед початком прочитайте [керівництво](https://github.com/mate-academy/py-task-guideline/blob/main/README.md).

Ви володієте станцією мийки автомобілів. Розрахунок вартості мийки займає багато часу, тому ви вирішуєте автоматизувати цей процес. Вартість мийки залежатиме від класу комфорту автомобіля, ступеня його чистоти, середнього рейтингу станції та відстані станції від центру міста.

Створіть клас `Car`, його метод `__init__` приймає та зберігає 3 аргументи:
1. `comfort_class` - клас комфорту автомобіля, від 1 до 7
2. `clean_mark` - оцінка чистоти автомобіля, від дуже брудного - 1 до абсолютно чистого - 10
3. `brand` - марка автомобіля

Створіть клас `CarWashStation`, його метод `__init__` приймає та зберігає 4 аргументи:
1. `distance_from_city_center` - відстань станції від центру міста, від 1.0 до 10.0
2. `clean_power` - `clean_mark`, до якого ця станція може очистити автомобіль (так, не всі станції можуть повністю очистити ваш автомобіль)
3. `average_rating` - середній рейтинг станції, від 1.0 до 5.0, округлений до 1 десяткової
4. `count_of_ratings` - кількість людей, які оцінили

Клас `CarWashStation` повинен мати такі методи:
1. `serve_cars` - метод, який приймає список автомобілів `Car`, миє тільки ті автомобілі, у яких `clean_mark` менше за `clean_power` станції мийки, і повертає дохід станції мийки за обслуговування цього списку автомобілів, округлений до 1 десяткової:

```python
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
```

Отже, мийка була виконана тільки для bmw, тому що `audi.clean_mark` > `wash_station.clean_power`, і `clean_mark` bmw змінився, тому що ми його помили.

Якби `clean_mark` audi був нижчим за `clean_power` станції мийки, то audi також був би помитий, і дохід би збільшився:

```python
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
```

2. `calculate_washing_price` - метод, який розраховує вартість для однієї мийки автомобіля. Вартість розраховується як: клас комфорту автомобіля * різниця між чистячою потужністю станції мийки та оцінкою чистоти автомобіля * рейтинг станції мийки / відстань станції мийки до центру міста, повертає число, округлене до 1 десяткової;
3. `wash_single_car` - метод, який миє один автомобіль, тому `clean_mark` повинен дорівнювати чистячій потужності станції мийки, якщо `clean_power` станції мийки більше, ніж `clean_mark` автомобіля;
4. `rate_service` - метод, який додає одну оцінку станції мийки, і на основі цієї оцінки змінюються `average_rating` та `count_of_ratings`:

```python
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
```

Ви можете додавати власні методи, якщо це необхідно.

Приклад:
```python
bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([
    bmw,
    audi,
    mercedes
])

income == 41.7

bmw.clean_mark == 8
audi.clean_mark == 9  
mercedes.clean_mark == 8
# audi не був помитий
# всі інші автомобілі помиті до '8'

ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford)  
# тільки розраховуємо вартість, не миємо
wash_cost == 9.1
ford.clean_mark == 1 

ws.rate_service(5)

ws.count_of_ratings == 12
ws.average_rating == 4.0
```

### Примітка: Перевірте свій код за допомогою цього [контрольного списку](checklist.md) перед тим, як завантажити своє рішення.