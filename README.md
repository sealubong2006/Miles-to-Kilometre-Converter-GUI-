# Miles to Kilometre Converter

## Description
This project is a simple GUI-based converter that converts values from miles to kilometres. It is built using Python's `tkinter` library and is suitable for beginners learning GUI development in Python.

---

## Features
1. Accepts user input in miles.
2. Displays the converted value in kilometres.
3. Simple, user-friendly interface with real-time calculations.

---

## How to Use
1. Enter a value in the "Miles" input field.
2. Click the **Calculate** button.
3. The equivalent value in kilometres will appear in the "Kilometres" field.

---

## File Descriptions
### `converter.py`
The main script that:
- Sets up the tkinter GUI.
- Accepts user input in miles.
- Calculates the equivalent kilometres using the formula:
  
  {kilometres} = {miles} times 1.60934 

- Displays the result in the output field.

---

## Code Breakdown
### 1. **GUI Components**
- **Labels**: Display text such as "Miles", "Kilometres", and "is equal to".
- **Entry Fields**:
  - One for user input (Miles).
  - Another for displaying the result (Kilometres).
- **Button**: Triggers the conversion function.

### 2. **Logic**
The conversion is handled by the `kilo_value` function, which:
- Reads the miles input from the user.
- Converts it into kilometres using the formula.
- Updates the output field with the result.

---

## Dependencies
- Python 3.x
- tkinter library (pre-installed with Python)

---

## Running the Project
1. Make sure you have Python installed on your system.
2. Save the `converter.py` file in your working directory.
3. Run the script:
   ```
   python converter.py
   ```
4. The GUI window will appear, and you can use the converter.

---

## Formula Used
To convert miles to kilometres, the program uses the formula:
{kilometres} = {miles} times 1.60934 

---

## Example
If the input is:
```
5 miles
```
The output will be:
```
8.0467 kilometres
```

---

## Customization
You can:
1. Change the window title by modifying this line:
   ```python
   windows.title("Miles to Kilometre Converter")
   ```
2. Adjust the font size and styles of the labels and buttons.

---

## Author
This project was created to demonstrate the basics of GUI programming using Python.

