from customtkinter import *

def createWindow(name):
    app = CTk()
    app.geometry("500x400")

    set_default_color_theme("green")

    # CTkButton(master=app, text="Button").pack(pady=20, padx=20)
    # CTkCheckBox(master=app, text="Check box").pack(pady=20, padx=20)
    # CTkComboBox(master=app, values=["Option 1", "Option 2", "Option 3"]).pack(pady=20, padx=20)
    # CTkEntry(master=app, placeholder_text="Start typing...").pack(pady=20, padx=20)
    # CTkProgressBar(master=app).pack(pady=20, padx=20)
    # CTkRadioButton(master=app, text="Radio button").pack(pady=20, padx=20)
    # CTkSlider(master=app).pack(pady=20, padx=20)
    # CTkSwitch(master=app, text="Option").pack(pady=20, padx=20)
    myFont = CTkFont(family='Helvetica', size=44,weight ='bold')
    
    app.textbox = CTkTextbox(master=app, width=500,height=400, corner_radius=0,font=myFont)
    app.textbox.grid(row=0, column=0, sticky="nsew")
    app.textbox.insert("0.0", name)
    app.mainloop()

