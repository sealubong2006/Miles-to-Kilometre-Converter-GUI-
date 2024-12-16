from tkinter import *

# Create the main application window
windows = Tk()
windows.title("Miles to Kilometre Converter")  # Set the window title
windows.minsize(width=300, height=100)  # Set the minimum size of the window
windows.config(padx=20, pady=20)  # Add padding around the window

# Label 1: "is equal to"
my_label_1 = Label(text="is equal to", font=("Arial", 12))
my_label_1.grid(column=0, row=1)  # Position the label in the grid

# Label 2: "Miles"
my_label_2 = Label(text="Miles", font=("Arial", 12))
my_label_2.grid(column=2, row=0)  # Position the label in the grid

# Label 3: "Kilometres"
my_label_3 = Label(text="Kilometres", font=("Arial", 12))
my_label_3.grid(column=2, row=1)  # Position the label in the grid

# Function to calculate the kilometre value based on the miles input
def kilo_value():
    value = input_.get()  # Get the value from the miles input field
    km = float(value) * 1.60934  # Convert miles to kilometres
    input_1.delete(0, END)  # Clear any existing value in the kilometre field
    input_1.insert(END, string=str(km))  # Insert the calculated kilometre value

# Entry field for miles input
input_ = Entry(width=10)
input_.grid(column=1, row=0)  # Position the entry field in the grid

# Entry field for kilometre output
input_1 = Entry(width=10)
input_1.grid(column=1, row=1)  # Position the entry field in the grid

# Button to trigger the conversion
button = Button(text="Calculate", command=kilo_value)  # Attach the function to the button
button.grid(column=1, row=2)  # Position the button in the grid





# Run the application event loop
windows.mainloop()