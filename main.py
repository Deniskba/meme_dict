meme_dict = {
            "CRINGE": "Что-то очень странное или стыдное",
            "LOL": "Что-то очень смешное"
            }

while True: 
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        # Что делать, если слово нашлось?
        print(meme_dict[word])
    else:
        # Что делать, если слово не нашлось?
        print('you made a misstake or this word is not in dictionary')
