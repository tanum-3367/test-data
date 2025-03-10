# maintenance_management.tfpdh002_cmcarinfo

## Description

整備会社車両情報:整備会社顧客情報：車両単位情報

## Columns

| Name | Type | Default | Nullable | Children | Parents | Comment |
| ---- | ---- | ------- | -------- | -------- | ------- | ------- |
| cm_car_id | integer | nextval('maintenance_management.tfpdh002_cmcarinfo_cm_car_id_seq'::regclass) | false | [maintenance_factory.tfpdh023_carinfo_syskey](maintenance_factory.tfpdh023_carinfo_syskey.md) [maintenance_management.tfpdh001_carinfo](maintenance_management.tfpdh001_carinfo.md) |  | 整備会社車両ID |
| hjn_num | varchar |  | true |  |  | 整備会社法人番号 |
| frame_number | varchar |  | true |  |  | 車台番号 |
| itaku_hist | boolean | false | false |  |  | 委託履歴 |
| itk_cmfactory_id | integer |  | false |  | [lease_management.ufpdh009_itk_cmfactory](lease_management.ufpdh009_itk_cmfactory.md) | 上流委託先工場ID |
| cm_cst_id | integer |  | true |  |  | 整備会社顧客ID |
| parking_id | integer |  | true |  | [maintenance_factory.tfpdh010_cmparking](maintenance_factory.tfpdh010_cmparking.md) | 駐車場ID |
| cst_id | integer |  | true |  |  | 顧客ID_使用先:リース会社から連携された顧客ID |
| lowsys_car_key | varchar |  | true |  |  | 連携システム車両キー:整備PKG移行データのキー格納を想定 |
| parking_position | varchar |  | true |  |  | 駐車場所:駐車場内における場所 |
| parking_memo | varchar |  | true |  |  | 駐車場メモ:Ph2で鍵関連項目に移行 |
| key_memo | varchar |  | true |  |  | 鍵関連メモ:未使用だったがPh2で論理名変更して採用。 |
| key_memo_2 | varchar |  | true |  |  | 鍵関連メモ_２ |
| rsv_mh | varchar |  | true |  |  | 予約方式 |
| aprch_mail | boolean | false | false |  |  | 促進方法_MAIL:※未使用：削除予定 |
| aprch_sms | boolean | false | false |  |  | 促進方法_SMS:※未使用：削除予定 |
| aprch_tel_office | boolean | false | false |  |  | 促進方法_会社TEL:※未使用：削除予定 |
| aprch_tel_mobile | boolean | false | false |  |  | 促進方法_携帯TEL:※未使用：削除予定 |
| aprch_fax | boolean | false | false |  |  | 促進方法_FAX:※未使用：削除予定 |
| aprch_dm | boolean | false | false |  |  | 促進方法_DM:※未使用：削除予定 |
| driver_aprch_flg | boolean | false | false |  |  | ドライバー促進フラグ:ドライバーが促進対象の場合はTrue |
| cmtntsh_aprch_flg | boolean | false | false |  |  | 車両管理担当者促進フラグ:車両管理担当者が促進対象の場合はTrue |
| aprch_memo | varchar |  | true |  |  | 促進メモ:※未使用：削除予定 |
| nyuk_mtd_schten | varchar |  | true |  |  | 入庫方法_スケ点:汎用コードマスタ（来店・納引・訪問） |
| nyuk_mtd_houten | varchar |  | true |  |  | 入庫方法_法定点検:汎用コードマスタ（来店・納引） |
| nyuk_mtd_syaken | varchar |  | true |  |  | 入庫方法_車検:汎用コードマスタ（来店・納引） |
| gosya_num | varchar |  | true |  |  | 号車番号 |
| intrvw_sht_flg | boolean | false | false |  |  | 問診票登録FLG:トリガーで更新 |
| memo_cst | varchar |  | true |  |  | 整備工場メモ |
| rec_rgst_dt | timestamp with time zone | CURRENT_TIMESTAMP | false |  |  | レコード作成日時 |
| rec_updt_dt | timestamp with time zone | CURRENT_TIMESTAMP | false |  |  | 最終更新日時 |
| rec_updt_id | integer |  | true |  | [user_management.mfpdg012_user_master](user_management.mfpdg012_user_master.md) | 最終更新者ID |
| car_number1 | varchar |  | true |  |  | 登録番号_陸事名:ph2追加項目 |
| car_number2 | varchar |  | true |  |  | 登録番号_種別:ph2追加項目 |
| car_number3 | varchar |  | true |  |  | 登録番号_かな:ph2追加項目 |
| car_number4 | varchar |  | true |  |  | 登録番号_番号:ph2追加項目 |
| old_car_number1 | varchar |  | true |  |  | 旧登録番号_陸事名 |
| old_car_number2 | varchar |  | true |  |  | 旧登録番号_種別 |
| old_car_number3 | varchar |  | true |  |  | 旧登録番号_かな |
| old_car_number4 | varchar |  | true |  |  | 旧登録番号_番号 |
| trok_kohu_dt | date |  | true |  |  | 登録交付年月日:ph2追加項目 |
| first_rgst_ym | varchar |  | true |  |  | 初度登録:ph2追加項目 |
| car_sybt_cd | varchar |  | true |  |  | 自動車の種別_コード:ph2追加項目 |
| car_sybt | varchar |  | true |  |  | 自動車の種別:ph2追加項目 |
| youto_cd | varchar |  | true |  |  | 用途_コード:ph2追加項目 |
| youto | varchar |  | true |  |  | 用途:ph2追加項目 |
| jiji_kbn_cd | varchar |  | true |  |  | 自事区分_コード:ph2追加項目 |
| jiji_kbn | varchar |  | true |  |  | 自事区分:ph2追加項目 |
| body_type_cd | varchar |  | true |  |  | 車体の形状_コード:ph2追加項目 |
| body_type | varchar |  | true |  |  | 車体の形状:ph2追加項目 |
| car_name_cd | varchar |  | true |  |  | 車名_コード:ph2追加項目 |
| riding_capacity1 | integer |  | true |  |  | 乗車定員1:ph2追加項目 |
| riding_capacity2 | integer |  | true |  |  | 乗車定員2:ph2追加項目 |
| riding_capacity3 | integer |  | true |  |  | 乗車定員3:ph2追加項目 |
| riding_capacity_kids_flg | boolean |  | true |  |  | 幼児定員フラグ:ph2追加項目 |
| riding_capacity_kids1 | integer |  | true |  |  | 幼児定員1:ph2追加項目 |
| riding_capacity_kids2 | integer |  | true |  |  | 幼児定員2:ph2追加項目 |
| loadage1 | bigint |  | true |  |  | 積載量1:ph2追加項目 |
| loadage2 | integer |  | true |  |  | 積載量2:ph2追加項目 |
| loadage3 | integer |  | true |  |  | 積載量3:ph2追加項目 |
| car_weight1 | integer |  | true |  |  | 車両重量1:ph2追加項目 |
| car_weight2 | integer |  | true |  |  | 車両重量2:ph2追加項目 |
| car_weight_all1 | bigint |  | true |  |  | 車両総重量1:ph2追加項目 |
| car_weight_all2 | integer |  | true |  |  | 車両総重量2:ph2追加項目 |
| car_weight_all3 | integer |  | true |  |  | 車両総重量3:ph2追加項目 |
| frame_number_2 | varchar |  | true |  |  | 車台番号_２:ph2追加項目、上にも同じ項目あり |
| car_length1 | integer |  | true |  |  | 全長1:ph2追加項目 |
| car_length2 | integer |  | true |  |  | 全長2:ph2追加項目 |
| car_width1 | integer |  | true |  |  | 全幅1:ph2追加項目 |
| car_width2 | integer |  | true |  |  | 全幅2:ph2追加項目 |
| car_height1 | integer |  | true |  |  | 全高1:ph2追加項目 |
| car_height2 | integer |  | true |  |  | 全高2:ph2追加項目 |
| jkjyu_f_f | integer |  | true |  |  | 前前軸重:ph2追加項目 |
| jkjyu_f_r | integer |  | true |  |  | 前後軸重:ph2追加項目 |
| jkjyu_r_f | integer |  | true |  |  | 後前軸重:ph2追加項目 |
| jkjyu_r_r | integer |  | true |  |  | 後後軸重:ph2追加項目 |
| car_model | varchar |  | true |  |  | 車種 |
| engine_type | varchar |  | true |  |  | エンジン型式（原動機の形式） |
| ventilation | numeric(10,2) |  | true |  |  | 排気量:ph2追加項目 |
| rotary_haikiryou | numeric(7,2) |  | true |  |  | ロータリー排気量:ph2追加項目 |
| rotor_num | integer |  | true |  |  | ロータ数:ph2追加項目 |
| unit | varchar |  | true |  |  | 総排気量又は定格出力_単位:ph2追加項目 |
| fuel_cd | varchar |  | true |  |  | 燃料_コード:ph2追加項目 |
| fuel | varchar |  | true |  |  | 燃料:ph2追加項目 |
| type_spec_number | varchar |  | true |  |  | 型式指定番号:ph2追加項目 |
| type_kbn_number | varchar |  | true |  |  | 種別区分番号:ph2追加項目 |
| syoyu_nm | varchar |  | true |  |  | 所有者名:ph2追加項目 |
| syoyu_kana | varchar |  | true |  |  | 所有者カナ:ph2追加項目 |
| syoyu_nm_cd | varchar |  | true |  |  | 所有者コード:ph2追加項目 |
| syoyu_ads | varchar |  | true |  |  | 所有者住所:ph2追加項目 |
| syoyu_ads_code_1 | varchar |  | true |  |  | 所有者住所コード都道府県市区群:ph2追加項目 |
| syoyu_ads_code_2 | varchar |  | true |  |  | 所有者住所コード町村:ph2追加項目 |
| syoyu_ads_code_3 | varchar |  | true |  |  | 所有者住所コード小字:ph2追加項目 |
| siyo_nm | varchar |  | true |  |  | 使用者名:ph2追加項目 |
| siyo_kana | varchar |  | true |  |  | 使用者カナ:ph2追加項目 |
| siyo_nm_cd | varchar |  | true |  |  | 使用者所有者コード:ph2追加項目 |
| siyo_ads | varchar |  | true |  |  | 使用者住所:ph2追加項目 |
| siyo_ads_code_1 | varchar |  | true |  |  | 使用者住所コード都道府県市区群:ph2追加項目 |
| siyo_ads_code_2 | varchar |  | true |  |  | 使用者住所コード町村:ph2追加項目 |
| siyo_ads_code_3 | varchar |  | true |  |  | 使用者住所コード小字:ph2追加項目 |
| siyo_honkyo | varchar |  | true |  |  | 使用本拠位置:ph2追加項目 |
| siyo_honkyo_ads_code_1 | varchar |  | true |  |  | 使用本拠位置住所コード都道府県市区群:ph2追加項目 |
| siyo_honkyo_ads_code_2 | varchar |  | true |  |  | 使用本拠位置住所コード町村:ph2追加項目 |
| siyo_honkyo_ads_code_3 | varchar |  | true |  |  | 使用本拠位置住所コード小字:ph2追加項目 |
| inspection_end_dt | date |  | true |  |  | 有効期間の満了する日:ph2追加項目 |
| running_range | integer |  | true |  |  | 走行距離:ph2追加項目 |
| running_range_date | date |  | true |  |  | 走行距離更新日時:ph2追加項目 |
| meter_exchange_flg | boolean |  | true |  |  | メーター交換有無:ph2追加項目 |
| meter_exchange_running_range | integer |  | true |  |  | メーター交換前走行距離 |
| meter_exchange_date | date |  | true |  |  | メーター交換日 |
| grade | varchar |  | true |  |  | グレード:ph2追加項目 |
| car_kbn | varchar |  | true |  |  | 車両区分:ph2追加項目 |
| kudo_houshiki | varchar |  | true |  |  | 駆動方式 |
| shift | varchar |  | true |  |  | ミッション |
| tire_size_s_f | varchar |  | true |  |  | タイヤサイズ夏（前）:ph2追加項目 |
| tire_size_s_r | varchar |  | true |  |  | タイヤサイズ夏（後）:ph2追加項目 |
| tire_size_w_f | varchar |  | true |  |  | タイヤサイズ冬（前）:ph2追加項目 |
| tire_size_w_r | varchar |  | true |  |  | タイヤサイズ冬（後）:ph2追加項目 |
| plug_num | integer |  | true |  |  | プラグ本数:ph2追加項目 |
| engine_oil_no_ele | numeric(7,2) |  | true |  |  | エンジンオイル量（エレメント交換なし）:ph2追加項目 |
| engine_oil_ele | numeric(7,2) |  | true |  |  | エンジンオイル量（エレメント交換あり）:ph2追加項目 |
| mission_oil | numeric(7,2) |  | true |  |  | ミッションオイル量:ph2追加項目 |
| front_def_oil | numeric(7,2) |  | true |  |  | フロントデフオイル量:ph2追加項目 |
| rear_def_oil | numeric(7,2) |  | true |  |  | リヤデフオイル量:ph2追加項目 |
| battery_size | varchar |  | true |  |  | バッテリーサイズ:ph2追加項目 |
| lease_motouke_id | varchar |  | true |  |  | リース元請ID:ph2追加項目 |
| tire_type | varchar |  | true |  |  | 現装着タイヤ:ph2追加項目 |
| body_color | varchar |  | true |  |  | ボディーカラー:ph2追加項目 |
| full_car_type | varchar |  | true |  |  | フル型式:ph2追加項目 |
| e_car_id | varchar |  | true |  |  | 電子車検証_車両ID |
| e_upload_dt | timestamp with time zone |  | true |  |  | 電子車検証取込日時 |
| car_memo_name_1 | varchar |  | true |  |  | 項目名１:ph2追加項目 |
| car_memo_1 | varchar |  | true |  |  | 車両メモ１:ph2追加項目 |
| car_memo_name_2 | varchar |  | true |  |  | 項目名２:ph2追加項目 |
| car_memo_2 | varchar |  | true |  |  | 車両メモ２:ph2追加項目 |
| car_memo_name_3 | varchar |  | true |  |  | 項目名３:ph2追加項目 |
| car_memo_3 | varchar |  | true |  |  | 車両メモ３:ph2追加項目 |
| car_memo_name_4 | varchar |  | true |  |  | 項目名４:ph2追加項目 |
| car_memo_4 | varchar |  | true |  |  | 車両メモ４:ph2追加項目 |
| car_memo_name_5 | varchar |  | true |  |  | 項目名５:ph2追加項目 |
| car_memo_5 | varchar |  | true |  |  | 車両メモ５:ph2追加項目 |
| car_memo_name_6 | varchar |  | true |  |  | 項目名６:ph2追加項目 |
| car_memo_6 | varchar |  | true |  |  | 車両メモ６:ph2追加項目 |
| car_memo_name_7 | varchar |  | true |  |  | 項目名７:ph2追加項目 |
| car_memo_7 | varchar |  | true |  |  | 車両メモ７:ph2追加項目 |
| car_memo_name_8 | varchar |  | true |  |  | 項目名８:ph2追加項目 |
| car_memo_8 | varchar |  | true |  |  | 車両メモ８:ph2追加項目 |
| car_memo_name_9 | varchar |  | true |  |  | 項目名９:ph2追加項目 |
| car_memo_9 | varchar |  | true |  |  | 車両メモ９:ph2追加項目 |
| car_memo_name_10 | varchar |  | true |  |  | 項目名１０:ph2追加項目 |
| car_memo_10 | varchar |  | true |  |  | 車両メモ１０:ph2追加項目 |
| car_memo_name_11 | varchar |  | true |  |  | 項目名１１:ph2追加項目 |
| car_memo_11 | varchar |  | true |  |  | 車両メモ１１:ph2追加項目 |
| car_memo_name_12 | varchar |  | true |  |  | 項目名１２:ph2追加項目 |
| car_memo_12 | varchar |  | true |  |  | 車両メモ１２:ph2追加項目 |
| car_memo_name_13 | varchar |  | true |  |  | 項目名１３:ph2追加項目 |
| car_memo_13 | varchar |  | true |  |  | 車両メモ１３:ph2追加項目 |
| car_memo_name_14 | varchar |  | true |  |  | 項目名１４:ph2追加項目 |
| car_memo_14 | varchar |  | true |  |  | 車両メモ１４:ph2追加項目 |
| car_memo_name_15 | varchar |  | true |  |  | 項目名１５:ph2追加項目 |
| car_memo_15 | varchar |  | true |  |  | 車両メモ１５:ph2追加項目 |
| car_memo_name_16 | varchar |  | true |  |  | 項目名１６:ph2追加項目 |
| car_memo_16 | varchar |  | true |  |  | 車両メモ１６:ph2追加項目 |
| car_memo_name_17 | varchar |  | true |  |  | 項目名１７:ph2追加項目 |
| car_memo_17 | varchar |  | true |  |  | 車両メモ１７:ph2追加項目 |
| car_memo_name_18 | varchar |  | true |  |  | 項目名１８:ph2追加項目 |
| car_memo_18 | varchar |  | true |  |  | 車両メモ１８:ph2追加項目 |
| car_memo_name_19 | varchar |  | true |  |  | 項目名１９:ph2追加項目 |
| car_memo_19 | varchar |  | true |  |  | 車両メモ１９:ph2追加項目 |
| car_memo_name_20 | varchar |  | true |  |  | 項目名２０:ph2追加項目 |
| car_memo_20 | varchar |  | true |  |  | 車両メモ２０:ph2追加項目 |
| contract_memo | varchar |  | true |  |  | 契約メモ:ph2追加項目 |
| car_id | integer |  | true |  |  | 車両特定ID:ph2追加項目 |
| input_expand_flg | boolean |  | true |  |  | 入力拡張フラグ:ph2追加項目 |
| rotary_flg | boolean |  | true |  |  | ロータリーフラグ:ph2追加項目 |
| old_running_range | integer |  | true |  |  | 旧走行距離:ph2追加項目 |
| old_running_range_date | date |  | true |  |  | 旧走行距離更新日時:ph2追加項目 |
| ins_memo | varchar |  | true |  |  | 車検証備考:ph2追加項目 |
| custom_parts_name | varchar |  | true |  |  | 架装部分名:ph2追加項目 |
| dealer_name | varchar |  | true |  |  | 納入ディーラー拠点名:ph2追加項目 |
| shipper_name | varchar |  | true |  |  | 荷主名:ph2追加項目 |
| car | varchar |  | true |  |  | 車名 |
| max_running_range | integer |  | true |  |  | 走行距離最大値:ph2追加項目 |
| max_running_range_date | date |  | true |  |  | 走行距離最大値更新日時:ph2追加項目 |
| cmc_consignor_cd | varchar |  | true |  |  | 整備会社委託元会社コード:ph2追加項目 |
| car_name_other | varchar |  | true |  |  | 車名_その他:ph2追加項目 |
| body_keijou_parts | varchar |  | true |  |  | 車体の形状_純正部品→ボディ形状_純正部品 |
| shashu_cd_parts | varchar |  | true |  |  | 車種コード_純正部品 |
| car_points | varchar |  | true |  | [invoice.mfpdh294_jaspamaint_sharyou](invoice.mfpdh294_jaspamaint_sharyou.md) | 車名_点数表 |
| kihon_katashiki_parts | varchar |  | true |  |  | 基本型式_純正部品 |
| car_model_points | varchar |  | true |  | [invoice.mfpdh294_jaspamaint_sharyou](invoice.mfpdh294_jaspamaint_sharyou.md) | 車両型式_点数表 |
| kudo_houshiki_parts | varchar |  | true |  |  | 駆動方式_純正部品:ph2追加項目 |
| end_month_parts | varchar |  | true |  |  | 終期_純正部品:ph2追加項目 |
| soubi_parts | varchar |  | true |  |  | 装備_純正部品:ph2追加項目 |
| engine_type_points | varchar |  | true |  | [invoice.mfpdh294_jaspamaint_sharyou](invoice.mfpdh294_jaspamaint_sharyou.md) | エンジン型式（原動機の形式）_点数表 |
| engine_katashiki_parts | varchar |  | true |  |  | エンジン型式（原動機の形式）_純正部品 |
| grade_parts | varchar |  | true |  |  | グレード_純正部品:ph2追加項目 |
| ventilation_parts | numeric(7,2) |  | true |  |  | 排気量_純正部品:ph2追加項目 |
| shift_parts | varchar |  | true |  |  | シフト_純正部品 |
| start_month_parts | varchar |  | true |  |  | 始期_純正部品:ph2追加項目 |
| del_flg | boolean | false | false |  |  | 削除フラグ |
| rec_rgst_id | integer |  | true |  | [user_management.mfpdg012_user_master](user_management.mfpdg012_user_master.md) | レコード作成者。Nullの場合はバッチからの更新。 |
| maker_cd_points | varchar |  | true |  | [invoice.mfpdh294_jaspamaint_sharyou](invoice.mfpdh294_jaspamaint_sharyou.md) | メーカーコード_点数表 |
| maker_cd_parts | varchar |  | true |  |  | メーカーコード_純正部品 |
| catalog_code_parts | varchar |  | true |  |  | カタログコード_純正部品 |
| sharyou_seq_parts | integer |  | true |  |  | 車両シーケンスNO |
| sharyou_no_parts | varchar |  | true |  |  | 車両番号_純正部品 |
| ins_type | varchar |  | true |  |  | 車検証種別 |
| rec_updt_name | varchar |  | true |  |  | 最終更新者名 |
| section_id | integer |  | true |  | [lease_management.mfpdh040_leasesection](lease_management.mfpdh040_leasesection.md) | 部署ID |
| car_type | varchar |  | true |  |  | 車両型式 |

## Constraints

| Name | Type | Definition |
| ---- | ---- | ---------- |
| tfpdh002_cmcarinfo_maker_cd_points_fkey | FOREIGN KEY | FOREIGN KEY (maker_cd_points, car_points, car_model_points, engine_type_points) REFERENCES invoice.mfpdh294_jaspamaint_sharyou(maker_cd, car, car_model, engine_type) |
| tfpdh002_cmcarinfo_fk3 | FOREIGN KEY | FOREIGN KEY (section_id) REFERENCES lease_management.mfpdh040_leasesection(section_id) |
| tfpdh002_cmcarinfo_fk1 | FOREIGN KEY | FOREIGN KEY (parking_id) REFERENCES maintenance_factory.tfpdh010_cmparking(parking_id) |
| tfpdh002_cmcarinfo_pkc | PRIMARY KEY | PRIMARY KEY (cm_car_id) |
| tfpdh002_cmcarinfo_rec_rgst_id_fkey | FOREIGN KEY | FOREIGN KEY (rec_rgst_id) REFERENCES user_management.mfpdg012_user_master(user_id) |
| tfpdh002_cmcarinfo_rec_updt_id_fkey | FOREIGN KEY | FOREIGN KEY (rec_updt_id) REFERENCES user_management.mfpdg012_user_master(user_id) |
| tfpdh002_cmcarinfo_fk2 | FOREIGN KEY | FOREIGN KEY (itk_cmfactory_id) REFERENCES lease_management.ufpdh009_itk_cmfactory(itk_cmfactory_id) |

## Indexes

| Name | Definition |
| ---- | ---------- |
| tfpdh002_cmcarinfo_pkc | CREATE UNIQUE INDEX tfpdh002_cmcarinfo_pkc ON maintenance_management.tfpdh002_cmcarinfo USING btree (cm_car_id) |
| fki_tfpdh002_cmcarinfo_fk1 | CREATE INDEX fki_tfpdh002_cmcarinfo_fk1 ON maintenance_management.tfpdh002_cmcarinfo USING btree (parking_id) |
| tfpdh002_cmcarinfo_ix1 | CREATE INDEX tfpdh002_cmcarinfo_ix1 ON maintenance_management.tfpdh002_cmcarinfo USING btree (hjn_num) |
| tfpdh002_cmcarinfo_ix2 | CREATE INDEX tfpdh002_cmcarinfo_ix2 ON maintenance_management.tfpdh002_cmcarinfo USING btree (cst_id) |

## Relations

![er](maintenance_management.tfpdh002_cmcarinfo.svg)

---

> Generated by [tbls](https://github.com/k1LoW/tbls)
