import threading
import time

lock_X = threading.Lock()
lock_Y = threading.Lock()

def proses_dengan_timeout(name, lock1, lock2):
    """Coba ambil lock dengan timeout"""
    for percobaan in range(5):
        # Coba ambil lock 1
        if lock1.acquire(timeout=1):
            print(f"{name}: Lock 1 didapat (percobaan {percobaan + 1})")
            time.sleep(0.2)
            
            # Coba ambil lock 2 dengan timeout
            if lock2.acquire(timeout=1):
                print(f"{name}: Lock 2 didapat! SELESAI\n")
                lock2.release()
                lock1.release()
                return
            else:
                # Timeout! Lepas lock 1
                print(f"{name}: Timeout! Lepas lock 1, coba lagi\n")
                lock1.release()
                time.sleep(0.1)
        else:
            print(f"{name}: Timeout pada lock 1\n")
            time.sleep(0.1)
    
    print(f"{name}: Gagal setelah 5 percobaan\n")

# Jalankan
t1 = threading.Thread(target=proses_dengan_timeout, args=("Thread-1", lock_X, lock_Y))
t2 = threading.Thread(target=proses_dengan_timeout, args=("Thread-2", lock_Y, lock_X))

t1.start()
t2.start()

t1.join()
t2.join()

print("Selesai! Timeout mencegah deadlock permanent")