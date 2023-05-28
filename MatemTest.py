from math import*
import random

'''
Математический тест.
Все подробно закомментировал в "tase 1" и "tase2". В цикле "tase 3" все повторяется, поэтому комментариев меньше.

Tase 1 - легко
Tase 2 - не очень сложно
Tase 3 - бывает достаточно сложно

В "tase 1" можно вводить в качестве ответов только целые числа (int)

В "tase 2" и "tase 3" присутствует деление и нужно вводить в ответы числа с плавающей точкой (float), с округлением до 2 цифр после запятой.

Если сразу не получиться, то прилагаются правилные ответы.

'''


digitsList = ['1','2','3','4','5','6','7','8','9'] # Список цифр для рандомного выбора
plusMinusList = ['+','-'] # Список математических операций для "Tase 1" а также используется в "Tase 3"
multDivList = ['*','/'] # Список операций для "Tase 2", и также используется в "Tase 3"

correctAnswer = 0 # Счетчик правильных ответов

while True: # Цикл предлагает постоянно меню, в котором при помощи цифр можно выбрать уровень сложности 1, 2, 3 или выход на 0
    print("Matemaatile test. \n\nValige sobiv tase.\nKui soovite Tase-1, siis kirjutage: 1 \nTase-2, valige: 2 \nTase-3 siis: 3 \nValja: 0")
    option = input("\nSinu valik: ")


    if option == '1': # Первый уровень сложности: достаточно легко. Использует только целые числа для ответа (int)
        print("\nTase 1")

        print("Kui palju ulesanndeid sa soovid teha?") 
        howMany = int(input("Sissesta ulesannete arv: ")) # Просим ввести количество примеров для решения.

        for times in range(0, howMany,1): # цикл FOR (start: 0, stop: howMany, step: 1). howMany - переменная, которая содержит число от пользователя.(Будет "крутить" цикл FOR столько раз, сколько примеров для решения запросил пользователь строкой выше.)
            
            a = int(random.choice(digitsList)) # Создется произвольное число на основании списка digitsList, которое записывается в переменную "a"
            b = int(random.choice(digitsList)) # Создется второе произвольное число, которое записывается в переменную "b"
            plusORminus = random.choice(plusMinusList) # Случайным образом выбирается математический знак из списка plusMinusList

            simpleTask = eval(str(a)+plusORminus+str(b)) # Тут записывается математическое пример либо такой: a + b, либо a - b. Затем он просчитывается. Благодаря динамической функции eval() удается задать произвольный математический знак операции(либо "+" либо "-"). Без этой функции запись: "a plusORminus b" постоянно выдавала ошибку.
            
            print(f"\n{a} {plusORminus} {b}") # Математический пример выодится для пользователя на консоль
            answer = int(input("Vastus: ")) # Просим пользователя ввести ответ

            if answer == simpleTask:    # Делаем проверку на правильность на правильность ответа от пользователя
                print("Oige vastus\n")
                correctAnswer+=1 # Счетчик, считает количество правильных ответов

            elif answer != simpleTask: # Если пользователь ответил неправильно, то... 
                print("Vale!")          # Cообщаем об этом пользователю и следом выводим правильный ответ строкой ниже.
                print(f"Oleks oige vastus: {simpleTask}\n")



    elif option == '2': # Второй уровень сложности: не очень сложно. Использует уже дробные и целые числа для ответа (float и int)
        print("\nTase 2")

        print("Kui palju ulesanndeid sa soovid teha?")
        howMany = int(input("Sissesta ulesannete arv: ")) # Просим ввести количество примеров для решения. Переменную howMany испольуем в цикле FOR. 

        for times in range(0, howMany,1):                    

            a = int(random.choice(digitsList)) # Создется произвольное число, которое записывается в переменную "a"
            b = int(random.choice(digitsList)) # Создется второе произвольное число, которое записывается в переменную "b"
            multORdiv = random.choice(multDivList) # Рандомно выбирается математический знак "*" или "/"

            mediumTask = eval(str(a)+multORdiv+str(b)) # Тут записывается математическое выражение либо такое: a * b, либо a / b. Затем оно просчитывается. Благодаря динамической функции eval() удается задать произвольный математатический знак операции(либо "*" либо "/"). Без этой функции eval() запись: "a multORdiv b" постоянно выдавала ошибку.

            mediumTask = round(mediumTask,2) # Округляем ответ до 2-х цифр после запятой, так как при делении может получиться число с большим количеством цифр после запятой

            print(f"\n{a} {multORdiv} {b}") # Математический пример выодится для пользователя на консоль
            answer = float(input("Vastus: ")) # Просим пользователя ввести ответ и округляем его до 2-х знаков после запятой.

            answer = round(answer,2) # Также округляем ответ пользователя до 2- цифр после запятой

            if answer == mediumTask: # Делаем проверку ответа на правильность
                print("Oige vastus\n")
                correctAnswer+=1 # Считаем количество правильных ответов

            elif answer != mediumTask: # Если ответ неверный, то сообщаем об этом пользователю и следом выводим правильный ответ строкой ниже.
                print("Vale!")
                print(f"Oleks oige vastus: {mediumTask}\n")
        
                

    elif option == '3': # Третий уровень сложности: бывает сложно. Использует дробные и целые числа для ответа (float и int)
        print("\nTase 3") # В уровне 3 все та же логика выполнения действий, что и в уровне 1 (tase 1) и уровне 2. Разница лишь в том что исрользуется 3-е число и все математичекие знаки(+, -, *, /,)

        print("Kui palju ulesanndeid sa soovid teha?")
        howMany = int(input("Sissesta ulesannete arv: "))

        for times in range(0, howMany,1):

            a = int(random.choice(digitsList))
            b = int(random.choice(digitsList))
            c = int(random.choice(digitsList))      # Случайным образом выбирается 3-е число "c"
            plusORminus = random.choice(plusMinusList) # Случайным образом выбирается математический знак из списка plusMinusList (т.е. + или -)
            multORdiv = random.choice(multDivList) # Случайным образом выбирается математический знак из списка multDivList (т.е. * или /)

            hardTask = eval(str(a)+multORdiv+str(b)+plusORminus+str(c))
            
            hardTask = round(hardTask,2) # Округляем ответ до 2-х цифр после запятой, так как при делении может получиться число с большим количеством цифр после запятой.
            
            print(f"\n{a} {multORdiv} {b} {plusORminus} {c}")
            answer = float(input("Vastus: "))

            answer = round(answer,2) # Округляем ответ пользователя до 2- цифр после запятой

            if answer == hardTask:
                print("Oige vastus\n")
                correctAnswer+=1

            elif answer != hardTask:
                print("Vale!")
                print(f"Oleks oige vastus: {hardTask}\n")
        
            

    elif option == '0': # Выход из бесконечного цикла меню.
        print("Lahen valja")
        break
    

    else: # Подсказка в случае, если не ввели нужную цифру в выборе меню.
        print("Kirjutage uks number: 1, 2, 3 voi 0 - valja.\n")


    ### Высчитываем оценку.
    result = correctAnswer/howMany * 100
    
    if result < 61:
        print("Sinu Hinne on 2\n")
    elif 61 <= result < 75:
        print("Sinu Hinne on 3\n")
    elif 75 <= result < 90:
        print("Sinu Hinne on 4\n")
    else:
        print("Sinu Hinne on 5\n")

    correctAnswer = 0 # Обнуляем счетчик. Чтобы он подсчитывал правильное количество ответов в каждом новом задании, если мы не выходим из основного меню (т.е. из цикла while true)

    input()




        
  
    

