
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Python App 🚀")
root.geometry("500x420")
root.configure(bg="#111827")
root.resizable(False, False)

# Welcome heading
title = tk.Label(
    root,
    text="🚀 HELLO, DEVELOPER!",
    font=("Segoe UI", 22, "bold"),
    bg="#111827",
    fg="#A78BFA"
)
title.pack(pady=(35, 10))

subtitle = tk.Label(
    root,
    text="Your coding journey starts here.",
    font=("Segoe UI", 11),
    bg="#111827",
    fg="#D1D5DB"
)
subtitle.pack(pady=5)

# Name input
name_entry = tk.Entry(
    root,
    font=("Segoe UI", 14),
    justify="center",
    bg="#1F2937",
    fg="white",
    insertbackground="white",
    relief="flat"
)
name_entry.pack(padx=55, fill="x", ipady=12, pady=25)
name_entry.insert(0, "Enter your name")

# Greeting function
def say_hello():
    name = name_entry.get().strip()

    if not name or name == "Enter your name":
        message.config(
            text="Please enter your name first! 😊",
            fg="#FBBF24"
        )
    else:
        message.config(
            text=f"Welcome, {name}! 🎉\nYou're officially coding!",
            fg="#34D399"
        )

# Interactive button
button = tk.Button(
    root,
    text="LET'S GO! ✨",
    command=say_hello,
    font=("Segoe UI", 12, "bold"),
    bg="#7C3AED",
    fg="white",
    activebackground="#6D28D9",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=35,
    pady=12
)
button.pack(pady=5)

# Response message
message = tk.Label(
    root,
    text="",
    font=("Segoe UI", 12, "bold"),
    bg="#111827",
    fg="#34D399"
)
message.pack(pady=20)

# Press Enter to activate the app
root.bind("<Return>", lambda event: say_hello())

# Start the application
root.mainloop()
