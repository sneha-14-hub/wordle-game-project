
# 🎯 Wordle Game (Python + Rich Library)

A colorful terminal-based **Wordle clone** built using **Python** and the [`rich`](https://github.com/Textualize/rich) library for styled console output.

## 🧩 Overview

This project recreates the popular **Wordle** game experience in your command line.  
Players have **6 chances** to guess a randomly selected 5-letter word.  
Each guess is color-coded using Rich:

🟩 — correct letter in the correct place  
🟨 — correct letter in the wrong place  
⬛ — incorrect letter


## ⚙️ Features

- 🎨 Beautiful terminal colors using the `rich` library  
- 🧠 Random 5-letter words from a predefined list  
- 🔁 Validations for repeated or invalid guesses  
- 📊 Pattern display for all guesses  
- 🏁 Automatic win/lose summary after 6 attempts  


## 🏗️ Tech Stack

- **Language:** Python 3  
- **Library:** [`rich`](https://github.com/Textualize/rich) (for console colors & prompts)


## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/wordle-game.git
   cd wordle-game


2. Install dependencies:

   ```bash
   pip install rich
   ```
   

3. Run the game:

   ```bash
   python wordle.py
   ```

---

## 🎮 Example Gameplay

```
WELCOME TO WORDLE

You may start guessing

Enter your guess: APPLE
🟩🟨⬛⬛🟩
```

After each guess, feedback squares show your progress — just like the real Wordle!

---

## 💡 Future Improvements

* Add a larger word bank
* Include a scoring system
* Add hints or difficulty levels
* Save user stats across sessions

---

## 👩‍💻 Author
SNEHA

