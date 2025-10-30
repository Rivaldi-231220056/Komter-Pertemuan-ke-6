import threading
import time
import random

# Semaphore untuk membatasi koneksi database maksimal 3
db_semaphore = threading.Semaphore(3)

def akses_database(user_id):
    """Simulasi akses database dengan connection pool"""
    print(f"User-{user_id} menunggu koneksi database...")
    
    with db_semaphore:
        print(f"User-{user_id} tersambung! Eksekusi query...")
        
        # Simulasi waktu eksekusi query (1-2 detik)
        waktu_query = random.uniform(1, 2)
        time.sleep(waktu_query)
        
        print(f"User-{user_id} selesai. Waktu query: {waktu_query:.2f} detik")

def main():
    # Buat 6 user yang ingin mengakses database
    threads = []
    for i in range(1, 7):
        t = threading.Thread(target=akses_database, args=(i,))
        threads.append(t)
        t.start()
    
    # Tunggu semua thread selesai
    for t in threads:
        t.join()
    
    print("\nSemua user telah selesai mengakses database!")

if __name__ == "__main__":
    main()