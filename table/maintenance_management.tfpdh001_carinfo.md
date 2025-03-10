# maintenance_management.tfpdh001_carinfo

## Description

委託車両情報

## Columns

| Name | Type | Default | Nullable | Children | Parents | Comment |
| ---- | ---- | ------- | -------- | -------- | ------- | ------- |
| fpls_car_id | integer | nextval('maintenance_management.tfpdh001_carinfo_fpls_car_id_seq'::regclass) | false | [maintenance_factory.tfpdh005_carinfo_mntflg](maintenance_factory.tfpdh005_carinfo_mntflg.md) [maintenance_management.tfpdh004_carinfo_mntitem](maintenance_management.tfpdh004_carinfo_mntitem.md) [maintenance_management.tfpdh006_carinfo_itksk](maintenance_management.tfpdh006_carinfo_itksk.md) [maintenance_management.tfpdh013_carinfo_ins](maintenance_management.tfpdh013_carinfo_ins.md) [maintenance_management.tfpdh048_carinfo_send](maintenance_management.tfpdh048_carinfo_send.md) [process_management.tfpdh003_mntschedule](process_management.tfpdh003_mntschedule.md) [process_management.tfpdh003_mntschedule_part_1](process_management.tfpdh003_mntschedule_part_1.md) [process_management.tfpdh003_mntschedule_part_10](process_management.tfpdh003_mntschedule_part_10.md) [process_management.tfpdh003_mntschedule_part_2](process_management.tfpdh003_mntschedule_part_2.md) [process_management.tfpdh003_mntschedule_part_3](process_management.tfpdh003_mntschedule_part_3.md) [process_management.tfpdh003_mntschedule_part_4](process_management.tfpdh003_mntschedule_part_4.md) [process_management.tfpdh003_mntschedule_part_5](process_management.tfpdh003_mntschedule_part_5.md) [process_management.tfpdh003_mntschedule_part_6](process_management.tfpdh003_mntschedule_part_6.md) [process_management.tfpdh003_mntschedule_part_7](process_management.tfpdh003_mntschedule_part_7.md) [process_management.tfpdh003_mntschedule_part_8](process_management.tfpdh003_mntschedule_part_8.md) [process_management.tfpdh003_mntschedule_part_9](process_management.tfpdh003_mntschedule_part_9.md) |  | FPLS車両ID:FPLS独自発番(リース契約＋車両単位) |
| old_fpls_car_id | varchar |  | true |  |  | 旧FPLS車両ID |
| itk_cmfactory_id | integer |  | false | [maintenance_factory.tfpdh005_carinfo_mntflg](maintenance_factory.tfpdh005_carinfo_mntflg.md) [maintenance_management.tfpdh004_carinfo_mntitem](maintenance_management.tfpdh004_carinfo_mntitem.md) [maintenance_management.tfpdh006_carinfo_itksk](maintenance_management.tfpdh006_carinfo_itksk.md) [maintenance_management.tfpdh013_carinfo_ins](maintenance_management.tfpdh013_carinfo_ins.md) [maintenance_management.tfpdh048_carinfo_send](maintenance_management.tfpdh048_carinfo_send.md) [process_management.tfpdh003_mntschedule](process_management.tfpdh003_mntschedule.md) [process_management.tfpdh003_mntschedule_part_1](process_management.tfpdh003_mntschedule_part_1.md) [process_management.tfpdh003_mntschedule_part_10](process_management.tfpdh003_mntschedule_part_10.md) [process_management.tfpdh003_mntschedule_part_2](process_management.tfpdh003_mntschedule_part_2.md) [process_management.tfpdh003_mntschedule_part_3](process_management.tfpdh003_mntschedule_part_3.md) [process_management.tfpdh003_mntschedule_part_4](process_management.tfpdh003_mntschedule_part_4.md) [process_management.tfpdh003_mntschedule_part_5](process_management.tfpdh003_mntschedule_part_5.md) [process_management.tfpdh003_mntschedule_part_6](process_management.tfpdh003_mntschedule_part_6.md) [process_management.tfpdh003_mntschedule_part_7](process_management.tfpdh003_mntschedule_part_7.md) [process_management.tfpdh003_mntschedule_part_8](process_management.tfpdh003_mntschedule_part_8.md) [process_management.tfpdh003_mntschedule_part_9](process_management.tfpdh003_mntschedule_part_9.md) |  | 整備工場ID |
| cm_cst_id | integer |  | true |  |  | 整備会社顧客ID |
| cm_car_id | integer |  | true |  | [maintenance_management.tfpdh002_cmcarinfo](maintenance_management.tfpdh002_cmcarinfo.md) | 整備会社車両ID |
| cm_reservation_user_id | integer |  | true |  | [user_management.mfpdg012_user_master](user_management.mfpdg012_user_master.md) | 促進担当者ID |
| cm_maintenance_user_id | integer |  | true |  | [user_management.mfpdg012_user_master](user_management.mfpdg012_user_master.md) | 整備担当者ID |
| cm_reception_user_id | integer |  | true |  | [user_management.mfpdg012_user_master](user_management.mfpdg012_user_master.md) | 受付担当者ID |
| cm_sales_user_id | integer |  | true |  | [user_management.mfpdg012_user_master](user_management.mfpdg012_user_master.md) | 営業担当者 |
| hjn_num | varchar |  | true |  |  | 整備会社法人番号 |
| lease_company_id | varchar |  | true |  | [lease_management.mfpdh009_leasecompany](lease_management.mfpdh009_leasecompany.md) | リース会社ID |
| lease_start_dt | date |  | true |  |  | リース契約開始日 |
| lease_end_dt | date |  | true |  |  | リース契約終了日 |
| lease_kiyak_dt | date |  | true |  |  | リース契約解約日 |
| re_lease_flg | boolean | false | false |  |  | 再リースフラグ |
| contract_no1 | varchar |  | true |  |  | 契約番号_表示用 |
| contract_no2 | varchar |  | true |  |  | 契約番号_管理用 |
| mnt_jtak_mng_no | varchar |  | true |  |  | メンテ受託管理番号 |
| cm_itak_mng_no | varchar |  | true |  |  | 整備委託管理番号 |
| lease_kbn | varchar |  | true |  |  | リース区分 |
| charge_list | varchar |  | true |  |  | 適用料金表 |
| charge_rank | varchar |  | true |  |  | 料金ランク |
| car_mng_no | varchar |  | true |  |  | 車両管理番号 |
| car_mng_tnt | varchar |  | true |  |  | 車両管理担当者 |
| car_mng_tnt_zip | varchar |  | true |  |  | 車両管理担当者郵便番号 |
| car_mng_tnt_tel | varchar |  | true |  |  | 車両管理担当者TEL |
| car_mng_tnt_tel_hy | varchar |  | true |  |  | 車両管理担当者TEL_ハイフン付 |
| car_mng_tnt_fax | varchar |  | true |  |  | 車両管理担当者FAX |
| car_mng_tnt_fax_hy | varchar |  | true |  |  | 車両管理担当者FAX_ハイフン付 |
| car_mng_tnt_email | varchar |  | true |  |  | 車両管理担当者EMAIL |
| car_mng_tnt_sms | varchar |  | true |  |  | 車両管理担当者SMS |
| driver_name | varchar |  | true |  |  | ドライバー名 |
| driver_tel | varchar |  | true |  |  | ドライバーTEL |
| driver_tel_hy | varchar |  | true |  |  | ドライバーTEL_ハイフン付 |
| driver_zip_code | varchar |  | true |  |  | ドライバー郵便番号 |
| driver_ads | varchar |  | true |  |  | ドライバー連絡先住所 |
| cst_jgs_nm | varchar |  | true |  |  | 顧客事業所名 |
| cst_bsh_nm | varchar |  | true |  |  | 顧客部署名 |
| cst_ads_cd | varchar |  | true |  |  | 顧客住所コード |
| cst_adscd_ads | varchar |  | true |  |  | 顧客住所コード住所 |
| cst_adscd_ika_ads | varchar |  | true |  |  | 顧客住所コード以下住所 |
| cst_ads | varchar |  | true |  |  | 顧客住所 |
| cst_tel | varchar |  | true |  |  | 顧客TEL |
| cst_tel_hy | varchar |  | true |  |  | 顧客TEL_ハイフン付 |
| cst_fax | varchar |  | true |  |  | 顧客FAX |
| cst_fax_hy | varchar |  | true |  |  | 顧客FAX_ハイフン付 |
| cst_email | varchar |  | true |  |  | 顧客EMAIL |
| cst_zip_code | varchar |  | true |  |  | 顧客郵便番号 |
| gosya_num | varchar |  | true |  |  | 号車番号 |
| car_number1 | varchar |  | true |  |  | 登録番号_陸事名 |
| car_number2 | varchar |  | true |  |  | 登録番号_種別 |
| car_number3 | varchar |  | true |  |  | 登録番号_かな |
| car_number4 | varchar |  | true |  |  | 登録番号_番号 |
| car_type_name | varchar |  | true |  |  | 車種名 |
| shipper_name | varchar |  | true |  |  | 荷主名 |
| running_range | integer |  | true |  |  | 契約走行距離 |
| custom_parts_name | varchar |  | true |  |  | 架装部分名 |
| car_grade | varchar |  | true |  |  | 車両グレード |
| dealer_name | varchar |  | true |  |  | 納入ディーラー拠点名 |
| jbsk_insurance_company | varchar |  | true |  |  | 自賠責_損保会社 |
| jbsk_agency | varchar |  | true |  |  | 自賠責指定代理店 |
| jbsk_agency_tel | varchar |  | true |  |  | 代理店連絡先 |
| jbsk_agency_tel_hy | varchar |  | true |  |  | 代理店連絡先_ハイフン付 |
| jbsk_charge | varchar |  | true |  |  | 自賠責負担先 |
| special_info | varchar |  | true |  |  | リース会社特記事項 |
| weight_tax | varchar |  | true |  |  | 重量税負担先 |
| insurance_ex_contract | varchar |  | true |  |  | 保険免責負担特約 |
| lease_company_nm | varchar |  | true |  |  | リース契約会社名 |
| lease_tnt_name | varchar |  | true |  |  | リース会社担当者 |
| lease_tnt_section | varchar |  | true |  |  | リース会社担当部署 |
| lease_tnt_tel | varchar |  | true |  |  | リース会社担当TEL |
| lease_tnt_tel_hy | varchar |  | true |  |  | リース会社担当TEL_ハイフン付 |
| lease_tnt_fax | varchar |  | true |  |  | リース会社担当FAX |
| lease_tnt_fax_hy | varchar |  | true |  |  | リース会社担当FAX_ハイフン付 |
| lease_tnt_email | varchar |  | true |  |  | リース会社担当Email |
| upsys_updt_dt | timestamp with time zone |  | true |  |  | 上流システム更新日時 |
| del_flg | boolean | false | false |  |  | 削除フラグ |
| rec_rgst_dt | timestamp with time zone | CURRENT_TIMESTAMP | true |  |  | レコード作成日時 |
| rec_updt_id | integer |  | true |  | [user_management.mfpdg012_user_master](user_management.mfpdg012_user_master.md) | 最終更新者ID |
| rec_updt_dt | timestamp with time zone | CURRENT_TIMESTAMP | true |  |  | 最終更新日時 |
| fpls_flg | boolean | false | false |  |  | FPLS追加フラグ:ph2追加項目、当フラグが True の車両のみが更新対象 |
| car_specific_key | varchar |  | true |  |  | 車両特定キー |
| drive_system | varchar |  | true |  |  | 駆動方式:ph2.2追加 |
| mission | varchar |  | true |  |  | ミッション:ph2.2追加 |
| rec_rgst_id | integer |  | true |  | [user_management.mfpdg012_user_master](user_management.mfpdg012_user_master.md) | レコード作成者。Nullの場合はバッチからの更新。 |
| upsys_key | varchar |  | true |  |  | 上流システムキー |
| cst_id | integer |  | true |  |  | 顧客ID_使用先 |
| cst_id_kiyksk | integer |  | true |  |  | 顧客ID_契約先 |
| insourced_a_display_flg | boolean | true | false |  |  | 委託内_A項目表示フラグ |
| insourced_b_display_flg | boolean | true | false |  |  | 委託内_B項目表示フラグ |
| outsourced_a_display_flg | boolean | true | false |  |  | 委託外_A項目表示フラグ |
| outsourced_b_display_flg | boolean | true | false |  |  | 委託外_B項目表示フラグ |
| car_specific_key_chg_flg | boolean | false | false |  |  | 車両特定キー変更フラグ |
| old_car_specific_key | varchar |  | true |  |  | 旧車両特定キー |
| rec_updt_name | varchar |  | true |  |  | 最終更新者名 |

## Constraints

| Name | Type | Definition |
| ---- | ---- | ---------- |
| tfpdh001_carinfo_fk1 | FOREIGN KEY | FOREIGN KEY (lease_company_id) REFERENCES lease_management.mfpdh009_leasecompany(lease_company_id) |
| tfpdh001_carinfo_pkc | PRIMARY KEY | PRIMARY KEY (fpls_car_id, c) |
| tfpdh001_carinfo_fk2 | FOREIGN KEY | FOREIGN KEY (cm_car_id) REFERENCES maintenance_management.tfpdh002_cmcarinfo(cm_car_id) |
| tfpdh001_carinfo_fk3 | FOREIGN KEY | FOREIGN KEY (cm_reservation_user_id) REFERENCES user_management.mfpdg012_user_master(user_id) |
| tfpdh001_carinfo_fk4 | FOREIGN KEY | FOREIGN KEY (cm_maintenance_user_id) REFERENCES user_management.mfpdg012_user_master(user_id) |
| tfpdh001_carinfo_fk5 | FOREIGN KEY | FOREIGN KEY (cm_reception_user_id) REFERENCES user_management.mfpdg012_user_master(user_id) |
| tfpdh001_carinfo_fk6 | FOREIGN KEY | FOREIGN KEY (cm_sales_user_id) REFERENCES user_management.mfpdg012_user_master(user_id) |
| tfpdh001_carinfo_rec_rgst_id_fkey | FOREIGN KEY | FOREIGN KEY (rec_rgst_id) REFERENCES user_management.mfpdg012_user_master(user_id) |
| tfpdh001_carinfo_rec_updt_id_fkey | FOREIGN KEY | FOREIGN KEY (rec_updt_id) REFERENCES user_management.mfpdg012_user_master(user_id) |

## Indexes

| Name | Definition |
| ---- | ---------- |
| tfpdh001_carinfo_pkc | CREATE UNIQUE INDEX tfpdh001_carinfo_pkc ON maintenance_management.tfpdh001_carinfo USING btree (fpls_car_id, itk_cmfactory_id) |
| tfpdh001_carinfo_ix1 | CREATE INDEX tfpdh001_carinfo_ix1 ON maintenance_management.tfpdh001_carinfo USING btree (lease_company_id) |

## Relations

![er](maintenance_management.tfpdh001_carinfo.svg)

---

> Generated by [tbls](https://github.com/k1LoW/tbls)
