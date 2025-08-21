def feet_to_meters(value):
    return value * 0.3048

def meters_to_feet(value):
    return value / 0.3048

feet = float(input('? '))
print(f'{feet}ft = {feet_to_meters(feet)}mt')

choice = input('f2m or m2f? ')
value = float(input('? '))
if choice == 'f2m':
    print(f'{value}ft = {feet_to_meters(value)}mt')
else: 
    print(f'{value}mt = {meters_to_feet(value)}ft')