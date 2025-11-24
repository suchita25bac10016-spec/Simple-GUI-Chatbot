import json
import tkinter as tk
from tkinter import scrolledtext
from difflib import get_close_matches

# Load responses.json with UTF-8 encoding
with open("responses.json", "r", encoding="utf-8") as f:
    responses = json.load(f)


def get_response(user_input):
    user_input = user_input.lower().strip()
    matches = get_close_matches(user_input, responses.keys(), n=1, cutoff=0.6)
    if matches:
        return responses[matches[0]]
    return "Sorry, I don't understand that."


def send_message():
    user_input = entry.get()
    if not user_input:
        return
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)

    if user_input.lower() in ["exit", "quit", "bye"]:
        chat_area.insert(tk.END, "Bot: Goodbye! 👋\n")
        root.after(2000, root.destroy)
        return

    response = get_response(user_input)
    chat_area.insert(tk.END, "Bot: " + response + "\n")


# GUI Setup
root = tk.Tk()
root.title("Simple Chatbot 🤖")

chat_area = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=50, height=20, state="normal")
chat_area.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
