import threading
import time

lock_P = threading.Lock()
lock_Q = threading.Lock()

def proses_dengan_trylock(name, lock1, lock2):
    """Try-lock pattern"""
    for percobaan in range(10):
        # Ambil lock 1 (blocking)
        lock1.acquire()
        print(f"{name}: Lock 1 didapat (percobaan {percobaan + 1})")
        
        # COBA ambil lock 2 (NON-BLOCKING)
        if lock2.acquire(blocking=False):
            print(f"{name}: Lock 2 juga didapat! SELESAI\n")
            time.sleep(0.1)
            lock2.release()
            lock1.release()
            return
        else:
            # Gagal! Lepas semua lock
            print(f"{name}: Lock 2 tidak tersedia, lepas lock 1\n")
            lock1.release()
            time.sleep(0.05)
    
    print(f"{name}: Gagal setelah 10 percobaan\n")

# Jalankan
t1 = threading.Thread(target=proses_dengan_trylock, args=("Thread-A", lock_P, lock_Q))
t2 = threading.Thread(target=proses_dengan_trylock, args=("Thread-B", lock_Q, lock_P))

t1.start()
t2.start()

t1.join()
t2.join()

print("Selesai! Try-lock mencegah deadlock")