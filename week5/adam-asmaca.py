import os
import random

from kelimeler_listesi import kelimeler
from adam import aşamalar, logo2, logo3


def clear():
    """Terminal ekranını temizler."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


secilen_kelime = random.choice(kelimeler)
kelime_uzunlugu = len(secilen_kelime)

oyun_bitti = False
hayat = 6

ekran = []
tahminler = []

print(logo3)
print("\nOyunu kazanmak istiyorsan asılmadan önce kelimeyi tahmin et 😂\n")

for _ in range(kelime_uzunlugu):
    ekran.append("_")


while not oyun_bitti:
    tahmin = input("Harf tahmin et: ").lower()
    clear()

    if tahmin in tahminler:
        print(f"{' '.join(ekran)}")
        print(aşamalar[hayat])
        print(f"Bu harfi daha önce tahmin ettin: '{tahmin}'. Farklı bir harf seç.")
        continue

    tahminler.append(tahmin)

    for yer in range(kelime_uzunlugu):
        harf = secilen_kelime[yer]

        if harf == tahmin:
            ekran[yer] = harf

    print(f"{' '.join(ekran)}")

    if tahmin not in secilen_kelime:
        hayat -= 1
        print(f"'{tahmin}' kelimenin içinde yok. Bir hayat kaybettin.")

    if "_" not in ekran:
        oyun_bitti = True
        print("\nVay be, kazandın! 🎉")
        print(logo2)

    elif hayat == 0:
        oyun_bitti = True
        print("Adam asıldı! Kaybettin 😅")
        print(f"\nKelime: '{secilen_kelime}'")

    else:
        print(aşamalar[hayat])
