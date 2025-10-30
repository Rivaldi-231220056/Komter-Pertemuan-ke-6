import threading
import time

rekening_A = threading.Lock()
rekening_B = threading.Lock()

def transfer_A_ke_B():
    """Transfer dari A ke B"""
    print("Transfer A->B: Mengunci rekening A...")
    with rekening_A:
        print("Transfer A->B: Rekening A terkunci!")
        time.sleep(0.5)
        
        print("Transfer A->B: Mencoba kunci rekening B...")
        with rekening_B:
            print("Transfer A->B: Berhasil!")

def transfer_B_ke_A():
    """Transfer dari B ke A"""
    print("Transfer B->A: Mengunci rekening B...")
    with rekening_B:
        print("Transfer B->A: Rekening B terkunci!")
        time.sleep(0.5)
        
        print("Transfer B->A: Mencoba kunci rekening A...")
        with rekening_A:
            print("Transfer B->A: Berhasil!")

# Jalankan
t1 = threading.Thread(target=transfer_A_ke_B)
t2 = threading.Thread(target=transfer_B_ke_A)

t1.start()
t2.start()

# Gunakan timeout untuk deteksi deadlock
t1.join(timeout=3)
t2.join(timeout=3)

if t1.is_alive() or t2.is_alive():
    print("\n*** DEADLOCK TERDETEKSI! ***")
    print("Thread 1 pegang Lock A, tunggu Lock B")
    print("Thread 2 pegang Lock B, tunggu Lock A")