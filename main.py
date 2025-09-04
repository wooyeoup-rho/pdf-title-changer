import os, sys
from tkinter import *
from tkinterdnd2 import TkinterDnD, DND_FILES
from PyPDF2 import PdfReader, PdfWriter

# CONSTANTS
BACKGROUND = "#D9D9D9"
FONT = "Tahoma"

file_path = None

# ---------------------------- RESOURCE PATH ------------------------------- #
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# FUNCTIONS
def get_title(file_path):
    reader = PdfReader(file_path)
    metadata = reader.metadata
    current_title = metadata.get("/Title", "No title found")
    return current_title

def change_title(file_path, new_title):
    try:
        reader = PdfReader(file_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        metadata = reader.metadata
        metadata.update({"/Title": new_title})
        writer.add_metadata(metadata)

        new_path = file_path.replace(".pdf", "_updated.pdf")
        with open(new_path, "wb") as f:
            writer.write(f)

        result_label.config(text=f"Updated PDF saved as {new_path}")
    except Exception as e:
        result_label.config(text="Error. Not good. Very bad.")
        print(f"Exception:\t{e}")

def on_drop(event):
    global file_path
    file_path = event.data
    original_title_field.config(state="normal")
    original_title_field.delete(0, 'end')

    if os.path.isfile(file_path):
        original_title_field.insert(0, get_title(file_path))
        change_title_button.config(state="active")
    else:
        result_label.config(text="Invalid file")

    original_title_field.config(state="readonly")

def save_changes():
    new_title = new_pdf_field.get()
    change_title(file_path, new_title)

# UI
window = TkinterDnD.Tk()
window.title("PDF Title Converter")
window.config(padx=20, pady=20, bg=BACKGROUND)
window.minsize(420, 260)

window.rowconfigure(0, pad=50)
window.columnconfigure(0, pad=50)

icon_photo = PhotoImage(file=resource_path("assets/images/pdf.png"))
window.iconphoto(False, icon_photo)

target_photo = PhotoImage(file=resource_path("assets/images/target.png"))
canvas = Canvas(width=128, height=128, bg=BACKGROUND, highlightthickness=0)
canvas.create_image(0,0,anchor="nw", image=target_photo)
canvas.grid(row=1, column=0, rowspan=5)

app_label = Label(window, text="Drag and drop a PDF", font=(FONT, 12, "bold"), bg=BACKGROUND)
app_label.grid(row=0, column=0, columnspan=3)

result_label = Label(window, text="", font=(FONT, 8), bg=BACKGROUND, wraplength=360, justify='left')
result_label.grid(row=6, column=0, rowspan=2, columnspan=3, sticky="we", pady=(20,0))

original_title_label = Label(window, text="Original title: ", font=(FONT, 8), bg=BACKGROUND)
original_title_label.grid(row=1, column=1, sticky="w")

original_title_field = Entry(window, font=(FONT, 8), bg=BACKGROUND, state="readonly")
original_title_field.grid(row=1, column=2)

new_pdf_label = Label(window, text="New title: ", font=(FONT, 8), bg=BACKGROUND)
new_pdf_label.grid(row=2, column=1, sticky="w")

new_pdf_field = Entry(window, font=(FONT, 8), bg=BACKGROUND)
new_pdf_field.grid(row=2, column=2)

change_title_button = Button(window, text="Save", font=(FONT, 8), command=save_changes, width=10, state="disabled")
change_title_button.grid(row=4, column=2, columnspan=1)

window.drop_target_register(DND_FILES)
window.dnd_bind("<<Drop>>", on_drop)

window.mainloop()