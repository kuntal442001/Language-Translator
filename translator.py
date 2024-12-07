from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

def translate_text():
    # Fetch source and target languages
    src_lang = combo_source.get()
    dest_lang = combo_target.get()
    text_to_translate = src_text.get("1.0", END).strip()

    if not text_to_translate:
        translated_text.delete("1.0", END)
        translated_text.insert(END, "Please enter text to translate.")
        return

    try:
        # Perform translation
        translator = GoogleTranslator(source=src_lang, target=dest_lang)
        result = translator.translate(text_to_translate)
        translated_text.delete("1.0", END)
        translated_text.insert(END, result)
    except Exception as e:
        translated_text.delete("1.0", END)
        translated_text.insert(END, f"Error: {e}")

# Create main window
app = Tk()
app.title("Language Translator")
app.geometry("600x500")
app.config(bg="#f2f2f2")

# Title Label
title_label = Label(app, text="Language Translator", font=("Arial", 20, "bold"), bg="#f2f2f2")
title_label.pack(pady=10)

# Source Text Area
src_label = Label(app, text="Source Text", font=("Arial", 12, "bold"), bg="#f2f2f2")
src_label.pack(pady=5)
src_text = Text(app, height=5, width=60, wrap=WORD, font=("Arial", 12))
src_text.pack(pady=5)

# Language Selection
translator_instance = GoogleTranslator()
languages = translator_instance.get_supported_languages()

frame = Frame(app, bg="#f2f2f2")
frame.pack(pady=10)

combo_source = ttk.Combobox(frame, values=languages, font=("Arial", 12), width=20)
combo_source.grid(row=0, column=0, padx=10)
combo_source.set("english")  # Default source language

combo_target = ttk.Combobox(frame, values=languages, font=("Arial", 12), width=20)
combo_target.grid(row=0, column=1, padx=10)
combo_target.set("spanish")  # Default target language

# Translate Button
translate_button = Button(app, text="Translate", font=("Arial", 14, "bold"), bg="#4caf50", fg="white", command=translate_text)
translate_button.pack(pady=10)

# Translated Text Area
trans_label = Label(app, text="Translated Text", font=("Arial", 12, "bold"), bg="#f2f2f2")
trans_label.pack(pady=5)
translated_text = Text(app, height=5, width=60, wrap=WORD, font=("Arial", 12))
translated_text.pack(pady=5)

# Run Application
app.mainloop()
