import threading
import time

# Semaphore dengan maksimal 2 thread
printer = threading.Semaphore(2)

def print_dokumen(karyawan, halaman):
    """Simulasi print dokumen"""
    print(f"{karyawan} menunggu printer...")

    with printer:  # Tunggu sampai ada printer tersedia
        print(f"{karyawan} mulai print {halaman} halaman")
        time.sleep(halaman * 0.5)  # Simulasi waktu print
        print(f"{karyawan} selesai print")

# 5 karyawan ingin print
karyawan_list = [
    ("Ipal", 1),
    ("Ipul", 3),
    ("Yogi", 4),
    ("Yoga", 2),
    ("Udins", 1),
]

threads = []
for nama, halaman in karyawan_list:
    t = threading.Thread(target=print_dokumen, args=(nama, halaman))
    threads.append(t)
    t.start()

# Tunggu semua selesai
for t in threads:
    t.join()

print("\nSemua dokumen selesai dicetak!")