print("\tПошук значення у масиві")
introduction = input("Якщо хочете дізнатися, як працює програма, то напишіть (так/ні): ")
if introduction == "так":
    print("Програма створює масив 5x5 елементів. Масив заповнюється довільними значеннями чілих чисел від 1 до 99. Програма виводить значення масиву, виводячи додаткові симоли біля кожного елементу.")
    print("Користувачем вводиться певне значення цілого числа. Після цього програми виводить значення масиву, змінюючи додаткові символи біля значень, що більше за введене число.")
   
else:
    print("Тоді почнемо!")

import random

def create_and_print_array():
    array = [[random.randint(1, 99) for _ in range(5)] for _ in range(5)]
    for row in array:
        for num in row:
            print(f'-{num:02}-  ', end='')
        print()
    return array

def print_array_with_highlight(array, threshold):
    for row in array:
        for num in row:
            if num > threshold:
                print(f'*{num:02}*  ', end='')
            else:
                print(f'-{num:02}-  ', end='')
        print()

if __name__ == "__main__":
    print("Створення початкового масиву:")
    original_array = create_and_print_array()
    
    user_input = int(input("Введіть значення для виділення: "))
    
    print("Масив з виділеними значеннями:")
    print_array_with_highlight(original_array, user_input)
