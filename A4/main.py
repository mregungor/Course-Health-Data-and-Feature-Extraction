import tkinter
from tkinter import *
import numpy as np
import tensorflow as tf
from tkinter import messagebox


model = tf.keras.models.load_model("model.keras")

def calculate_risk():
    gender = gender_var.get()
    age = age_var.get()

    try:
        age = int(age)
        if age < 0:
            messagebox.showerror("Hata", "Yaş 0'dan küçük olamaz.")
            return
    except ValueError:
        messagebox.showerror("Hata", "Lütfen bir sayı girin.")
        return

    symptoms_values = [symptom_var.get() for symptom_var in symptom_vars]
    age_values = [0, 0, 0, 0, 0]

    if int(age) < 10:
        age_values[0] = 1
    elif int(age) < 20:
        age_values[1] = 1
    elif int(age) < 25:
        age_values[2] = 1
    elif int(age) < 60:
        age_values[3] = 1
    else:
        age_values[4] = 1

    symptoms_values += age_values

    if gender == 1:
        symptoms_values += [0, 1]
    else:
        symptoms_values += [1, 0]

    severity_value = severity_var.get()
    if severity_value == 1:
        symptoms_values += [1, 0, 0]  # Mild
    elif severity_value == 2:
        symptoms_values += [0, 1, 0]  # Moderate
    else:
        symptoms_values += [0, 0, 1]  # None

    model.predict(np.array([symptoms_values]))
    result = model.predict(np.array([symptoms_values]))[0][0]
    formatted_result = "{:.2%}".format(result)
    messagebox.showinfo("Risk", "Astım hastalığına sahipseniz nefes alma zorluğu yaşamanızın ihtimali:" + formatted_result)


window = Tk()
window.geometry("550x600")
window.title("Asthma Risk Calculator")

label1 = Label(window, text="Cinsiyet", fg="blue")
label2 = Label(window, text="Yaş", fg="blue")
label3 = Label(window, text="Semptomları Seçin", fg="red")

gender_var = IntVar()
gender_var.set(-1)

age_var = StringVar()

r1 = Radiobutton(window, text="Erkek", value=1, variable=gender_var)
r2 = Radiobutton(window, text="Kadın", value=2, variable=gender_var)
t1 = Entry(window, textvariable=age_var)

symptoms = [
    "Yorgunluk",
    "Kuru Öksürük",
    "Boğaz Ağrısı",
    "Semptomsuzluk",
    "Ağrı",
    "Burun Tıkanıklığı",
    "Burun Akıntısı",
    "Deneyim Yok",
]

symptom_vars = [IntVar() for _ in range(len(symptoms))]

for i, symptom in enumerate(symptoms):
    Label(window, text=symptom, fg="blue").grid(row=i + 3, column=0, padx=0, pady=10)
    symptom_vars[i].set(-1)
    Radiobutton(window, text="Evet", value=1, variable=symptom_vars[i]).grid(
        row=i + 3, column=1
    )
    Radiobutton(window, text="Hayır", value=0, variable=symptom_vars[i]).grid(
        row=i + 3, column=2
    )

label4 = Label(window, text="Ciddiyet", fg="blue")
severity_var = IntVar()
severity_var.set(-1)
r3 = Radiobutton(window, text="Hafif", value=1, variable=severity_var)
r4 = Radiobutton(window, text="Orta", value=2, variable=severity_var)
r5 = Radiobutton(window, text="Ciddi Değil", value=3, variable=severity_var)

button1 = Button(window, text="Risk Hesapla", fg="red", command=calculate_risk)
button1.grid(row=len(symptoms) + 5, column=1, columnspan=2, pady=10)

label1.grid(row=0, column=0, padx=0, pady=10)
label2.grid(row=1, column=0, padx=0, pady=10)
label3.grid(row=2, column=0, padx=0, pady=10)

r1.grid(row=0, column=1)
r2.grid(row=0, column=2)
t1.grid(row=1, column=1)

label4.grid(row=len(symptoms) + 3, column=0, padx=0, pady=10)
r3.grid(row=len(symptoms) + 3, column=1)
r4.grid(row=len(symptoms) + 3, column=2)
r5.grid(row=len(symptoms) + 3, column=3)

window.mainloop()
