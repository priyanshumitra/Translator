from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Function to translate text
def change(text="type", src="english", dest="Hindi"):
    try:
        trans = Translator()
        trans_result = trans.translate(text, src=src, dest=dest)
        translated_text = trans_result.text
        return translated_text
    except Exception as e:
        return "Error in Translation", str(e)

# Function to handle translation and display results in the GUI
def data():
    source_lang = comb_sor.get()
    dest_lang = comb_dest.get()
    source_text = sor_text.get(1.0, END).strip()

    if not source_text:
        dest_text.delete(1.0, END)
        dest_text.insert(END, "Please enter text to translate!")
        return

    translated_text = change(text=source_text, src=source_lang, dest=dest_lang)

    # Display translated text
    dest_text.delete(1.0, END)
    dest_text.insert(END, translated_text)

# Tkinter GUI Setup
root = Tk()
root.title("Translator")
root.geometry("500x750")
root.configure(bg='#765341')

# Heading Label
lab_text = Label(root, text="Translator", font=('Times New Roman', 40, 'bold'), fg='Black', bg='Brown')
lab_text.place(x=100, y=20, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

# Source Text Label
lab_text = Label(root, text="Source Text", font=('Times New Roman', 20, 'bold'), fg='Black', bg='#765341')
lab_text.place(x=100, y=90, height=20, width=300)

# Source Text Box
sor_text = Text(frame, font=('Times New Roman', 18), wrap=WORD, bd=2, relief=SOLID)
sor_text.place(x=10, y=120, height=150, width=480)

# Language List
list_text = list(LANGUAGES.values())

# Source Language Combobox
comb_sor = ttk.Combobox(frame, values=list_text, font=('Times New Roman', 14))
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("english")  # Default value

# Translate Button
button_change = Button(frame, text="Translate", relief=RAISED, font=('Times New Roman', 14), bg="orange", command=data)
button_change.place(x=180, y=300, height=40, width=120)

# Destination Language Combobox
comb_dest = ttk.Combobox(frame, values=list_text, font=('Times New Roman', 14))
comb_dest.place(x=340, y=300, height=40, width=150)
comb_dest.set("Hindi")  # Default value

# Destination Text Label
lab_text = Label(root, text="Destination Text", font=('Times New Roman', 20, 'bold'), fg='Black', bg='#765341')
lab_text.place(x=100, y=360, height=20, width=300)

# Destination Text Box
dest_text = Text(frame, font=('Times New Roman', 18), wrap=WORD, bd=2, relief=SOLID)
dest_text.place(x=10, y=400, height=150, width=480)

root.mainloop()



