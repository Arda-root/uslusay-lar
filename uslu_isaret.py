import tkinter as tk
from tkinter import messagebox

class UsluSayiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Üslü Sayı İşaret Bulucu")
        self.root.geometry("420x350")
        self.root.resizable(False, False)

        self.soru_indeks = 0
        self.sorular = [
            {"id": "taban_pozitif", "metin": "1. Soru:\nTaban POZİTİF mi?"},
            {"id": "kuvvet_tek", "metin": "2. Soru:\nKuvvet TEK mi?"},
            {"id": "parantez_var", "metin": "3. Soru:\nParantez VAR mı?"},
            {"id": "kuvvet_disarida", "metin": "4. Soru:\nKuvvet parantezin DIŞINDA mı?"}
        ]

        self.label_soru = tk.Label(root, text="", font=("Arial", 14, "bold"), wraplength=380, justify="center")
        self.label_soru.pack(pady=30)

        self.frame_butonlar = tk.Frame(root)
        self.frame_butonlar.pack(pady=20)

        self.btn_evet = tk.Button(self.frame_butonlar, text="EVET", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=10, height=2, command=lambda: self.cevabi_isle(True))
        self.btn_evet.grid(row=0, column=0, padx=10)

        self.btn_hayir = tk.Button(self.frame_butonlar, text="HAYIR", font=("Arial", 12, "bold"), bg="#f44336", fg="white", width=10, height=2, command=lambda: self.cevabi_isle(False))
        self.btn_hayir.grid(row=0, column=1, padx=10)

        self.btn_sifirla = tk.Button(root, text="Baştan Başla", font=("Arial", 10), command=self.sifirla)
        self.btn_sifirla.pack(side="bottom", pady=15)

        self.soruyu_goster()

    def soruyu_goster(self):
        self.label_soru.config(text=self.sorular[self.soru_indeks]["metin"])

    def cevabi_isle(self, durum):
        mevcut_id = self.sorular[self.soru_indeks]["id"]

        if mevcut_id == "taban_pozitif":
            if durum:
                self.sonucu_goster("POZİTİF (+)", "Taban pozitif olduğu için üs ne olursa olsun sonuç pozitiftir.")
            else:
                self.soru_indeks = 1

        elif mevcut_id == "kuvvet_tek":
            if durum:
                self.sonucu_goster("NEGATİF (-)", "Taban negatif ve kuvvet tek olduğu için sonuç negatiftir.")
            else:
                self.soru_indeks = 2

        elif mevcut_id == "parantez_var":
            if not durum:
                self.sonucu_goster("NEGATİF (-)", "Parantez olmadığı için çift kuvvet eksiyi artı yapamaz, sonuç negatiftir.")
            else:
                self.soru_indeks = 3

        elif mevcut_id == "kuvvet_disarida":
            if durum:
                self.sonucu_goster("POZİTİF (+)", "Parantez var ve çift kuvvet dışarıda olduğu için sonuç pozitiftir.")
            else:
                self.sonucu_goster("NEGATİF (-)", "Kuvvet parantezin içinde kaldığı için eksiyi kapsamaz, sonuç negatiftir.")

        if self.soru_indeks < len(self.sorular):
            self.soruyu_goster()

    def sonucu_goster(self, isaret, aciklama):
        messagebox.showinfo("Sonuç", f"İşaret: {isaret}\n\nNedeni: {aciklama}")
        self.sifirla()

    def sifirla(self):
        self.soru_indeks = 0
        self.soruyu_goster()

if __name__ == "__main__":
    root = tk.Tk()
    app = UsluSayiApp(root)
    root.mainloop()
