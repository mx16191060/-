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
