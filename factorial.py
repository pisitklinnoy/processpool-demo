import concurrent.futures
import time
import math
import sys

# เพิ่มขีดจำกัดของจำนวนหลักของตัวเลขที่สามารถแปลงเป็นสตริงได้
sys.set_int_max_str_digits(100_000)

# ฟังก์ชันคำนวณแฟคทอเรียล
def compute_factorial(n):
    print(f"Computing factorial({n})")
    return math.factorial(n)

# จำนวนตัวเลขที่ต้องการคำนวณ
numbers = [10_000, 15_000, 20_000, 25_000]

if __name__ == "__main__":
    start_time = time.time()

    # ใช้ ProcessPoolExecutor เพื่อรันฟังก์ชันแบบขนาน
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(compute_factorial, numbers))

    end_time = time.time()

    print(f"Computed {len(results)} factorials")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
