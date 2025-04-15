import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Button, Label, Frame, Combobox
from googletrans import Translator

translator = Translator()

def translate():
    english_text = entry.get()
    lang_name = lang_combo.get()
    dest_code = language_map.get(lang_name)
    
    if english_text.strip() and dest_code:
        try:
            result = translator.translate(english_text, src='en', dest=dest_code)
            output_label.config(text=result.text)
        except Exception as e:
            output_label.config(text="Translation failed.")
    else:
        output_label.config(text="Please enter a word.")

# Clear input/output
def clear_fields():
    entry.delete(0, tk.END)
    output_label.config(text="")

# Copy translated text
def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_label.cget("text"))

# Language map
language_map = {
    "Urdu 🇵🇰": "ur",
    "German 🇩🇪": "de"
}

# Setup style/theme
style = Style("flatly")  
root = style.master
root.title("MultiLingualMate - English Translator")
root.geometry("550x300")
root.resizable(False, False)

# Header
Label(root, text="🌍 English to Urdu / German Translator", font=("Segoe UI", 16, "bold")).pack(pady=15)

# Entry
entry = Entry(root, width=50, font=("Segoe UI", 12))
entry.pack(pady=5)
entry.focus()

# Language selection
lang_combo = Combobox(root, values=list(language_map.keys()), font=("Segoe UI", 11), width=25)
lang_combo.set("Urdu 🇵🇰")
lang_combo.pack(pady=5)

# Buttons
btn_frame = Frame(root)
btn_frame.pack(pady=10)

Button(btn_frame, text="Translate", bootstyle="success", command=translate, width=15).grid(row=0, column=0, padx=5)
Button(btn_frame, text="Clear", bootstyle="warning", command=clear_fields, width=10).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Copy", bootstyle="info", command=copy_output, width=10).grid(row=0, column=2, padx=5)

# Output
output_label = Label(root, text="", font=("Segoe UI", 14), wraplength=450, justify="center", foreground="#2d3436")
output_label.pack(pady=15)

root.mainloop()