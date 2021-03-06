import numpy as np
import pandas as pd

products = [
    'Amihan White Vinegar 1L (68)',
    'Amihan White Vinegar 2L (69)',
    'Amihan White Vinegar 4L (70)',
    'Amihan White Vinegar 350Ml (307)',
    'Amihan White Vinegar 385Ml (308)',
    'DATU PUTI Brewed Soysauce Less Sodium 265ml (314)',
    'DATU PUTI Magic 250ml (311)',
    'DATU PUTI Mansi 250ml (312)',
    'DATU PUTI Natural Cane Vinegar 265ml (313)',
    'Datu Puti Oysterrific Oyster Sauce 30g (262)',
    'Datu Puti Oysterrific Oyster Sauce 170g (263)',
    'Datu Puti Oysterrific Oyster Sauce 430g (276)',
    'DATU PUTI Pares Packs -VinSoy SACHET 60ml (278)',
    'Datu Puti Patis 15Ml (New) (88)',
    'Datu Puti Patis  60Ml (New) (89)',
    'Datu Puti Patis 150Ml (90)',
    'Datu Puti Patis 350Ml (Bot.) (91)',
    'Datu Puti Patis 350Ml (Pet) (92)',
    'Datu Puti Patis 1000Ml (93)',
    'Datu Puti Red Cane 1L (66)',
    'Datu Puti Red Cane 4L (67)',
    'Datu Puti Soy Sauce 1L PET (78)',
    'Datu Puti Soy Sauce 1L Sup (81)',
    'Datu Puti Soy Sauce  60Ml Sakto (72)',
    'Datu Puti Soy Sauce  100Ml Sup (73)',
    'Datu Puti Soy Sauce 200Ml (74)',
    'Datu Puti Soy Sauce 340ML (75)',
    'Datu Puti Soy Sauce 340Ml Refill Pack (76)',
    'Datu Puti Soy Sauce 385Ml Pet (77)',
    'Datu Puti Soy Sauce Gallon Pet (80)',
    'Datu Puti Soy Sauce Half Gallon Pet (79)',
    'Datu Puti Soy Sauce Sachet 20Ml (71)',
    'Datu Puti Spiced Vinegar 350Ml (64)',
    'Datu Puti Spiced Vinegar 750Ml (65)',
    'DATU PUTI Sugar Cane Vinegar 200ml (330)',
    'DATU PUTI Sugar Cane Vinegar 350ml (331)',
    'DATU PUTI  Sukang Iloko 250ml (328)',
    'DATU PUTI  Sukang Sinamak 250ml (327)',
    'DATU PUTI  Sukang Tagalog 250ml (329)',
    'DATU PUTI Toyo Chili 250ml (310)',
    'DATU PUTI Toyomansi 375ML (267)',
    'DATU PUTI Toyomansi 750ML (268)',
    'Datu Puti White Vinegar 1L (60)',
    'Datu Puti White Vinegar 1L Sup (63)',
    'Datu Puti White Vinegar 60Ml Sakto (54)',
    'Datu Puti White Vinegar 100Ml Sup (55)',
    'Datu Puti White Vinegar 200Ml (56)',
    'Datu Puti White Vinegar 350Ml Bot. (57)',
    'Datu Puti White Vinegar 350Ml Refill Pack (58)',
    'Datu Puti White Vinegar 385Ml Pet (59)',
    'Datu Puti White Vinegar Gallon Pet (62)',
    'Datu Puti White Vinegar Half Gallon Pet (61)',
    'Datu Puti White Vinegar Sachet 20Ml (53)',
    'Datu-Puti Adobo Series: Adobo Sa Gata 180ml (371)',
    'Datu-Puti Adobo Series: Humba 180ml (373)',
    'Datu-Puti Adobo Series: Pininyahang Adobo 180ml (372)',
    'Datu-Puti Adobo Series: Spicy Adobo 180ml (370)',
    'DATU-PUTI BBQ-RRIFIC BARBEQUE MARINADE 72ML (353)',
    'DATU-PUTI BBQ-RRIFIC BARBEQUE MARINADE 144ML (354)',
    'DATU-PUTI BBQ-RRIFIC BARBEQUE MARINADE 350ML (355)',
    'DatuPuti Oysterrific Oyster Sauce 70g (273)',
    'DP Pinoy Spice 375ml (257)',
    'Golden Fiesta Big Crunch Breading Mix 60g (334)',
    '\u200bGrande Barbeque Spag Pack (UFC SS 1KG+BBQ144ML+1 PASTA 800G)\u200b (413)',
    'Grande Chicken Spag Pack (UFC SS 1KG+GFBC60G+1 PASTA 800G) (414)',
    'Grande Spaghetti Catsup Pack (UFC SS 1KG + UFC BC 320G SUP + 1PASTA 800G) (412)',
    'Jufran Banana Catsup - Regular 4kg (404)',
    'Jufran Banana Catsup - Regular 320g (23)',
    'Jufran R-H Chili Sauce 100g (32)',
    'JUFRAN Sweet Chili Sauce 1kg SUP (240)',
    'JUFRAN Sweet Chili Sauce 90g (335)',
    'Jufran Sweet Chili Sauce 330g (36)',
    'Jufran Thai Fish Sauce 200Ml (98)',
    'Jufran Thai Fish Sauce 750Ml (99)',
    'LOCALLY JUICE DRINK CALAMANSI FLAVOR 350ML (401)',
    'LOCALLY JUICE DRINK DALANDAN FLAVOR 350ML (356)',
    'LOCALLY JUICE DRINK GUYABANO FLAVOR 350ML (400)',
    'LOCALLY JUICE DRINK MANGOSTEEN FLAVOR 350ML (359)',
    'LOCALLY JUICE DRINK POMELO FLAVOR 350ML (417)',
    'LOCALLY JUICE DRINK SINEGUELAS FLAVOR 350ML (418)',
    'LOCALLY JUICE DRINK TAMARIND FLAVOR 350ML (357)',
    'LOCALLY Juice \u200bin Can Calamansi Flavor 240ml (438)',
    'LOCALLY Juice \u200bin Can Dalandan Flavor 240ml (440)',
    '\u200b\u200bLOCALLY Juice \u200bin Can \u200b\u200bGuyabano Flavor 240ml\u200b (437)',
    '\u200b\u200bLOCALLY Juice \u200bin Can Pomelo Flavor 240ml (439)',
    'LOCALLY Juice \u200bin Can Tamarind Flavor 240ml (441)',
    'Mafran Banana Catsup Regular 1G (25)',
    'Mafran Banana Catsup Regular 320g (24)',
    'MANG TOMAS Extra Hot SIGA 325gm (332)',
    'Mang Tomas Lechon Sauce - Hot 325g (87)',
    'Mang Tomas Lechon Sauce - Regular 1kg-SUP (232)',
    'Mang Tomas Lechon Sauce - Regular 40g (83)',
    'Mang Tomas Lechon Sauce - Regular 100g (84)',
    'Mang Tomas Lechon Sauce - Regular 325g (85)',
    'Mang Tomas Lechon Sauce - Regular 550g (86)',
    'MERCI BUCO LOCALLY COCONUT WATER WITH LYCHEE 1L (425)',
    'MERCI BUCO LOCALLY COCONUT WATER WITH LYCHEE 330ML (426)',
    'MERCI BUCO LOCALLY COCONUT WATER WITH PANDAN 1L (423)',
    'MERCI BUCO LOCALLY COCONUT WATER WITH PANDAN 330ML (424)',
    'MERCI BUCO LOCALLY  PURE ORGANIC 1L (427)',
    'MERCI BUCO LOCALLY  PURE ORGANIC 330ML (428)',
    'Nelicom Pale Patis  1L New (96)',
    'Nelicom Pale Patis 350Ml (95)',
    'Nelicom Pale Patis Pet 4L New (97)',
    'Nelicom Pure Patis 750Ml (94)',
    'Papa Banana Catsup - Regular 1 kg (20)',
    'Papa Banana Catsup - Regular 4 kg (22)',
    'Papa Banana Catsup - Regular 100g (16)',
    'Papa Banana Catsup - Regular 200g (17)',
    'Papa Banana Catsup - Regular 320g (18)',
    'Papa Banana Catsup - Regular 550g (19)',
    'Papa Banana Catsup Baon Pack 25g (15)',
    'Papa Mini Spaghetti Pack (Papa Spaghetti Sauce 450g+ 350g pasta) (472)',
    'Papa Plus Banana Catsup Regular 2kg (21)',
    'PAPA SPAGHETTI PACK (397)',
    'SM Bonus Banana Catsup 320g (27)',
    'UFC Banana Catsup - Regular 1 kg (11)',
    'UFC Banana Catsup - Regular 2 kg (12)',
    'UFC Banana Catsup - Regular 4 kg (13)',
    'UFC Banana Catsup - Regular 10g (236)',
    'UFC Banana Catsup - Regular 320g (4)',
    'UFC Banana Catsup - Regular 550g (5)',
    'UFC Banana Catsup Baon Pack 25g (1)',
    'UFC Banana Catsup Budget Pack 100g (2)',
    "UFC Banana Catsup Saver's Pack 200g (3)",
    'UFC Banana Catsup Spouch 320g (14)',
    'UFC Golden Fiesta Canola Oil 1L (251)',
    'UFC Golden Fiesta Canola Oil 2L (252)',
    'UFC Golden Fiesta Cooking Oil 1L (248)',
    'UFC Golden Fiesta Cooking Oil 2L (249)',
    'UFC Golden Fiesta Cooking Oil 3.785L (250)',
    'UFC Golden Fiesta Cooking Oil 50ml (242)',
    'UFC Golden Fiesta Cooking Oil 100ml (243)',
    'UFC Golden Fiesta Cooking Oil 250ml (244)',
    'UFC Golden Fiesta Cooking Oil 485ml (245)',
    'UFC Golden Fiesta Cooking Oil 500ml (246)',
    'UFC Golden Fiesta Cooking Oil 950ml (247)',
    'UFC Golden Fiesta Corn Oil 1L (253)',
    'UFC Golden Fiesta Corn Oil 2L (254)',
    'UFC Golden Fiesta Soya Oil 1L (255)',
    'UFC Golden Fiesta Soya Oil 2L (256)',
    'UFC Hapi Fiesta Vegetable Oil 1L PET (271)',
    'UFC Hapi Fiesta Vegetable Oil 1L SUP (270)',
    'UFC Hapi Fiesta Vegetable Oil 2L SUP (272)',
    'UFC Hapi Fiesta Vegetable Oil 500Ml (316)',
    'UFC Hot Sauce 100g (33)',
    'UFC Ready Recipe Afritada 200g (51)',
    'UFC Ready Recipe Caldereta 200g (49)',
    'UFC READY RECIPE CALDERETA MIX 55G (321)',
    'UFC Ready Recipe Gata 40g (325)',
    'UFC Ready Recipe  Kare - Kare Mix  45g (323)',
    'UFC Ready Recipe Mechado 200g (48)',
    'UFC Ready Recipe Menudo 200g (47)',
    'UFC Ready Recipe Menudo /Afritada 50g (322)',
    'UFC READY RECIPE MIX CURRY 40G (320)',
    'UFC Sinigang sa Sampalok 20g (261)',
    'UFC Spagg Sauce w/ Real Cheese & Hotdog 250g (269)',
    'UFC Spagg Sauce w/ Real Cheese & Hotdog 500g (274)',
    'UFC Spaghetti Sauce 250g (43)',
    'UFC Spaghetti Sauce 500g (44)',
    'UFC Spaghetti Sauce 750g (45)',
    'UFC Spaghetti Sauce 1000g (46)',
    'UFC Sweet Chili Sauce 90g (35)',
    'UFC Sweet Chili Sauce 340g (34)',
    'UFC Tamis Anghang H&S 320g (26)',
    'UFC Tomato Sauce 115g (37)',
    'UFC Tomato Sauce 200g (38)',
    'UFC Tomato Sauce 1000g (39)',
    'UFC Tomato Sauce  - Guisado 1kg (42)',
    'UFC Tomato Sauce  - Guisado 115g (40)',
    'UFC Tomato Sauce  - Guisado 200g (41)',
    'Locally Juice In Can Pink Guava 240ml (514)',
    'Locally Juice In Can Ripe Mango 240ml (515)',
    'Locally Pink Guava 1L Tetra Pack',
    'Locally Ripe Mango 1L Tetra Pack (512)',
    'UFC Golden Fiesta Canola 1L SUP (553)']

nc_cols = ['NR', 'NC', 'NF', '-', -1]

info_cols = ['YEAR', 'MONTH', 'WEEK', 'AREA', 'GROUP', 'ACCOUNT', 'OUTLET']


def compute_osa(df):
    df_products = df[products].copy()
    not_carried_count = df_products.isin(nc_cols).sum(axis=1)
    total_carried_count = len(products) - not_carried_count

    # set non-numeric values to NaN
    df_products[df[products].isin(nc_cols)] = np.NaN

    # convert all entries to float
    df_products = df_products.astype(float)

    osa = (df_products.sum(axis=1).div(total_carried_count) / 7)

    df_osa = df[info_cols].copy()
    df_osa['OSA'] = osa

    return df_osa


def compute_osa_2(df):
    new_products = set(products).intersection(df.columns)
    df_products = df[new_products].copy()
    not_carried_count = df_products.isin(nc_cols).sum(axis=1)
    total_carried_count = len(products) - not_carried_count

    # set non-numeric values to NaN
    df_products[df[new_products].isin(nc_cols)] = np.NaN

    # convert all entries to float
    df_products = df_products.astype(float)

    osa = (df_products.sum(axis=1).div(total_carried_count) / 7)

    
    df['OSA'] = osa.values

    return df