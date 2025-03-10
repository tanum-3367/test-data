import pandas as pd
import random
from datetime import datetime, timedelta

def generate_records(start, end):
    records = []
    lease_company_ids = ['001', '002', '003', '004']

    for i in range(start, end):
        record = {
            "fpls_car_id": i,
            "old_fpls_car_id": f"old_{i}",
            "itk_cmfactory_id": random.randint(1, 100), 
            "cm_cst_id": random.choice([random.randint(1, 100), '']),
            "cm_car_git initid": random.choice([random.randint(12282727, 12282730), '']),
            "cm_reservation_user_id": random.choice([random.randint(1, 5), '']),
            "cm_maintenance_user_id": random.choice([random.randint(1, 5), '']),
            "cm_reception_user_id": random.choice([random.randint(1, 5), '']),
            "cm_sales_user_id": random.choice([random.randint(1, 5), '']),
            "hjn_num": f"HJN{i:03d}",
            "lease_company_id": random.choice(lease_company_ids),
            "lease_start_dt": (datetime.now() - timedelta(days=random.randint(0, 1000))).date().isoformat(),
            "lease_end_dt": (datetime.now() + timedelta(days=random.randint(0, 1000))).date().isoformat(),
            "lease_kiyak_dt": None,
            "re_lease_flg": False,
            "contract_no1": f"CN1_{i}",
            "contract_no2": f"CN2_{i}",
            "mnt_jtak_mng_no": f"MNT_{i}",
            "cm_itak_mng_no": f"ITAK_{i}",
            "lease_kbn": f"LK_{i}",
            "charge_list": f"CL_{i}",
            "charge_rank": f"CR_{i}",
            "car_mng_no": f"CMN_{i}",
            "car_mng_tnt": f"TNT_{i}",
            "car_mng_tnt_zip": f"{10000 + i}",
            "car_mng_tnt_tel": f"090-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}",
            "car_mng_tnt_tel_hy": f"090-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "car_mng_tnt_fax": f"FAX_{i}",
            "car_mng_tnt_fax_hy": f"FAXH_{i}",
            "car_mng_tnt_email": f"tnt{i}@example.com",
            "car_mng_tnt_sms": f"SMS_{i}",
            "driver_name": f"Driver {i}",
            "driver_tel": f"080{random.randint(10000000, 99999999)}",
            "driver_tel_hy": f"080-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "driver_zip_code": f"{random.randint(10000, 99999)}",
            "driver_ads": f"Address {i}",
            "cst_jgs_nm": f"CSTJ_{i}",
            "cst_bsh_nm": f"CSTB_{i}",
            "cst_ads_cd": f"CADS_{i}",
            "cst_adscd_ads": f"ADSC_{i}",
            "cst_adscd_ika_ads": f"ADSI_{i}",
            "cst_ads": f"CST_Address_{i}",
            "cst_tel": f"070{random.randint(10000000, 99999999)}",
            "cst_tel_hy": f"070-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "cst_fax": f"CST_FAX_{i}",
            "cst_fax_hy": f"CST_FAXH_{i}",
            "cst_email": f"cst{i}@example.com",
            "cst_zip_code": f"{random.randint(10000, 99999)}",
            "gosya_num": f"GS_{i}",
            "car_number1": f"CNUM1_{i}",
            "car_number2": f"CNUM2_{i}",
            "car_number3": f"CNUM3_{i}",
            "car_number4": f"CNUM4_{i}",
            "car_type_name": f"Type_{i}",
            "shipper_name": f"Shipper_{i}",
            "running_range": random.randint(1000, 100000),
            "custom_parts_name": f"CustomParts_{i}",
            "car_grade": f"Grade_{i}",
            "dealer_name": f"Dealer_{i}",
            "jbsk_insurance_company": f"Insurance_{i}",
            "jbsk_agency": f"Agency_{i}",
            "jbsk_agency_tel": f"050-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "jbsk_agency_tel_hy": f"050-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "jbsk_charge": f"Charge_{i}",
            "special_info": f"Special info {i}",
            "weight_tax": f"WeightTax_{i}",
            "insurance_ex_contract": f"InsEx_{i}",
            "lease_company_nm": f"LeaseCompany_{i}",
            "lease_tnt_name": f"LeaseTnt_{i}",
            "lease_tnt_section": f"Section_{i}",
            "lease_tnt_tel": f"03-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}",
            "lease_tnt_tel_hy": f"03-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "lease_tnt_fax": f"LeaseFax_{i}",
            "lease_tnt_fax_hy": f"LeaseFaxHy_{i}",
            "lease_tnt_email": f"lease{i}@example.com",
            "upsys_updt_dt": (datetime.now() - timedelta(days=random.randint(0, 1000))).isoformat(),
            "del_flg": False,
            "rec_rgst_dt": datetime.now().isoformat(),
            "rec_updt_id": random.randint(1, 20),
            "rec_updt_dt": datetime.now().isoformat(),
            "fpls_flg": False,
            "car_specific_key": f"CSK_{i}",
            "drive_system": f"Drive_{i}",
            "mission": f"Mission_{i}",
            "rec_rgst_id": random.randint(1, 10),
            "upsys_key": f"UPSYS_{i}",
            "cst_id": random.randint(1, 100),
            "cst_id_kiyksk": random.randint(1, 100),
            "insourced_a_display_flg": True,
            "insourced_b_display_flg": True,
            "outsourced_a_display_flg": True,
            "outsourced_b_display_flg": True,
            "car_specific_key_chg_flg": False,
            "old_car_specific_key": f"OLD_CSK_{i}",
            "rec_updt_name": f"Updater_{i}"
        }
        records.append(record)
    return records

csv_filename = "tfpdh001_carinfo.csv"
num_records = 3300000
# num_records = 10

chunksize = 10000
# chunksize = 1


open(csv_filename, "w").close()

for start in range(1, num_records + 1, chunksize):
    end = min(start + chunksize, num_records + 1)
    records = generate_records(start, end)
    df = pd.DataFrame(records)
    # first time w, afer a
    mode = "w" if start == 1 else "a"
    header = False
    df.to_csv(csv_filename, index=False, mode=mode, header=header)
    print(f"From {start} to {end - 1}")
