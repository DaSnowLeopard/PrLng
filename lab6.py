text = ["Я", "хочу", "спать", "сейчас", "очень", "сильно", "потому", "что",
        "устала", "я", "хочу", "лечь", "в", "теплую", "постель", "и", "закрыть",
        "глаза", "и", "мечтать", "о", "чем", "то", "хорошем", "я", "правда", "хочу", "поспать"]

print(' '.join(text))

for i in range(len(text)):
    text[i] = text[i].lower()

print(' '.join(sorted(text)))

