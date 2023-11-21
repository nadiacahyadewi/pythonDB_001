import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import messagebox

uiApp = tk.Tk()
uiApp.configure(background='Mediumpurple')
uiApp.geometry("500x500")
uiApp.resizable()
uiApp.title("Aplikasi prediksi Prodi Pilihan")

#make canvas
inputFrame = tk.Frame(uiApp)
inputFrame.pack(padx=10,fill="x", expand=True)


#make label
inputLabel = ttk.Label(inputFrame, text="Aplikasi prediksi Prodi Pilihan")
inputLabel.pack(padx=5, pady=10, fill="x", expand=True)

#membuat input nama 
labelInputNama = ttk.Label(inputFrame, text="Masukkan Nama Anda ")
labelInputNama.pack(padx=2, pady=1, fill="x", expand=True)

entryInputNama = ttk.Entry(inputFrame)
entryInputNama.pack(padx=2, pady=1, fill="x", expand=True)

#membuat input Nilai fisika
labelInputFisika = ttk.Label(inputFrame, text="Masukkan Nilai Fisika")
labelInputFisika.pack(padx=2, pady=1, fill="x", expand=True)

entryInputFisika= ttk.Entry(inputFrame)
entryInputFisika.pack(padx=2, pady=1, fill="x", expand=True)

#membuat input Nilai bahasa inggris
labelInputBing = ttk.Label(inputFrame, text="Masukkan Nilai Bahasa Inggris")
labelInputBing.pack(padx=2, pady=1, fill="x", expand=True)

entryInputBing = ttk.Entry(inputFrame)
entryInputBing.pack(padx=2, pady=1, fill="x", expand=True)

#membuat input Nilai Biologi
labelInputBiologi = ttk.Label(inputFrame, text="Masukkan Nilai Biologi")
labelInputBiologi.pack(padx=2, pady=1, fill="x", expand=True)

entryInputBiologi = ttk.Entry(inputFrame)
entryInputBiologi.pack(padx=2, pady=1, fill="x", expand=True)


#membuat button 
#membuat fungsi dialog
def klikButton():
    nama_siswa = entryInputNama.get()
    fisika = (entryInputFisika.get())
    inggris = (entryInputBing.get())
    biologi = (entryInputBiologi.get())


        # prediksi fakultas 
    if  biologi > fisika and biologi > inggris :
            prediksi_fakultas = "Kedokteran"
    elif fisika > biologi and fisika > inggris:
            prediksi_fakultas = "Teknik"
    elif inggris > biologi and inggris > fisika:
            prediksi_fakultas = "Bahasa"
    else:
            prediksi_fakultas = "Tidak dapat diprediksi"

    messagebox.showinfo("Hasil prediksi", f"\nHasil Prediksi Fakultas {prediksi_fakultas}!")

    # Save the data to SQLite database
    simpan_ke_database(nama_siswa, biologi, fisika, inggris, prediksi_fakultas)


def simpan_ke_database(nama_siswa, biologi, fisika, inggris, prediksi_fakultas):
    try:
        conn = sqlite3.connect("nilai_siswa.db")
        cursor = conn.cursor()

        # Membuat tabel jika belum ada
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS nilai_siswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_siswa TEXT,
                biologi INTEGER,
                fisika INTEGER,
                inggris INTEGER,
                prediksi_fakultas TEXT
            )
        ''')

        # Menyimpan data ke tabel
        cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
                       (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))

        conn.commit()
        conn.close()

        print("Data berhasil disimpan ke database.")
    except Exception as e:
        print(f"Error: {e}")

buttonSubmit = ttk.Button(inputFrame, text="CEK HASIL PREDIKSI", command=klikButton)
buttonSubmit.pack(padx=25, pady=30, fill="x", expand=True)
uiApp.mainloop()

