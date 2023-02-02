# have a python dictionary that has a key/value pair that represent a word and it's definition
# collect input from the user, input is a word
# check id the word is in the dictionary or not
# print hte definition

word_dictionary = {
    'sorry': 'maaf',
    'go': 'pergi',
    'grow': 'tumbuh',
    'love': 'cinta',
    'jump': 'lompat',
    'cook': 'memasak',
    'air': 'udara',
    'water': 'air',
    'fire': 'api',
    'home': 'rumah',
    'flower': 'bunga',
    'fun': 'menyenangkan',
    'fur': 'bulu',
    'from': 'dari',
    'eyes': 'mata',
    'spy': 'mata-mata',
    'fish': 'ikan',
    'bird': 'burung',
    'garage': 'garasi',
    'hall': 'aula',
    'wall': 'tembok',
    'create': 'membuat',
    'build': 'membangun',
    'float': 'mengambang',
    'pity': 'menyedihkan',
    'train': 'kereta',
    'rain': 'hujan',
    'ruin': 'menghancurkan',
    'write': 'menulis',
    'will': 'akan',
    'quit': 'keluar',
    'queen': 'ratu',
    'king': 'raja',
    'kill': 'membunuh',
    'clown': 'badut',
    'clear': 'jelas',
    'clean': 'bersih',
    'tidy': 'merapikan',
    'fool': 'bodoh',
    'floor': 'lantai',
    'let': 'membiarkan',
    'view': 'pemandangan',
    'word': 'kata',
    'sentence': 'kalimat',
    'done': 'selesai'
}


def main():

    option = input("Translate english word to bahasa? (y/n)")
    while option.lower() == 'y':
        word = input("Enter a word: ")
        look_out(word)
    else:
        print("Bye")
        exit()


def look_out(word):
    if word == "":
        exit()
    if word in word_dictionary:
        print(f"{word}: {word_dictionary[word]}")


main()
