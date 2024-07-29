# Перевірте свій код за наступними пунктами

## Стиль коду

1. Якщо у вас є довгі математичні обчислення, ви можете розділити їх на додаткові змінні або розбити після бінарних операцій (не перед ними — це спричиняє помилки W504).

Гарний приклад:

```python
fuel_consumption = max_fuel_consumption * height_fuel_consumption_coeficient
estimated_speed = plan_max_speed - wind_awerage_speed * wind_angle_coefisient
estimated_time = distance_to_the_destinatoin / estimated_speed
how_much_fuel_needed = fuel_consumption * estimated_time * overlap_coeficient
```

Гарний приклад:

```python
how_much_fuel_needed = (max_fuel_consumption
                        * height_fuel_consumption_coeficient
                        * distance_to_the_destinatoin
                        / (plan_max_speed
                           - wind_awerage_speed
                           * wind_angle_coefisient)
                        * overlap_coeficient)
```

Поганий приклад:

```python
how_much_fuel_needed = max_fuel_consumption \
                       * height_fuel_consumption_coeficient \
                       * distance_to_the_destinatoin / (
                               plan_max_speed 
                               - wind_awerage_speed 
                               * wind_angle_coefisient
                       ) * overlap_coeficient
```

2. Використовуйте описові та правильні назви змінних.

Гарний приклад:

```python
def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"
```

Поганий приклад:

```python
def get_full_name(x: str, y: str) -> str:
    return f"{x} {y}"
```

## Чистий код

1. Ви можете уникнути `else`, коли використовуєте оператор `return`.

Гарний приклад:

```python
def is_adult(age: int) -> str:
    if age >= 18:
        return "adult"
    return "not an adult"
```

Поганий приклад:

```python
def is_adult(age: int) -> str:
    if age >= 18:
        return "adult"
    else:
        return "not an adult"
```

2. Додавайте коментарі, оператори виводу та функції для перевірки свого рішення, коли пишете код. Не забувайте видаляти їх, коли ви готові до коміту та пушу вашого коду.