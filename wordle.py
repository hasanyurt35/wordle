
def dict_creator(filename= "englishwords.txt", letter_count= 5):
    with open(filename,"r", encoding="utf8") as file:
        all_words = file.readlines()
    words_list = [word.lower() for word in all_words if len(word) == letter_count +1 and word[:-1].isalpha()]
    file_name = f"{letter_count}letter{filename}"
    with open(file_name, "w", encoding="utf8") as file:
        file.writelines(words_list)
    return f"{file_name} file is created"

def grayLetters(all_words, gray_letters):
    gray_words = []
    for word in all_words:
        if not set(word).intersection(gray_letters):
            gray_words.append(word)
    return gray_words

def yellowLetters(all_words, yellow_letters):
    yellow_words = [word for word in all_words if len(set(word).intersection(yellow_letters))== len(yellow_letters)]
    return yellow_words

def greenLetters(all_words, green_letters):
    green_words = []
    green_count = len(list(filter(None, green_letters)))
    len_word = len(green_letters)
    for word in all_words:
        counter = 0
        for index in range(len_word):
            if word[index] == green_letters[index]:
                counter +=1
        if counter == green_count:
            green_words.append(word)
    return green_words

def main():
    with open("5letterenglishwords.txt", "r", encoding="utf8") as file:
        five_letter_words = [word[:-1] for word in file.readlines()]
    print("You can hack 5 Letter wordle game with this app. \nStart with until, dames and broch")
    gray_letters = input("Enter gray letters: ")
    yellow_letters = input("enter yellow letters: ")

    green_letters = []
    for i in range(1,6):
        green_letters.append(input(f"Enter letter {i} if it is green, if not hit enter: "))
    gray_words = grayLetters(five_letter_words, gray_letters)
    # print(len(gray_words), gray_words)
    yellow_words = yellowLetters(gray_words, yellow_letters)
    # print(len(yellow_words), yellow_words)
    green_words = greenLetters(yellow_words, green_letters)
    print(len(green_words), green_words)

if __name__ == "__main__":
    main()
