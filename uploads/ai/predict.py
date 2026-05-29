import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# ------------------ ML MODEL ------------------

# Dataset
data = pd.DataFrame({
    'age': [25,40,30,50,22,35,28,60,45],
    'fever': [1,1,0,1,0,1,0,1,0],
    'cough': [1,0,1,1,0,1,1,1,1],
    'bp': [120,130,110,150,115,140,118,160,135],
    'disease': ['Flu','Viral','Cold','Fever','Normal','Flu','Cold','Serious','Viral']
})

X = data[['age','fever','cough','bp']]
y = data['disease']

model = DecisionTreeClassifier()
model.fit(X, y)

# ------------------ FUNCTIONS ------------------

def open_prediction_window():
    home_window.destroy()
    prediction_window()

def predict_disease():
    try:
        age = int(age_entry.get())
        fever = int(fever_entry.get())
        cough = int(cough_entry.get())
        bp = int(bp_entry.get())

        result = model.predict([[age, fever, cough, bp]])
        messagebox.showinfo("Prediction Result", f"Predicted Disease: {result[0]}")

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

def prediction_window():
    global age_entry, fever_entry, cough_entry, bp_entry

    window = tk.Tk()
    window.title("Disease Prediction")
    window.geometry("300x300")

    tk.Label(window, text="Enter Patient Details").pack(pady=10)

    tk.Label(window, text="Age").pack()
    age_entry = tk.Entry(window)
    age_entry.pack()

    tk.Label(window, text="Fever (1=Yes, 0=No)").pack()
    fever_entry = tk.Entry(window)
    fever_entry.pack()

    tk.Label(window, text="Cough (1=Yes, 0=No)").pack()
    cough_entry = tk.Entry(window)
    cough_entry.pack()

    tk.Label(window, text="BP").pack()
    bp_entry = tk.Entry(window)
    bp_entry.pack()

    tk.Button(window, text="Predict", command=predict_disease).pack(pady=10)

    window.mainloop()

# ------------------ HOME PAGE ------------------

home_window = tk.Tk()
home_window.title("Hospital Management System")
home_window.geometry("300x200")

tk.Label(home_window, text="Welcome to HMS AI System", font=("Arial", 14)).pack(pady=20)

tk.Button(home_window, text="Disease Prediction", command=open_prediction_window).pack(pady=10)

home_window.mainloop()