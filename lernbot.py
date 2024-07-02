import random


eng_words = ['Hi','Bye','Task', 'Programm']
ru_words = ['Привет','Пока','Задача', 'Программа']
score = 0
#perfomance
while True:  
    mod = input("Выбери режим работы тренажера: 1 - тренироваться, 2 - добавить новые слова, 3 - Выйти: \n")
    while ((mod != '1') and (mod != '2') and (mod != '3')):
        mod = input("Недопустимый символ! Выбери 1, 2 или 3. (1 - тренироваться, 2 - добавить новые слова, 3 - Выйти) \n")
    
    #Alfa 0
    if mod == '1':
        mod = 0
        print("Переведи как можно больше слов правильно! У тебя 10 попыток!")
        #Beta 0
        if len(eng_words) >= 9:
            #Gamma 0
            for i in range(10):
                #Delta 0
                number = random.randint(0, len(eng_words))
                print("Как переводится слово: " + eng_words[number])
                if input() == ru_words[number]:
                    print("Отлично!!!")
                    score += 1
                else:
                    print("Нет... Это слово - " + ru_words[number])
            print('Вы набрали ', score, ' из 10')
            continue
        else:
            print('Нужно минимум 10 слов!')
            continue    
    #Alfa 1
    if mod == '2':
        viel_wort = int(input('Сколько слов хотите добавить? \n'))
        #Beta 1
        if viel_wort >= 0:    
            print('При нажатии на enter 2 раза вы можете отменить действие.')
            #Gamma 1
            for j in range(viel_wort):
                word = input("Введите слово на русском языке: ")
                translate = input("Введите перевод этого слова: ")
                #Delta 1
                if len(word) > 0 and len(translate) > 0:
                    ru_words.append(word)
                    eng_words.append(translate)
                    print("Слово успешно добавлено!")
                else:    
                    break
                continue
        else:
            print('Число должно быть больше нуля!!!')
            continue
                 
    else:
        exit()   
