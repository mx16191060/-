# 将数据转化为df格式,会方便数据清洗工作

['', '']<br>
2 2967527 557
['vin', 'back_legroom', 'bed', 'bed_height', 'bed_length', 'body_type', 'cabin', 'city', 'city_fuel_economy', 'combine_fuel_economy', 'daysonmarket', 'dealer_zip', 'engine_displacement', 'engine_type', 'exterior_color', 'fleet', 'frame_damaged', 'franchise_dealer', 'franchise_make', 'front_legroom', 'fuel_tank_volume', 'fuel_type', 'has_accidents', 'height', 'highway_fuel_economy', 'horsepower', 'interior_color', 'isCab', 'is_certified', 'is_cpo', 'is_new', 'is_oemcpo', 'latitude', 'length', 'listed_date', 'listing_color', 'listing_id', 'longitude', 'main_picture_url', 'major_options', 'make_name', 'maximum_seating', 'mileage', 'model_name', 'owner_count', 'power', 'price', 'salvage', 'savings_amount', 'seller_rating', 'sp_id', 'sp_name', 'theft_title', 'torque', 'transmission', 'transmission_display', 'trimId', 'trim_name', 'vehicle_damage_category', 'wheel_system', 'wheel_system_display', 'wheelbase', 'width', 'year']<br>
                       vin back_legroom bed bed_height bed_length        body_type<br>
0        ZACNJABB5KPJ92081      35.1 in                            SUV / Crossover<br>
1        SALCJ2FX1LH858117      38.1 in                            SUV / Crossover<br>
2        JF1VA2M67G9829723      35.4 in                                      Sedan<br>
3        SALRR2RV0L2433391      37.6 in                            SUV / Crossover<br>
4        SALCJ2FXXLH862327      38.1 in                            SUV / Crossover<br>
...                    ...          ...  ..        ...        ...              ...<br>
3000035  2GNAXJEV0J6261526      39.7 in                            SUV / Crossover<br>
3000036  1GNERFKW0LJ225508      38.4 in                            SUV / Crossover<br>
3000037  3FA6P0HD3GR134062      38.3 in                                      Sedan<br>
3000038  SAJAJ4BNXHA968809        35 in                                      Sedan<br>
3000039  JN8AT2MT1HW400805      37.9 in                            SUV / Crossover<br>

[3000040 rows x 6 columns]<br>
(3000040, 64)<br>
cost time: 74.69691133499146 76.83863496780396

# 转变为df格式之后,首先用info函数查看数据信息
 #   Column                   Dtype <br>
---  ------                   ----- <br>
 0   vin                      object<br>
 1   back_legroom             object<br>
 2   bed                      object<br>
 3   bed_height               object<br>
 4   bed_length               object<br>
 5   body_type                object<br>
 6   cabin                    object<br>
 7   city                     object<br>
 8   city_fuel_economy        object<br>
 9   combine_fuel_economy     object<br>
 10  daysonmarket             object<br>
 11  dealer_zip               object<br>
 12  engine_displacement      object<br>
 13  engine_type              object<br>
 14  exterior_color           object<br>
 15  fleet                    object<br>
 16  frame_damaged            object<br>
 17  franchise_dealer         object<br>
 18  franchise_make           object<br>
 19  front_legroom            object<br>
 20  fuel_tank_volume         object<br>
 21  fuel_type                object<br>
 22  has_accidents            object<br>
 23  height                   object<br>
 24  highway_fuel_economy     object<br>
 25  horsepower               object<br>
 26  interior_color           object<br>
 27  isCab                    object<br>
 28  is_certified             object<br>
 29  is_cpo                   object<br>
 30  is_new                   object<br>
 31  is_oemcpo                object<br>
 32  latitude                 object<br>
 33  length                   object<br>
 34  listed_date              object<br>
 35  listing_color            object<br>
 36  listing_id               object<br>
 37  longitude                object<br>
 38  main_picture_url         object<br>
 39  major_options            object<br>
 40  make_name                object<br>
 41  maximum_seating          object<br>
 42  mileage                  object<br>
 43  model_name               object<br>
 44  owner_count              object<br>
 45  power                    object<br>
 46  price                    object<br>
 47  salvage                  object<br>
 48  savings_amount           object<br>
 49  seller_rating            object<br>
 50  sp_id                    object<br>
 51  sp_name                  object<br>
 52  theft_title              object<br>
 53  torque                   object<br>
 54  transmission             object<br>
 55  transmission_display     object<br>
 56  trimId                   object<br>
 57  trim_name                object<br>
 58  vehicle_damage_category  object<br>
 59  wheel_system             object<br>
 60  wheel_system_display     object<br>
 61  wheelbase                object<br>
 62  width                    object<br>
 63  year                     object<br>
## 问题1
在处理数据的时候遇到一个问题是，明明某些列有很多是空的，但是在python里用dataframe.info统计出来并不是空的，就很奇怪，排查之后发现在我的excel表里这些数据看起来是空的值，但其实是一个空格。
但是用isnull判断是为False的
df.replace(to_replace=r'^\s*$',value=np.nan,regex=True,inplace=True)
