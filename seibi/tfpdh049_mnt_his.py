import time
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_records(start, end):
    records = []
    lease_company_ids = ['001', '002', '003', '004']
    factory_codes = ['FC001', 'FC002', 'FC003']
    tenken_categories = ['A', 'B', 'C']
    
    for i in range(start, end):
        record = {
            "mnt_his_id": f"MNT_{i:010d}",
            "factory_cd": random.choice(factory_codes),
            "mnt_mng_no": random.choice([random.randint(1, 5), '']),
            "contract_no1": random.choice([random.randint(1, 5), '']),
            "frame_number": random.choice([random.randint(1, 5), '']),
            "fpl_invoice_no": random.choice([random.randint(1, 5), '']),
            "lease_company_invoice_no": random.choice([random.randint(1, 5), '']),
            "tenken_kbn": random.choice(tenken_categories),
            "mnt_comp_date": (datetime.now() - timedelta(days=random.randint(0, 3650))).date().isoformat(),
            "mileage": random.randint(0, 200000) if random.random() > 0.2 else '',
            "lease_company_id": random.choice(lease_company_ids),
            "del_flg": False,
            "rec_rgst_dt": datetime.now().isoformat(),
            "rec_updt_id": random.randint(1, 10),
            "rec_updt_dt": datetime.now().isoformat(),
            "rec_rgst_id": random.randint(1, 10),
            "dok01": random.choice([random.randint(1, 5), '']),
            "dok02": random.choice([random.randint(1, 5), '']),
            "dok03": random.choice([random.randint(1, 5), '']),
            "dok04": random.choice([random.randint(1, 5), '']),
            "dok05": random.choice([random.randint(1, 5), '']),
            "dok06": random.choice([random.randint(1, 5), '']),
            "dok07": random.choice([random.randint(1, 5), '']),
            "car_specific_key": random.choice([random.randint(1, 5), '']),
            "mileage_before_exchange": random.choice([random.randint(1, 50), '']),
            "rec_updt_name": f"Updater_{random.randint(1, 100)}"
        }
        records.append(record)
    return records

csv_filename = "tfpdh049_mnt_his.csv"
num_records = 36000000
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
