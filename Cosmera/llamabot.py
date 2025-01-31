import ollama
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

def get_response(user_input):
    if user_input.strip() == "":
        return

    chat_history.insert(tk.END, f"You: {user_input}\n")

    # Define mood responses for specific emojis
    mood_responses = {
        "😀": "I'm glad you're feeling happy! 😊",
        "😢": "I'm sorry to hear you're feeling sad. It's okay to have tough days. 🌸",
        "😠": "Seems like you're angry. Take a deep breath and relax. 😌",
        "😌": "It seems like you're feeling peaceful. Stay calm and centered. 🌿",
        "😷": "Feeling under the weather? Don't forget to take care of yourself! 🧡",
    }

    # Check if the user input matches any mood emoji
    if user_input in mood_responses:
        bot_reply = mood_responses[user_input]
    else:
        # If no mood emoji, use the Ollama API to get a response
        try:
            # Using Ollama API to get response from Llama 2 model
            response = ollama.chat(model="llama2", messages=[{"role": "user", "content": user_input}])
            bot_reply = response['message']['content']
        except Exception as e:
            bot_reply = f"Error: {str(e)}"

    # Insert the response into the chat history
    chat_history.insert(tk.END, f"Cosmera: {bot_reply}\n\n")
    user_entry.delete(0, tk.END)
    chat_history.yview(tk.END)  # Auto-scroll

    return bot_reply  # Return bot reply for further use (like printing)


# Tkinter Setup
root = tk.Tk()
root.title("Cosllama - Women's Health Assistant")
root.geometry("500x600")

# Set the window icon
root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\shubh\OneDrive - Manipal Education (MENA) FZ LLC\Projects\Cosmera\icon.png"))

# Create chat history window
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Roboto Slab", 12, "bold"), bg="#f2e7dd", fg="#7f171f")
chat_history.pack(pady=20)

# Instructions for the user
instructions = ttk.Label(root, text="I'm all ears, just ask!", font=("Helvetica", 11, "bold"), foreground="#d56b01", background="#f2e7dd")
instructions.pack(pady=10)

# User input field
user_entry = ttk.Entry(root, width=50, font=("Helvetica", 14), background="#f0f0f0", foreground="#2b2b2b")
user_entry.pack(pady=10)

# Send button to trigger response
send_button = ttk.Button(root, text="Send 🦙", command=lambda: get_response(user_entry.get()), style="TButton")
send_button.pack(pady=10)

# Run the Tkinter loop
root.mainloop()
