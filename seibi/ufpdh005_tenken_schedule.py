import time
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_records(start, end):
    records = []
    lease_company_ids = ['001', '002', '003', '004']
    tenken_categories = ['A', 'B', 'C']
    spt_cmfactory_ids = ['SPT001', 'SPT002', 'SPT003']
    
    for i in range(start, end):
        year = random.choice([2022, 2023])
        month = random.randint(1, 12)
        record = {
            "lease_company_id": random.choice(lease_company_ids),
            "upsys_key": f"SYS_{i:04d}",
            "tenken_ym": f"{year}{month:02d}",
            "tenken_kbn": random.choice(tenken_categories),
            "tenken_status": random.choice(["pending", "in_progress", "completed"]),
            "tenken_limit_dt": (datetime.now() + timedelta(days=random.randint(0, 90))).date().isoformat(),
            "tenken_mng_number": f"TMN_{i:05d}" if random.random() > 0.3 else None,
            "del_flg": False,
            "upsys_updt_dt": (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat(),
            "rec_rgst_dt": (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat(),
            "rec_updt_dt": (datetime.now() - timedelta(days=random.randint(0, 180))).isoformat(),
            "spt_cmfactory_id": random.choice(spt_cmfactory_ids),
            **{f"dok{j:02d}": f"DOK{j:02d}_{i}" for j in range(1, 11)},
            "rec_rgst_id": random.randint(1, 10),
            "rec_updt_id": random.randint(1, 10),
            "rec_updt_name": f"Updater_{random.randint(1, 100)}"
        }
        records.append(record)
    return records

csv_filename = "ufpdh005_tenken_schedule.csv"
num_records = 30000000
chunksize = 100000

start_time = time.time()

open(csv_filename, "w").close()

for start in range(1, num_records + 1, chunksize):
    end = min(start + chunksize, num_records + 1)
    records = generate_records(start, end)
    df = pd.DataFrame(records)
    mode = "w" if start == 1 else "a"
    header = False
    df.to_csv(csv_filename, index=False, mode=mode, header=header)
    print(f"From {start} to {end - 1}")

elapsed_time = time.time() - start_time
print(f"Data generation completed in {elapsed_time:.2f} seconds")
