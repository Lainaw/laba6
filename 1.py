countriesDict={"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
"Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
"Северная Македония": "Скопье", "Сербия": "Белград"}
print('пары страна-столица:',countriesDict)
while True:
    print('1 - Узнать столицу страны или наоборот','\n','2 - Добавить новую страну и столицу','\n','3 - Вывести список стран по алфавиту')
    
    menu=input()
    if menu== "1":
        v=input('Будем искать страну по стoлице(1) или стoлицу по стране(2)?')
        if v == "1":
            dict_items = countriesDict.items()
            city = input('Введите название столицы:')
            for key, value in dict_items:
                if value == city:
                    print("Эта столица пренадлежит:", key)
        elif v == "2":
            country = input('Введите название страны:')
            print("Столица этой страны: ", countriesDict[country])
    elif menu == "2":
        countryAdd = input('Введите название страны,которую хотите добавить:')
        cityAdd = input('Введите название столицы:')
        countriesDict[countryAdd] = cityAdd
    elif menu == "3":
        sortedTuple = sorted(countriesDict.items(), key=lambda x: x[0])
        print(dict(sortedTuple))