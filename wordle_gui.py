import tkinter as tk
from tkinter import messagebox, scrolledtext

def grayLetters(all_words, gray_letters):
    gray_words = []
    for word in all_words:
        if not set(word).intersection(gray_letters):
            gray_words.append(word)
    return gray_words

def yellowLetters(all_words, yellow_letters):
    yellow_words = [word for word in all_words if len(set(word).intersection(yellow_letters)) == len(yellow_letters)]
    return yellow_words

def greenLetters(all_words, green_letters):
    green_words = []
    green_count = len(list(filter(None, green_letters)))
    len_word = len(green_letters)
    for word in all_words:
        counter = 0
        for index in range(len_word):
            if green_letters[index] and word[index] == green_letters[index]:
                counter += 1
        if counter == green_count:
            green_words.append(word)
    return green_words

def load_words(filename="C:/projects/wordle/5lettergermanwords.txt"):
    with open(filename, "r", encoding="utf8") as file:
        return [word.strip().lower() for word in file.readlines()]

def run_filter():
    gray = gray_entry.get().lower()
    yellow = yellow_entry.get().lower()
    green = [g1.get().lower(), g2.get().lower(), g3.get().lower(), g4.get().lower(), g5.get().lower()]

    words = load_words()
    gray_filtered = grayLetters(words, gray)
    yellow_filtered = yellowLetters(gray_filtered, yellow)
    green_filtered = greenLetters(yellow_filtered, green)

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Possible Words ({len(green_filtered)}):\n")
    result_text.insert(tk.END, "\n".join(green_filtered))

# ---------------- Tkinter GUI ------------------

root = tk.Tk()
root.title("Wordle Solver")
root.geometry("500x500")

tk.Label(root, text="Gray Letters:").pack()
gray_entry = tk.Entry(root)
gray_entry.pack()

tk.Label(root, text="Yellow Letters:").pack()
yellow_entry = tk.Entry(root)
yellow_entry.pack()

tk.Label(root, text="Green Letters (one per box):").pack()
frame = tk.Frame(root)
frame.pack()

g1 = tk.Entry(frame, width=3); g1.pack(side=tk.LEFT)
g2 = tk.Entry(frame, width=3); g2.pack(side=tk.LEFT)
g3 = tk.Entry(frame, width=3); g3.pack(side=tk.LEFT)
g4 = tk.Entry(frame, width=3); g4.pack(side=tk.LEFT)
g5 = tk.Entry(frame, width=3); g5.pack(side=tk.LEFT)

tk.Button(root, text="Submit", command=run_filter).pack(pady=10)

result_text = scrolledtext.ScrolledText(root, height=15, width=50)
result_text.pack(padx=10, pady=10)

root.mainloop()
