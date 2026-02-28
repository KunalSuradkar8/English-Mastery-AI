# 🚀 English Mastery AI Tutor

Welcome to the **English Mastery AI Tutor**! 
This is not just a simple grammar checker; it is a smart, Python-based desktop application that acts as your personal English teacher. It helps you learn English naturally by finding your mistakes, correcting them, and explaining the grammar rules in your native language (Marathi).

---

## 🎯 Why I Built This Project (Motivation)
Learning English grammar can be confusing. Most tools online only tell you *what* is wrong, but they don't tell you *why* it is wrong or *how* to fix it. 
As someone learning both English and Programming at the same time, I wanted to build a system that:
1. Translates my thoughts from English to Marathi.
2. Checks if my grammar is correct.
3. Teaches me the rule behind the mistake.
4. Keeps a record of my daily practice securely on my own computer.

---

## ✨ Deep Dive Into Features

### 🧠 1. Smart Grammar Brain
It doesn't just check spellings. It understands the structure of the sentence.
* **Subject-Verb Agreement:** It checks if you are using 'is/are', 'has/have', or 'was/were' correctly with the subject (e.g., *He has* instead of *He have*).
* **Articles & Prepositions:** It guides you on where to use 'a', 'an', 'the', 'in', 'at', or 'on'.
* **Parts of Speech:** It breaks down your sentence and tells you which word is a Noun, Verb, Pronoun, or Conjunction.

### 💡 2. Auto-Suggestions & Tips
If you make a mistake, the app doesn't just show a red flag.
* It generates a **Corrected Sentence** (💡) showing exactly how it should be written.
* It provides **Learning Tips** (🎓) in simple Marathi so you never make the same mistake twice.

### 🌐 3. Real-Time Translation
Integrated with the Google Translate API (`googletrans`), it instantly translates your English sentence into Marathi so you can verify if the meaning is what you intended to say.

### 💾 4. Personal Database Tracking
Your learning data is completely private. The app uses a local **SQLite3 Database** to silently save:
* The sentence you typed.
* The time and date you practiced.
* Whether the sentence was right or wrong.
(This data can later be used to create analytics and progress charts!)

### 🎨 5. Beautiful Dark Mode UI
Built using Python's `Tkinter`, the user interface is modern, eye-friendly (Dark Mode), and very easy to use. No complicated menus—just type and learn!

---

## 🏗️ How It Works (Project Structure)
This software is divided into different parts, just like a real-world application:
* **`gui_main.py` (The Face):** Handles the beautiful Dark Mode window and buttons.
* **`english_tutor.py` (The Teacher):** Checks the rules, finds mistakes, and generates tips.
* **`grammar_brain.py` (The Memory):** A library of words, verbs, and English rules.
* **`progress_tracker.py` (The Bookkeeper):** Connects to the SQL database to save your daily progress.

---

## 🛠️ Technology Stack Used
* **Programming Language:** Python 3.x
* **Graphical Interface (GUI):** Tkinter
* **Database Management:** SQLite3 (Local SQL Database)
* **External APIs:** Googletrans (For language translation)
* **Version Control:** Git & GitHub

---

## 👨‍💻 About the Developer
Developed by **Kunal**. 
I am on a journey to understand how computers, software, and data work together. this project is my step towards learning Python, APIs, and Database integration by building something that solves a real-world problem.

---
*If you like this project, feel free to explore the code!* ⭐