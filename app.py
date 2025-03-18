from flask import Flask, render_template, request
import tkinter as tk
from tkinter import messagebox

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        show_popup(user_input)
    return render_template("index.html")

def show_popup(text):
    root = tk.Tk()
    root.withdraw()  # Hide main window
    messagebox.showinfo("User Input", f"You entered: {text}")
    root.destroy()

if __name__ == "__main__":
    app.run(debug=True)
