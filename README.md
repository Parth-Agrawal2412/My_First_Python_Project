# Python Mini-Apps Suite 🚀

> *This is the first project I've ever released on GitHub, made with Python and love.* ❤️

Welcome to my Python Mini-Apps Collection! This repository features a versatile set of 9 command-line interface (CLI) tools designed to assist with daily tasks, simple calculations, text manipulation, security generation, and finance tracking.

---

## 🌟 Included Tools

| # | Tool Name | Description |
|---|---|---|
| **1** | **Calculator** | Evaluates basic math operations (`+`, `-`, `*`, `/`) with input validation and zero-division protection. |
| **2** | **Acronym Generator** | Takes any phrase or string of text and creates its uppercase acronym. |
| **3** | **Bill Generator** | Generates formatted bills with item names, prices, quantities, discount percentages, and clean table output. |
| **4** | **Mini Expense Tracker** | Tracks expense totals against daily wages (or calculates daily wage from monthly income). |
| **5** | **Password Generator** | Generates secure random passwords using letters, numbers, and special characters based on your chosen length. |
| **6** | **Password Strength Checker** | Evaluates password strength based on length, uppercase characters, numbers, and special symbols. |
| **7** | **Character Counter** | Analyzes text and displays letter occurrence frequencies across the alphabet. |
| **8** | **Word Counter** | Calculates total word count from input text strings. |
| **9** | **Salary Finder** | Converts income values seamlessly between Daily, Monthly, and Yearly representations. |

---

## ✨ Features

- **Robust Error Handling:** Input validation prevents crashes from non-numeric inputs or invalid options.
- **Clean CLI Formatting:** Structured tabular outputs and clear user prompts.
- **Modular & Standalone:** Runs either as individual standalone scripts or through a central menu interface.
- **Pure Python:** Built entirely using Python built-in modules—no external library dependencies needed!

---

## 🛠️ Prerequisites

Ensure you have **Python 3.6+** installed on your machine.

To check your installed Python version, run:
```bash
python --version
```


---

## 📖 Usage Examples

<details>
<summary><b>1. Calculator</b></summary>

```text
Welcome to the Calculator made by Parth Agrawal
Enter your Equation (e.g., 10 + 5): 42 * 3
Your result was: 126.0
```
</details>

<details>
<summary><b>2. Acronym Generator</b></summary>

```text
Welcome to the Acronym generator made by Parth Agrawal
Enter a text: Application Programming Interface
Acronym: API
```
</details>

<details>
<summary><b>3. Bill Generator</b></summary>

```text
-------------------------------------------------------
S.No  Item Name            Price      Qty      Total     
-------------------------------------------------------
1     Coffee               150.00     2        300.00    
2     Sandwich             120.00     1        120.00    
-------------------------------------------------------
Total Amount: 420.00
Total Items:  3
Discount:     42.00
Final Amount: 378.00
-------------------------------------------------------
```
</details>

## 🛠️ How to Run the Main Program

Follow these simple steps to start the main menu program:

### Step 1: Open Terminal / Command Prompt
Open your command terminal (macOS/Linux) or Command Prompt / PowerShell (Windows).

### Step 2: Navigate to Project Directory
Change directory to the folder where `Final_Project.py` is saved:

```bash
cd path/to/your/project-folder
```

### Step 3: Run the Script
Execute the program file using Python:

```bash
python Final_Project.py
```

---

## 🎮 Interactive Menu Navigation

Once launched, the application operates through an interactive command-line menu:

1. **Start Prompt:** Type **`y`** when asked `Want to run program (y or n):` to launch the option list.
2. **Select Tool:** Enter the corresponding number (**1 through 9**) for the tool you wish to run:
   * **1** — Calculator
   * **2** — Acronym Generator
   * **3** — Bill Generator
   * **4** — Mini Expense Tracker
   * **5** — Password Generator
   * **6** — Password Strength Checker
   * **7** — Character Counter
   * **8** — Word Counter
   * **9** — Salary Finder
3. **Exit Tool / Main Program:** Type **`stop`** at the menu prompt or enter **`n`** when asked whether to run the program to exit safely.

---

## 🧰 Module Overview & Usage Guidelines

Below is a detailed breakdown of each module available inside `Final_Project.py`:

### 1. 🧮 Calculator
* **Function:** Performs basic arithmetic operations between two numbers.
* **Format:** Enter expressions in the format `number operator number` (e.g., `10 + 5`, `20 / 4`).
* **Supported Operators:** `+`, `-`, `*`, `/`.

### 2. 🔤 Acronym Generator
* **Function:** Generates acronyms from multi-word strings.
* **Usage:** Type any phrase or phrase title (e.g., `"Hyper Text Markup Language"` $\rightarrow$ outputs `HTML`).

### 3. 🧾 Bill Generator
* **Function:** Calculates total items, prices, discounts, and generates a formatted receipt.
* **Usage:** Enter total items, item names, individual prices, quantities, and optional percentage discount. Displays an aligned tabular receipt summary.

### 4. 💰 Mini Expense Tracker
* **Function:** Tracks expenses against daily earnings.
* **Usage:** Log item names and costs, then enter your daily wage directly (or calculate it using your monthly salary and active working days). Displays net expenses and money saved.

### 5. 🔑 Password Generator
* **Function:** Generates strong, random passwords.
* **Usage:** Enter your desired password length. Outputs a combination of uppercase/lowercase letters, digits, and special characters.

### 6. 🛡️ Password Strength Checker
* **Function:** Evaluates the strength of custom passwords.
* **Usage:** Input any string. Returns total calculated strength points based on length, numeric characters, uppercase letters, and special symbols alongside a strength rating.

### 7. 📊 Character Counter
* **Function:** Counts frequency occurrences for every letter ($a-z$) in a given text string.
* **Usage:** Input any sentence or text body to print a letter frequency report.

### 8. 📝 Word Counter
* **Function:** Counts total word occurrences in a block of text.
* **Usage:** Enter a sentence or paragraph to receive total word count metrics instantly.

### 9. 💵 Salary Finder
* **Function:** Converts income figures between daily wages, monthly salary, and yearly earnings.
* **Usage:** Choose your starting input unit (Daily / Monthly / Yearly), enter the amount, and choose your target conversion unit. Run until typing `stop`.

---

## 🛠️ For getting Single Separated Code
                                     
Open the Separated_code Folder:

```
Separated_Code
├── acronym_generator.py
├── bill_generator.py
├── calculator.py
├── character_counter.py
├── mini_expense_tracker.py
├── password_generator.py
├── password_strength_checker.py
├── salary_finder.py
└── word_counter.py

```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Parth-Agrawal2412/My_First_Python_Project/issues).

---

## 👤 Author

**Parth Agrawal**
- GitHub: https://github.com/Parth-Agrawal2412

---

## 📜 License

This project is open source and available under the [CCO License](LICENSE).