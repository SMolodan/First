workers = {
    "The last of us": {
        "Жанр": "Хоррор",
        "Розробник":["Naughty Dog" , "9"]

    },
    "Detroit": {
        "Жанр": "Інтерактивне кіно",
        "Розробник":["Quantic Dream" , "8.5"]

    },
    "GTA V": {
        "Жанр": "Екшн-пригода",
        "Розробник":["Rockstar North" , '9.5']

    }
}

question = input("Виберіть варіант:\n1 - яка гра має найбільший рейтинг,\n2 - яка гра має найнижчий рейтинг,\n3 - скільки ігор мають рейтинг вище 9")


rating_count = 0

for worker in workers:
    rating = float(workers[worker]["Розробник"][1])
    if rating > 9:
        rating_count += 1

if question == "1":
    print("Гра з найбільшим рейтингом:\nGTA V:\n" , workers['GTA V'] )
elif question == "2":
    print("Гра з найнижчим рейтингом:\nDetroit:\n", workers['Detroit'])
elif question == '3':
    print("Кількість ігор з рейтингом вище 9:", rating_count )
else:
    print("Невідоме питання")
