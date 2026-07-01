# 3 - masala

from collections import namedtuple

Car = namedtuple('Car', ['brand', 'model', 'year', 'mileage'])

cars = [
    Car('Chevrolet', 'Coblat', 2019, 15000),
    Car('Chevrolet', 'Gentra', 2023, 26000),
    Car('Chevrolet', 'Malibu', 2020, 140000),
    Car('Chevrolet', 'Matiz', 2010, 200000),
    Car('Chevrolet', 'Spark', 2017, 30000)
]

kam_yurgani = min(cars, key = lambda x: x.mileage)
print(f'Eng kam yurgan mashina nomi: {kam_yurgani.model} - masofa :{kam_yurgani.mileage}')
