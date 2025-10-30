import threading
import time
import random

class DiningPhilosophers:
    def __init__(self, num_philosophers=5):
        self.num_philosophers = num_philosophers
        # Buat lock untuk setiap garpu
        self.forks = [threading.Lock() for _ in range(num_philosophers)]
        # Lock untuk memastikan hanya satu filsuf yang mengambil garpu sekaligus
        self.table_lock = threading.Lock()
        
    def filosof(self, philosopher_id):
        """Simulasi perilaku filsuf dengan solusi lock ordering"""
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.num_philosophers
        
        for makan_ke in range(2):  # Setiap filsuf makan 2 kali
            # Fase berpikir
            print(f"Filsuf-{philosopher_id} sedang berpikir...")
            time.sleep(random.uniform(0.1, 0.3))
            
            # **SOLUSI: LOCK ORDERING - selalu ambil garpu dengan nomor lebih kecil dulu**
            first_fork = min(left_fork, right_fork)
            second_fork = max(left_fork, right_fork)
            
            # Ambil garpu pertama (yang nomornya lebih kecil)
            print(f"Filsuf-{philosopher_id} mencoba mengambil garpu {first_fork}")
            self.forks[first_fork].acquire()
            print(f"Filsuf-{philosopher_id} berhasil mengambil garpu {first_fork}")
            
            # Ambil garpu kedua (yang nomornya lebih besar)
            print(f"Filsuf-{philosopher_id} mencoba mengambil garpu {second_fork}")
            self.forks[second_fork].acquire()
            print(f"Filsuf-{philosopher_id} berhasil mengambil garpu {second_fork}")
            
            # Fase makan
            print(f"Filsuf-{philosopher_id} ✓✓✓ MAKAN untuk ke-{makan_ke + 1} kali")
            time.sleep(random.uniform(0.5, 1.0))
            
            # Lepas garpu (urutan tidak penting)
            self.forks[second_fork].release()
            print(f"Filsuf-{philosopher_id} melepaskan garpu {second_fork}")
            
            self.forks[first_fork].release()
            print(f"Filsuf-{philosopher_id} melepaskan garpu {first_fork}")
            
            print(f"Filsuf-{philosopher_id} selesai makan ke-{makan_ke + 1}\n")

def main():
    print("=" * 70)
    print("DINING PHILOSOPHERS PROBLEM")
    print("Solusi: Lock Ordering")
    print("=" * 70)
    print("Aturan: Selalu ambil garpu dengan nomor lebih kecil terlebih dahulu")
    print("=" * 70)
    
    dining_table = DiningPhilosophers(5)
    
    # Buat thread untuk setiap filsuf
    philosophers = []
    for i in range(5):
        philosopher = threading.Thread(target=dining_table.filosof, args=(i,))
        philosophers.append(philosopher)
        print(f"Filsuf-{i} telah duduk di meja")
    
    print("\n" + "="*30 + " MULAI " + "="*30)
    
    # Jalankan semua thread
    for philosopher in philosophers:
        philosopher.start()
    
    # Tunggu semua filsuf selesai
    for philosopher in philosophers:
        philosopher.join()
    
    print("="*50)
    print("SEMUA FILSUF TELAH SELESAI MAKAN!")
    print("Tidak terjadi deadlock berkat Lock Ordering")
    print("="*50)

if __name__ == "__main__":
    main()