# CSC500 – Critical Thinking Assignment 7
## Course Lookup Utility (CTA7)

### 📌 Overview
This small console program stores and looks up classroom information for a set of courses. It maps course numbers to room numbers, instructor names, and class start times. When run, the program shows the available course numbers and prompts the user to enter one. The prompt repeats in a loop so you can perform multiple lookups; enter `Q` (or `q`) at the prompt to quit. For each valid course number the program displays the room, instructor, and time for that course.

This implementation was created for **Critical Thinking Assignment 7** for **CSC500 – Principles of Programming**.

---

### 🖥️ Program Features
- Stores course data in three dictionaries:
  - course -> room number
  - course -> instructor name
  - course -> class time
- Accepts user input for a course number (case-insensitive, whitespace trimmed).
- Looks up and prints the room number, instructor, and class time for the entered course.
- Prints a friendly message when the entered course is not found.

---

### 📋 Example Usage

```
CSC101
Enter one of the above courses: csc101
Course Number: CSC101
Room Number: 3004
Instructor: Dr. Haynes
Class Time: 8:00 AM
```

If the user enters an invalid course:

```
Enter one of the above courses: MATH200
Course not found.
```

---

### ▶️ How to Run
1. Make sure you have Python 3 installed.
2. From the `CTA7` folder, run:

```powershell
python CTA7.py
```

3. Enter one of the displayed course numbers when prompted (or enter `Q` to quit).

---

Author: Anthony Le
