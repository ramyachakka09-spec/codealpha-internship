# 🎮 Hangman Game in Python

A simple command-line **Hangman Game** built using Python. The game randomly selects a word, and the player has to guess it one letter at a time before running out of attempts.

---

## 📌 Features

- Random word selection
- Letter-by-letter guessing
- Input validation
- Prevents duplicate guesses
- Displays remaining attempts
- Win and lose conditions
- Beginner-friendly Python project

---

## 🛠️ Technologies Used

- Python 3
- Built-in `random` module

---

## 📂 Project Structure

```
Hangman/
│── hangman.py
│── README.md
```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/hangman-game.git
```

2. Navigate to the project folder.

```bash
cd hangman-game
```

3. Run the Python file.

```bash
python hangman.py
```

---

## 🎯 How to Play

1. The game randomly chooses a word.
2. Guess one letter at a time.
3. If the letter is correct, it appears in the word.
4. If the letter is incorrect, one attempt is lost.
5. You have **6 incorrect attempts**.
6. Guess the entire word before your attempts run out.

---

## 📷 Sample Output

```
========================================
        HANGMAN GAME
========================================
Guess the word one letter at a time.
You have 6 incorrect guesses.

Word: _ _ _ _ _ _

Enter a letter: p
✅ Correct Guess!

Word: p _ _ _ _ _

Enter a letter: x
❌ Wrong Guess!
Remaining Attempts: 5
```

---

## 📋 Word List

The game currently selects a random word from the following list:

- python
- coding
- computer
- program
- developer

You can easily modify the list inside the code:

```python
words = ["python", "coding", "computer", "program", "developer"]
```

---

## 🚀 Future Improvements

- Add difficulty levels
- Load words from a text file
- ASCII Hangman graphics
- Score tracking
- Play again option
- Multiplayer mode
- Categories (Animals, Fruits, Countries, etc.)

---

## 🧠 Concepts Used

- Loops (`while`, `for`)
- Conditional statements (`if`, `else`)
- Lists
- Strings
- User input
- Random module
- Input validation

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a Pull Request.

---

## 📄 License

This project is open source and available under the **MIT License**.

---

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/your-username

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
