



from sre_parse import SPECIAL_CHARS


aa = str(input())
"""
CPUs:
0. none:                       0 zł
1. i5 10400f:                730 zł
2. Ryzen 5 3600:             900 zł
3. Ryzen 5 5600x:           1300 zł
4. i5 11400:                 900 zł
5. i3 10100f:                370 zł
6. Ryzen 5 3400g:            800 zł
7. Ryzen 7 3700x:           1300 zł
8. i5 11600k:               1200 zł
9. Ryzen 5 1600af:           550 zł
10. i5 10600kf:              900 zł 
11. i7 10700kf:             1250 zł
12. Ryzen 7 5800x:          1900 zł
13. i5 10600k:               950 zł
14. i7 11700f:              1800 zł
15. Ryzen 9 5900x:          2750 zł
16. Ryzen 3 1200af:          330 zł
17. i5 11600kf:             1080 zł
18. i7 10700k:              1500 zł
19. Ryzen 7 3800x:          1350 zł
20. Ryzen 9 3900x:          2000 zł
GPUs:
0. none:                       0 zł
1. GTX 1660:                1900 zł
2. RTX 2060:                2400 zł
3. RTX 3070:                4400 zł
4. GT 1030:                  430 zł
5. GTX 1660 Ti:             1800 zł
6. GTX 1660 S:              1700 zł
7. RTX 3070 Ti:             4700 zł
8. RX 6700 XT:              4100 zł
9. RTX 3080:                5900 zł
10. RTX 3090:              10400 zł
11. RTX 3060:               3000 zł
12. GTX 1650 S:             1700 zł
13. RX 6800 XT:             6100 zł
14. RTX 3060 Ti:            3700 zł
15. RTX 3080 Ti:            7300 zł
16. RX 6900 XT:             9000 zł
17. RX 6800:                6000 zł
18. GTX 1650:               1400 zł
19. RX 6600 XT:             3000 zł
20. RX 6600:                2500 zł
Motherboards:
0. none:                       0 zł
1. MSI B450 Gaming plus:     330 zł
2. Gigabyte B560M DS3H:      410 zł
3. MSI Z490 Gaming plus:     750 zł
4. MSI B460M Pro-vdh:        330 zł
5. MSI B460M Pro:            300 zł
6. MSI Z490 A-pro:           680 zł
7. Gigabyte Z590 Gaming X:   760 zł
8. MSI B550 A-pro:           670 zł
9. MSI B450 Tomahawk:        350 zł
10. MSI B450 A-pro:          300 zł
11. Gigabyte B460M DS3H V2:  280 zł
12. MSI B550 Tomahawk:       660 zł
13. ASRock B560M pro4:       490 zł
14. ASRock B560 pro4:        570 zł
15. Gigabyte X570 A elite:   900 zł
16. Gigabyte B450 A elite:   350 zł
17. MSI B560M Bazooka:       520 zł
18. MSI Z590 A-pro:          830 zł
19. Gigabyte B450M DS3H:     260 zł
20. Gigabyte X570 Gaming X:  730 zł
RAM:
0. none:                       0 zł
1. 2x8GB 3200 Hyperx:        420 zł
2. 2x8GB 3600 Crucial:       450 zł
3. 2x8GB 3200 Hyperx RGB:    460 zł
4. 2x8GB 3600 Hyperx RGB:    460 zł
5. 1x16GB 3200 Goodram:      320 zł
6. 2x8GB 2666 Hyperx:        390 zł
7. 2x8GB 3200 Crucial:       410 zł
8. 1x8GB 3200 Goodram:       180 zł
9. 2x8GB 3200 Crucial RED:   420 zł
10. 2x8GB 3200 Viper 4 B:    410 zł
11. 2x16GB 3200 G.S Ripjaws: 740 zł
12. 2x8GB 2666 Goodram:      360 zł
13. 2x8GB 3200 G.S Aegis:    380 zł
14. 2x8GB 3200 Goodram:      400 zł
15. 2x8GB 3200 G.S Ripjaws:  400 zł
16. 2x8GB 3600 Corsair RGB:  530 zł
17. 2x8GB 3200 Adata D20:    420 zł
18. 2x4GB 3200 Viper 4 B:    240 zł
19. 2x16GB 3200 Hyperx RGB:  850 zł
20. 2x16GB 3200 Hyperx:      830 zł
Memory:
0. none:                       0 zł
1. Samsung 980 500GB:        300 zł
2. WD SN550 1TB:             470 zł
3. Goodram CX400 512GB:      230 zł
4. Crucial MX500 500GB:      260 zł
5. Samsung 980 1TB:          590 zł
6. Samsung 870 evo 500GB:    350 zł
7. Seagate Barracuda 2TB:    240 zł
8. Kioxia exceria 240GB:     140 zł
9. Crucial BX500 240GB:      150 zł
10. Samsung 870 evo 1TB:     500 zł
11. Gigabyte 512GB M.2:      270 zł
12. Kioxia Exceria 480GB:    220 zł
13. Goodram CX400 256GB:     140 zł
14. Kingston A2000 500GB:    250 zł
15. Kingston KC2500 500GB:   330 zł
16. Goodram CX400 1TB:       430 zł
17. Samsung 870 qvo 1TB:     450 zł
18. Samsung 970 evo 500GB:   420 zł
19. WD blue sata 500GB:      260 zł
20. Goodram CX400 128GB:      90 zł
PSUs:
0. none:                       0 zł
1. SPC Vero L3 600w:         250 zł
2. SPC Vero L3 500w:         200 zł
3. SPC Supremo FM2 750w:     450 zł
4. BeQuiet StrPow11 850w:    700 zł
5. SPC Vero M3 700w:         300 zł
6. SPC Supremo FM2 650w:     400 zł
7. Gigabyte P850GM 850w:     480 zł
8. SPC Supremo M2 550w:      300 zł
9. BeQuiet SysPow9 600w:     270 zł
10. BeQuiet PurPow11 600w:   400 zł
11. Chieftec smart 500w:     200 zł
12. SPC Supremo l2 650w:     360 zł
13. SPC Vero m3 600w:        270 zł
14. SPC Supremo l2 550w:     280 zł
15. BeQuiet SysPow9 700w:    330 zł
16. Corsair CV550 550w:      200 zł
17. BeQuiet StrPow11 750w:   600 zł
18. Corsair RM750x 750w:     540 zł
19. Corsair TX750M 750w:     400 zł
20. SPC Elementum e2 450w:   170 zł
Coolers:
0. none:                       0 zł
1. SPC Fera 5:               120 zł
2. SPC Fortis 3:             160 zł
3. SPC Fera 5 dual:          150 zł
4. SPC Spartan 4:             70 zł
5. BeQuiet Pure Rock 2:      170 zł
6. SPC Spartan 4 Max:         90 zł
7. BeQuiet Dark Rock 4:      280 zł
8. SPC Grandis 3:            200 zł
9. SPC Navis 240 RGB:        320 zł
10. BeQuiet Dark Rock Pro4:  360 zł
11. SPC Navis 240 ARGB:      380 zł
12. BeQuiet Pure Rock 2:     150 zł
13. SPC Fera 3 ARGB:         150 zł
14. SPC Fortis 3 ARGB:       190 zł
15. SPC Spartan 4 ARGB:       90 zł
16. MSI MAG Core LQ 240R:    520 zł
17. SPC Navis 360 ARGB:      500 zł
18. Scythe Mugen 5:          230 zł
19. SPC Grandis 3 ARGB:      250 zł
20. Arctic LF II 240:        370 zł
Cases:
0. none:                       0 zł
1. BeQuiet Pure Base 500DX:  400 zł
2. SPC Signum SG1 TG:        230 zł
3. SPC Regnum RG6V TG:       280 zł
4. BeQuiet Pure Base 500 W:  280 zł
5. SPC Regnum RG6V TG ARGB:  340 zł
6. SPC Signum SG1:           190 zł
7. BeQuiet Pure Base 500 c:  270 zł
8. SPC Signum SG1V TG ARGB:  310 zł
9. SPC Armis AR1:            140 zł
10. SPC Ventum VT4V TG ARGB: 300 zł 
11. MSI MAG Forge 101M:      300 zł
12. BeQuiet Pure Base 500 b: 300 zł
13. SPC Signum SG1X RGB:     330 zł
14. Krux Pallas:             220 zł
15. SPC Signum SG7V ARGB:    440 zł
16. SPC Ventum VT4V:         250 zł
17. SPC Armis AR6X ARGB:     400 zł
18. Krux Trek:               130 zł
19. Krux Mirror:             250 zł
20. Krux Leda:               280 zł
"""
if aa == "specs":
  r = int(input())
  s = int(input())
  if r == 1:
    class cpu:
        def __init__(self, cores, threads, ba_clock, bo_clock, l3, igpu, oc, price):
            self.cores = cores
            self.threads = threads
            self.ba_clock = ba_clock
            self.bo_clock = bo_clock 
            self.l3 = l3
            self.igpu = igpu
            self.oc = oc
            self.price = price
    i5_10400f = cpu(6, 12, 2900, 4300, 12, "none", "no", 730)
    r5_3600 = cpu(6, 12, 3600, 4200, 32, "none", "yes", 900)
    r5_5600x = cpu(6, 12, 3700, 4600, 35, "none", "yes", 1300)
    i5_11400 = cpu(6, 12, 2600, 4400, 12, 'uhd_730', 'no', 900)
    i3_10100f = cpu(4, 8, 3600, 4300, 6, 'none', 'no', 370)
    r5_3400g = cpu(4, 8, 3700, 4200, 6, 'vega_11', 'yes', 800)
    r7_3700x = cpu(8, 16, 3600, 4400, 32, 'none', 'yes', 1300)
    i5_11600k = cpu(6, 12, 3900, 4900, 12, 'uhd_750', 'yes', 1200)
    r5_1600af = cpu(6, 12, 3200, 3600, 19, 'none', 'yes', 550)
    i5_10600kf = cpu(6, 12, 4100, 4800, 12, 'none', 'yes', 900)
    i7_10700kf = cpu(8, 16, 3800, 5100, 16, 'none', 'yes', 1250)
    r7_5800x = cpu(8, 16, 3800, 4700, 32, 'none', 'yes', 1900)
    i5_10600k = cpu(6, 12, 4100, 4800, 12, 'uhd_630', 'yes', 950)
    i7_11700f = cpu(8, 16, 2500, 4900, 16, 'none', 'no', 1800)
    r9_5900x = cpu(12, 24, 3700, 4800, 70, 'none', 'yes', 2750)
    r3_1200af = cpu(4, 4, 3100, 3400, 8, 'none', 'yes', 330)
    i5_11600kf = cpu(6, 12, 3900, 4900, 12, 'none', 'yes', 1080)
    i7_10700k = cpu(8, 16, 3800, 5100, 16, 'uhd_630', 'yes', 1500)
    r7_3800x = cpu(8, 16, 3900, 4500, 36, 'none', 'yes', 1350)
    r9_3900x = cpu(12, 24, 3800, 4600, 70, 'none', 'yes', 2000)
    if s == 1:
        print(i5_10400f.cores)
    if s == 2:
        print(r5_3600.cores)
    if s == 3:
        print(r5_5600x.cores)
    if s == 4:
        print(i5_11400.cores)
    if s == 5:
        print(i3_10100f.cores)
    if s == 6:
        print(r5_3400g.cores)
    if s == 7:
        print(r7_3700x.cores)
    if s == 8:
        print(i5_11600k.cores)
    if s == 9:
        print(r5_1600af.cores)
    if s == 10:
        print(i5_10600kf.cores)
    if s == 11:
        print(i7_10700kf.cores)
    if s == 12:
        print(r7_5800x.cores)
    if s == 13:
        print(i5_10600k.cores)
    if s == 14:
        print(i7_11700f.cores)
    if s == 15:
        print(r9_5900x.cores)
    if s == 16:
        print(r3_1200af.cores)
    if s == 17:
        print(i5_11600kf.cores)
    if s == 18:
        print(i7_10700k.cores)
    if s == 19:
        print(r7_3800x.cores)
    if s == 20:
        print(r9_3900x.cores)
  if r == 2:
    class gpu:
        def __init__(self, cores, ba_clock, bo_clock, vram, v_speed, v_bus, tdp, price):
            self.cores = cores
            self.ba_clock = ba_clock
            self.bo_clock = bo_clock
            self.vram = vram
            self.v_speed = v_speed
            self.v_bus = v_bus
            self.tdp = tdp
            self.price = price
    gtx_1660 = gpu(1408, 1530, 1785, '6_gddr5', 8000, 192, '120w', 1900)
    rtx_2060 = gpu(1920, 1365, 1680, '6_gddr6', 14000, 192, '160w', 2400)
    rtx_3070 = gpu(5888, 1500, 1725, '8_gddr6', 14000, 256, '220w', 4400)
    gt_1030 = gpu(384, 1228, 1468, '2_gddr5', 6000, 64, '30w', 430)
    gtx_1660_ti = gpu(1536, 1500, 1770, '6_gddr6', 12000, 192, '120w', 1800)
    gtx_1660_s = gpu(1408, 1530, 1785, '6_gddr6', 14000, 192, '125w', 1700)
    rtx_3070_ti = gpu(6144, 1575, 1770, '8_gddr6x', 19000, 256, '290w', 4700)
    rx_6700_xt = gpu(2560, 2321, 2581, '12_gddr6', 16000, 192, '230w', 4100)
    rtx_3080 = gpu(8704, 1440, 1710, '10_gddr6x', 19000, 320, '320w', 5900)
    rtx_3090 = gpu(10496, 1395, 1695, '24_gddr6x', 19500, 384, '350w', 10400)
    rtx_3060 = gpu(3584, 1320, 1777, '12_gddr6', 15000, 192, '170w', 3000)
    gtx_1650_s = gpu(1280, 1530, 1725, '4_gddr6', 12000, 128, '100w', 1700)
    rx_6800_xt = gpu(4608, 1825, 2250, '16_gddr6', 16000, 256, '300w', 6100)
    rtx_3060_ti = gpu(4864, 1410, 1665, '8_gddr6', 14000, 256, '200w', 3700)
    rtx_3080_ti = gpu(10240, 1365, 1665, '12_gddr6x', 19000, 384, '350w', 7300)
    rx_6900_xt = gpu(5120, 1825, 2250, '16_gddr6', 16000, 256, '300w', 9000)
    rx_6800 = gpu(3840, 1700, 2105, '16_gddr6', 16000, 256, '250w', 6000)
    gtx_1650 = gpu(896, 1485, 1665, '4_gddr6', 12000, 128, '75w', 1400)
    rx_6600_xt = gpu(2048, 1968, 2589, '8_gddr6', 16000, 128, '160w', 3000)
    rx_6600 = gpu(1792, 1626, 2491, '8_gddr6', 16000, 128, '132w', 2500)
    if s == 1:
        print(gtx_1660.cores)
    if s == 2:
        print(rtx_2060.cores)
    if s == 3:
        print(rtx_3070.cores)
    if s == 4:
        print(gt_1030.cores)
    if s == 5:
        print(gtx_1660_ti.cores)
    if s == 6:
        print(gtx_1660_s.cores)
    if s == 7:
        print(rtx_3070_ti.cores)
    if s == 8:
        print(rx_6700_xt.cores)
    if s == 9:
        print(rtx_3080.cores)
    if s == 10:
        print(rtx_3090.cores)
    if s == 1:
        print(rtx_3060.cores)
    if s == 2:
        print(gtx_1650_s.cores)
    if s == 3:
        print(rx_6800_xt.cores)
    if s == 4:
        print(rtx_3060_ti.cores)
    if s == 5:
        print(rtx_3080_ti.cores)
    if s == 6:
        print(rx_6900_xt.cores)
    if s == 7:
        print(rx_6800.cores)
    if s == 8:
        print(gtx_1650.cores)
    if s == 9:
        print(rx_6600_xt.cores)
    if s == 10:
        print(rx_6600.cores)
  if r == 3:
    class mobo:
        def __init__(self, socket, chipset, ff, max_ram_s, max_ram_c, ram_s, pcie, price):
            self.socket = socket
            self.chipset = chipset
            self.ff = ff
            self.max_ram_s = max_ram_s
            self.max_ram_c = max_ram_c
            self.ram_s = ram_s
            self.pcie = pcie
            self.price = price
    b450_gaming_plus = mobo('am4', 'b450', 'ATX', '4133', 128, 4, '3.0', 330)
    b560m_ds3h = mobo('lga1200', 'b560', 'mATX', '5333', 128, 4, '3.0/4.0', 410)
    z490_gaming_plus = mobo('lga1200', 'z490', 'ATX', '4800', 128, 4, '3,0/4.0', 750)
    b460m_pro_vdh = mobo('lga1200', 'b460', 'mATX', '2666/2933', 128, 4, '3.0', 330)
    b460m_pro = mobo('lga1200', 'b460', 'mATX', '2666/2933', 128, 4, '3.0', 300)
    z490_a_pro = mobo('lga1200', 'z490', 'ATX', '4800', 128, 4, '3,0/4.0', 680)
    z590_gaming_x = mobo('lga1200', 'z590', 'ATX', '5000', 128, 4, '3.0/4.0', 760)
    b550_a_pro = mobo('am4', 'b550', 'ATX', "4400", 128, 4, '4.0', 670)
    b450_tomahawk = mobo('am4', 'b450', 'ATX', '4133', 128, 4, '3.0', 350)
    b450_a_pro = mobo('am4', 'b450', 'ATX', '4133', 128, 4, '3.0', 300)
    b460m_ds3h_v2 = mobo('lga1200', 'b460', 'mATX', '2666/2933', 128, 4, '3.0', 280)
    b550_tomahawk = mobo('am4', 'b550', 'ATX', '4600', 128, 4, '4.0', 660)
    b560m_pro4 = mobo('lga1200', 'b560', 'mATX', '4800', 128, 4, '3.0/4.0', 490)
    b560_pro4 = mobo('lga1200', 'b560', 'ATX', '4800', 128, 4, '3.0', 570)
    x570_a_elite = mobo('am4', 'x570', 'ATX', '4000', 128, 4, '4.0', 900)
    b450_a_elite = mobo('am4', 'b450', 'ATX', '3600', 128, 4, '3.0', 350)
    b560m_bazooka = mobo('lga1200', 'b560', 'mATX', '5066', 128, 4, '3.0/4.0', 520)
    z590_a_pro = mobo('lga1200', 'z590', 'ATX', '5333', 128, 4, '3.0/4.0', 830)
    b450m_ds3h = mobo('am4', 'b450', 'mATX', '3600', 128, 4, '3.0', 260)
    x570_gaming_x = mobo('am4', 'x570', 'mATX', '4000', 128, 4, '4.0', 730)
    if s == 1:
        print(b450_gaming_plus.socket)
    if s == 2:
        print(b560m_ds3h.socket)
    if s == 3:
        print(z490_gaming_plus.socket)
    if s == 4:
        print(b460m_pro_vdh.socket)
    if s == 5:
        print(b460m_pro.socket)
    if s == 6:
        print(z490_a_pro.socket)
    if s == 7:
        print(z590_gaming_x.socket)
    if s == 8:
        print(b550_a_pro.socket)
    if s == 9:
        print(b450_tomahawk.socket)
    if s == 10:
        print(b450_a_pro.socket)
    if s == 11:
        print(b460m_ds3h_v2.socket)
    if s == 12:
        print(b550_tomahawk.socket)
    if s == 13:
        print(b560m_pro4.socket)
    if s == 14:
        print(b560_pro4.socket)
    if s == 15:
        print(x570_a_elite.socket)
    if s == 16:
        print(b450_a_elite.socket)
    if s == 17:
        print(b560m_bazooka.socket)
    if s == 18:
        print(z590_a_pro.socket)
    if s == 19:
        print(b450m_ds3h.socket)
    if s == 20:
        print(x570_gaming_x.socket)
  if r == 4:
    class drive:
        def __init__(self, interface, capacity, r_speed, w_speed, pcie, mem_type, mtbf, price):
            self.interface = interface
            self.capacity = capacity
            self.r_speed = r_speed
            self.w_speed = w_speed
            self.pcie = pcie
            self.mem_type = mem_type
            self.mtbf = mtbf
            self.price = price
    samsung_980_500 = drive('m.2', '500gb', '3100mb/s', '2600mb/s', '3.0', 'TLC', '1500000', 300)
    wd_sn550_1000 = drive('m.2', '1tb', '2400mb/s', '1950mb/s', '3.0', 'TLC', '1700000', 470)
    goodram_cx400_512 = drive('sata', '512gb', '550mb/s', '500mb/s', '-', 'TLC', '2000000', 230)
    crucial_mx500_500 = drive('sata', '500gb', '560mb/s', '510mb/s', '-', 'TLC', '1800000', 260)
    samsung_980_1000 = drive('m.2', '1tb', '3500mb/s', '3000mb/s', '3.0', 'TLC', '1500000', 590)
    samsung_870_evo_500 = drive('sata', '500gb', '560mb/s', '530mb/s', '-', 'TLC', '1500000', 350)
    seagate_barracuda_2000 = drive('sata', '2tb', '7200obr/s', '-', '-', '-', '-', 240)
    kioxia_exceria_240 = drive('sata', '240gb', '555mb/s', '540mb/s', '-', 'TLC', '1500000', 140)
    crucial_bx500_240 = drive('sata', '240gb', '540mb/s', '500mb/s', '-', 'TLC', '1500000', 150)
    samsung_870_evo_1000 = drive('sata', '1tb', '560mb/s', '530mb/s', '-', 'TLC', '1500000', 500)
    gigabyte_m2_512 = drive('m.2', '512gb', '1700mb/s', '1550mb/s', '3.0', 'TLC', '1500000', 270)
    kioxia_exceria_480 = drive('sata', '480gb', '555mb/s', '540mb/s', '-', 'TLC', '1500000', 220)
    goodram_cx400_256 = drive('sata', '256gb', '550mb/s', '480gb', '-', 'TLC', '2000000', 140)
    kingston_a2000_500 = drive('m.2', '500gb', '2200mb/s', '2000mb/s', '3.0', 'TLC', '2000000', 250)
    kingston_kc2500_500 = drive('m.2', '500gb', '3500mb/s', '2500mb/s', '3.0', 'TLC', '2000000', 330)
    goodram_cx400_1000 = drive('sata', '1tb', '550mb/s', '500mb/s', '-', 'TLC', '2000000', 430)
    samsung_870_qvo_1000 = drive('sata', '1tb', '560mb/s', '530mb/s', '-', 'TLC', '1500000', 450)
    samsung_970_evo_500 = drive('m.2', '500gb', '3400mb/s', '2500mb/s', '3.0', 'TLC', '1500000', 420)
    WD_blue_500 = drive('sata', '500gb', '560mb/s', '530mb/s', '-', 'TLC', '1750000', 260)
    goodram_cx400_128 = drive('sata', '128gb', '550mb/s', '460mb/s', '-', 'TLC', '2000000', 90)
    if s == 1:
      print(samsung_980_500.capacity)
    if s == 2:
      print(wd_sn550_1000.capacity)
    if s == 3:
      print(goodram_cx400_512.capacity)
    if s == 4:
      print(crucial_mx500_500.capacity) 
    if s == 5:
      print(samsung_980_1000.capacity)
    if s == 6:
      print(samsung_870_evo_500.capacity)
    if s == 7:
      print(seagate_barracuda_2000.capacity)
    if s == 8:
      print(kioxia_exceria_240.capacity)
    if s == 9:
      print(crucial_bx500_240.capacity)
    if s == 10:
      print(samsung_870_evo_1000.capacity)
    if s == 11:
        print(gigabyte_m2_512.capacity)
    if s == 12:
        print(kioxia_exceria_480.capacity)
    if s == 13:
        print(goodram_cx400_256.capacity)
    if s == 14:
        print(kingston_a2000_500.capacity)
    if s == 15:
        print(kingston_kc2500_500.capacity)
    if s == 16:
        print(goodram_cx400_1000.capacity)
    if s == 17:
        print(samsung_870_qvo_1000.capacity)
    if s == 18:
        print(samsung_970_evo_500.capacity)
    if s == 19:
        print(WD_blue_500.capacity)
    if s == 20:
        print(goodram_cx400_128.capacity)
  if r == 5:
    class psu:
        def __init__(self, power, size, efficiency, certificate, modular, dimensions, price):
            self.power = power
            self.size = size
            self.efficiency = efficiency
            self.certificate = certificate
            self.modular = modular
            self.dimensions = dimensions
            self.price = price
    spc_vero_l3_600 = psu('600w', 'ATX', '89%', '80+ bronze', 'no', '86x150x140', 250)
    spc_vero_l3_500 = psu('500w', 'ATX', '89%', '80+ bronze', 'no', '86x150x140', 200)
    spc_supremo_fm2_750 = psu('750w', 'ATX', '88-92%', '80+ gold', 'full', '87x150x160', 450)
    bequiet_strpow11_850 = psu('850w', 'ATX', '91-93%', '80+ gold', 'full', '86x150x170', 700)
    spc_vero_m3_700 = psu('700w', 'ATX', '89%', '80+ bronze', 'semi', '86x150x160', 300)
    spc_supremo_fm2_650 = psu('650w', 'ATX', '92%', '80+ gold', 'full', '86x150x160', 400)
    gigabyte_p850gm_850 = psu('850w', 'ATX', '90%', '80+ gold', 'full', '86x150x140', 480)
    spc_supremo_m2_550 = psu('550w', 'ATX', '91%', '80= gold', 'semi', '86x150x163', 300)
    bequiet_syspow9_600 = psu('600w', 'ATX', '86-89%', '80+ bronze', 'no', '86x150x140', 270)
    bequiet_purpow11_600 = psu('600w', 'ATX', '92%', '80+ gold', 'no', '86x150x150', 400)
    chieftec_smart_500 = psu('500w', 'ATX', '80%', '80+', 'no', '87x150x140', 200)
    spc_supremo_l2_650 = psu('650w', 'ATX', '92%', '80+ gold', 'no', '86x150x161', 360)
    spc_vero_m3_600 = psu('600w', 'ATX', '89%', '80+ bronze', 'semi', '86x150x160', 270)
    spc_supremo_l2_550 = psu('550w', 'ATX', '91%', '80+ gold', 'no', '86x150x160', 280)
    bequiet_syspow9_700 = psu('700w', 'ATX', '86-89%', '80+ bronze', 'no', '86x150x140', 330)
    corsair_cv550_550 = psu('550w', 'ATX', '82-88%', '80+ bronze', 'no', '86x150x125', 200)
    bequiet_strpow11_750 = psu('750w', 'ATX', '92-94%', '80+ gold', 'full', '86x150x170', 600)
    corsair_rm750x_750 = psu('750w', 'ATX', '-', '80+ gold', 'full', '86x150x180', 540)
    corsair_tx750m_750 = psu('750w', 'ATX', '91-93%', '80= gold', 'semi', '86x150x140', 400)
    spc_elementum_e2_450 = psu('450w', 'ATX', '-', '80+', 'no', '86x150x140', 170)
    if s == 1:
      print(spc_vero_l3_600.power)
    if s == 2:
      print(spc_vero_l3_500.power)
    if s == 3:
      print(spc_supremo_fm2_750.power)
    if s == 4:
      print(bequiet_strpow11_850.power) 
    if s == 5:
      print(spc_vero_m3_700.power)
    if s == 6:
      print(spc_supremo_fm2_650.power)
    if s == 7:
      print(gigabyte_p850gm_850.power)
    if s == 8:
      print(spc_supremo_m2_550.power)
    if s == 9:
      print(bequiet_syspow9_600.power)
    if s == 10:
      print(bequiet_purpow11_600.power)
    if s == 11:
        print(chieftec_smart_500.power)
    if s == 12:
        print(spc_supremo_l2_650.power)
    if s == 13:
        print(spc_vero_m3_600.power)
    if s == 14:
        print(spc_supremo_l2_550.power)
    if s == 15:
        print(bequiet_syspow9_700.power)
    if s == 16:
        print(corsair_cv550_550.power)
    if s == 17:
        print(bequiet_strpow11_750.power)
    if s == 18:
        print(corsair_rm750x_750.power)
    if s == 19:
        print(corsair_tx750m_750.power)
    if s == 20:
        print(spc_elementum_e2_450.power)
  if r == 6:
    class cooler:
        def __init__(self, dimensions, fans, heatpipes, MTBF, TDP, price):
            self.dimensions = dimensions
            self.fans = fans
            self.heatpipes = heatpipes
            self.MTBF = MTBF
            self.TDP = TDP
            self.price = price
    spc_fera_5 = cooler('155x127x77', '1x120', '4x6', '100000', '220w', 120)
    spc_fortis_3 = cooler('158x125x140', '1x140', '5x6', '50000', '220w', 150)
    spc_fera_5_dual = cooler('155x127x102', '2x120', '4x6', '100000', '220w', 160)
    spc_spartan_4 = cooler('134x106x78', '1x100', '2x6', '50000', '125w', 70)
    bequiet_pr_2_b = cooler('155x121x88', '1x120', '4x6', '80000', '150w', 170)
    spc_spartan_4max = cooler('143x124x71', '1x120', '3x6', '50000', '125w', 90)
    bequiet_dr_4 = cooler('159x136x96', '1x135', '6x6', '300000', '200w', 280)
    spc_grandis_3 = cooler('159x140x131', '1x120 1x140', '6x6', '50000', '250w', 200)
    spc_navis_240_rgb = cooler('45x75x75', '2x120', '-', '50000', '350w', 320)
    bequiet_dr_4pro = cooler('163x136x146', '1x120 1x135', '7x6', '300000', '250w', 360)
    spc_navis_240_argb = cooler('54x275x120', '2x120', '-', '50000', '250w', 380)
    bequiet_pr_2 = cooler('155x121x88', '1x120', '4x6', '80000', '150w', 150)
    spc_fera_3_argb = cooler('146x123x78', '1x120', '4x6', '50000', '180', 150)
    spc_fortis_3_argb = cooler('158x140x125', '1x140', '5x6', '50000', '220w', 190)
    spc_spartan_4_argb = cooler('134x106x78', '1x100', '2x6', '50000', '125', 90)
    msi_mag_lq_240r = cooler('52x120x274', '2x120', '-', '100000', '-', 520)
    spc_navis_360_argb = cooler('54x395x120', '3x120', '-', '50000', '350w', 500)
    scythe_mugen_5 = cooler('155x130x112', '1x120', '6x6', '120000', '-', 230)
    spc_grandis_3_argb = cooler('159x140x131', '1x120 1x140', '6x6', '50000', '250w', 250)
    arctic_lf_ll_argb = cooler('277x120x63', '2x120', '-', '60000', '-', 370)
    if s == 1:
      print(spc_fera_5.dimensions)
    if s == 2:
      print(spc_fera_5_dual.dimensions)
    if s == 3:
      print(spc_fortis_3.dimensions)
    if s == 4:
      print(spc_spartan_4.dimensions) 
    if s == 5:
      print(bequiet_pr_2_b.dimensions)
    if s == 6:
      print(spc_spartan_4max.dimensions)
    if s == 7:
      print(bequiet_dr_4.dimensions)
    if s == 8:
      print(spc_grandis_3.dimensions)
    if s == 9:
      print(spc_navis_240_rgb.dimensions)
    if s == 10:
      print(bequiet_dr_4pro.dimensions)
    if s == 11:
        print(spc_navis_240_argb.dimensions)
    if s == 12:
        print(bequiet_pr_2.dimensions)
    if s == 13:
        print(spc_fera_3_argb.dimensions)
    if s == 14:
        print(spc_fortis_3_argb.dimensions)
    if s == 15:
        print(spc_spartan_4_argb.dimensions)
    if s == 16:
        print(msi_mag_lq_240r.dimensions)
    if s == 17:
        print(spc_navis_360_argb.dimensions)
    if s == 18:
        print(scythe_mugen_5.dimensions)
    if s == 19:
        print(spc_grandis_3_argb.dimensions)
    if s == 20:
        print(arctic_lf_ll_argb.dimensions)
  if r == 7:
    class case:
        def __init__(self, size, dimensions, fans, mobo, psu, price):
            self.size = size
            self.dimensions = dimensions
            self.fans = fans
            self.mobo = mobo
            self.psu = psu
            self.price = price
    bq_pb_500dx = case('Middle Tower', '463x232x450', '3x140', 'ATX, mATX, mITX', 'ATX', 400)
    spc_signum_sg1tg = case('Middle Tower', '447x216x413', '2x120', 'ATX, mATX, mITX', 'ATX', 230)
    spc_regnum_rg6vtg = case('Middle Tower', '470x221x443', '4x120', 'ATX, mATX, mITX, eATX', 'ATX', 280)
    bq_pb_500_w = case('Middle Tower', '163x232x450', '2x140', 'ATX, mATX, mITX', 'ATX', 280)
    spc_regnum_rg6v_argb = case('Middle Tower', '470x221x443', '4x120', 'ATX, mATX, mITX, eATX', 'ATX', 340)
    spc_signum_sg1 = case('Middle Tower', '447x216x413', '4x120', 'ATX, mATX, mITX', 'ATX', 190)
    bq_pb_500_c = case('Middle Tower', '163x232x450', '2x140', 'ATX, mATX, mITX', 'ATX', 270)
    spc_signum_sg1v_argb = case('Middle Tower', '447x216x413', '4x120', 'ATX, mATX, mITX', 'ATX', 310)
    spc_armis_ar1 = case('Middle Tower', '415x191x368', '1x80', 'ATX, mATX, mITX', 'ATX', 140)
    spc_ventum_vt4v_argb = case('Middle Tower', '440x210x440', '4x120', 'ATX, mATX, mITX', 'ATX', 300)
    msi_forge_101m = case('Middle Tower', '499x210x421', '4x120', 'ATX, mATX, mITX', 'ATX', 300)
    bq_pb_500_b = case('Middle Tower', '163x232x450', '2x140', 'ATX, mATX, mITX', 'ATX', 300)
    spc_signum_sg1x_argb = case('Middle Tower', '447x216x413', '4x120', 'ATX, mATX, mITX', 'ATX', 330)
    krux_pallas = case('Middle Tower', '439x215x375', '4x120', 'ATX, mATX, mITX', 'ATX', 220)
    spc_signum_sg7v_argb = case('Middle Tower', '518x243x508', '4x120', 'ATX, mATX, mITX', 'ATX', 440)
    spc_ventum_vt4 = case('Middle Tower', '440x210x440', '4x120', 'ATX, mATX, mITX', 'ATX', 250)
    spc_armis_ar6x_argb = case('Middle Tower', '470x221x443', '4x120', 'ATX, mATX, mITX, eATX', 'ATX', 400)
    krux_trek = case('Middle Tower', '359x184x351', '1x80', 'mATX, mITX', 'ATX', 130)
    krux_mirror = case('Middle Tower', '454x212x415', '4x120', 'ATX, mATX, mITX', 'ATX', 250)
    krux_leda = case('Middle Tower', '453x211x455', '4x120', 'ATX, mATX, mITX', 'ATX', 280)
    if s == 1:
      print(bq_pb_500dx.size)
    if s == 2:
      print(spc_signum_sg1tg.size)
    if s == 3:
      print(spc_regnum_rg6vtg.size)
    if s == 4:
      print(bq_pb_500_w.size) 
    if s == 5:
      print(spc_regnum_rg6v_argb.size)
    if s == 6:
      print(spc_signum_sg1.size)
    if s == 7:
      print(bq_pb_500_c.size)
    if s == 8:
      print(spc_signum_sg1v_argb.size)
    if s == 9:
      print(spc_armis_ar1.size)
    if s == 10:
      print(spc_ventum_vt4v_argb.size)
    if s == 11:
        print(msi_forge_101m.size)
    if s == 12:
        print(bq_pb_500_b.size)
    if s == 13:
        print(spc_signum_sg1x_argb.size)
    if s == 14:
        print(krux_pallas.size)
    if s == 15:
        print(spc_signum_sg7v_argb.size)
    if s == 16:
        print(spc_ventum_vt4.size)
    if s == 17:
        print(spc_armis_ar6x_argb.size)
    if s == 18:
        print(krux_trek.size)
    if s == 19:
        print(krux_mirror.size)
    if s == 20:
        print(krux_leda.size)

if aa == "configurator":
  x = int(input())
  y = int(input())
  z = int(input())
  v = int(input())
  q = int(input())
  w = int(input())
  u = int(input())
  t = int(input())
  print("Welcome in PC configurator")
  print("----------------")
  #CPU
  if x == 0: 
      a = None
      b = 0
  if x == 1:
      a = "i5 10400f"
      b = 730
  if x == 2:
      a = "Ryzen 5 3600"
      b = 900
  if x == 3:
      a = "Ryzen 5 5600x"
      b = 1300
  if x == 4:
      a = "i5 11400"
      b = 900
  if x == 5:
      a = "i3 10100f"
      b = 370
  if x == 6:
      a = "Ryzen 5 3400G"
      b = 800
  if x == 7:
      a = "Ryzen 7 3700x"
      b = 1300
  if x == 8:
      a = "i5 11600k"
      b = 1200
  if x == 9:
      a = "Ryzen 5 1600af"
      b = 550
  if x == 10:
      a = "i5 10600kf"
      b = 900
  if x == 11:
      a = "i7 10700kf"
      b = 1250 
  if x == 12:
      a = "Ryzen 7 5800x"
      b = 1900
  if x == 13:
      a = "i5 10600k"
      b = 950 
  if x == 14:
      a = "i7 11700f"
      b = 1800
  if x == 15:
      a = "Ryzen 9 5900x"
      b = 2750 
  if x == 16:
      a = "Ryzen 3 1200af"
      b = 330
  if x == 17:
      a = "i5 11600kf"
      b = 1080
  if x == 18:
      a = "i7 10700k"
      b = 1500
  if x == 19:
      a = "Ryzen 7 3800x"
      b = 1350
  if x == 20:
      a = "Ryzen 9 3900x"
      b = 2000
#GPU
  if y == 0: 
      c = None
      d = 0
  if y == 1:
      c = "GTX 1660"
      d = 1900
  if y == 2:
      c = "RTX 2060"
      d = 2400
  if y == 3:
      c = "RTX 3070"
      d = 4400
  if y == 4:
      c = "GT 1030"
      d = 430
  if y == 5:
      c = "GTX 1660 Ti"
      d = 1800
  if y == 6:
      c = "GTX 1660 S"
      d = 1700
  if y == 7:
      c = "RTX 3070 Ti"
      d = 4700
  if y == 8:
      c = "RX 6700 XT"
      d = 4100
  if y == 9:
      c = "RTX 3080"
      d = 5900
  if y == 10:
      c = "RTX 3090"
      d = 10400
  if y == 11:
      c = "RTX 3060"
      d = 3000
  if y == 12:
      c = "GTX 1650 S"
      d = 1700
  if y == 13:
      c = "RX 6800 XT"
      d = 6100
  if y == 14:
      c = "RTX 3060 Ti"
      d = 3700
  if y == 15:
      c = "RTX 3080 Ti"
      d = 7300
  if y == 16:
      c = "RX 6900 XT"
      d = 9000
  if y == 17:
      c = "RX 6800"
      d = 6000
  if y == 18:
      c = "GTX 1650"
      d = 1400
  if y == 19:
      c = "RX 6600 XT"
      d = 3000
  if y == 20:
      c = "RX 6600"
      d = 2500
#MOBO
  if z == 0: 
      e = None
      f = 0
  if z == 1:
      e = "MSI B450 Gaming plus"
      f = 330
  if z == 2:
      e = "Gigabyte B560M DS3H"
      f = 410
  if z == 3:
      e = "MSI Z490 Gaming plus"
      f = 750
  if z == 4:
      e = "MSI B460M Pro-vdh"
      f = 330
  if z == 5:
      e = "MSI B460M Pro"
      f = 300
  if z == 6:
      e = "MSI Z490 A-pro"
      f = 680
  if z == 7:
      e = "Gigabyte Z590 Gaming x"
      f = 760
  if z == 8:
      e = "MSI B550 A-pro"
      f = 670
  if z == 9:
      e = "MSI B450 Tomahawk"
      f = 350
  if z == 10:
      e = "MSI B450 A-pro"
      f = 300
  if z == 11:
      e = "Gigabyte B460M DS3H V2"
      f = 280
  if z == 12:
      e = "MSI B550 Tomahawk"
      f = 660
  if z == 13:
      e = "ASRock B560M pro4"
      f = 490
  if z == 14:
      e = "ASRock B560 pro4"
      f = 570
  if z == 15:
      e = "Gigabyte X570 A elite"
      f = 900
  if z == 16:
      e = "Gigabyte B450 A elite"
      f = 350
  if z == 17:
      e = "MSI B560M Bazooka"
      f = 520
  if z == 18:
      e = "MSI Z590 A-pro"
      f = 830
  if z == 19:
      e = "Gigabyte B450 DS3H"
      f = 260
  if z == 20:
      e = "Gigabyte X570 Gaming X"
      f = 730
#RAM
  if v == 0: 
      g = None
      h = 0
  if v == 1:
      g = "2x8GB 3200 Hyperx"
      h = 420
  if v == 2:
      g = "2x8GB 3600 Crucial"
      h = 450
  if v == 3:
      g = "2x8GB 3200 Hyperx RGB"
      h = 460
  if v == 4:
      g = "2x8GB 3600 Hyperx RGB"
      h = 460
  if v == 5:
      g = "1x16GB 3200 Goodram"
      h = 320
  if v == 6:
      g = "2x8GB 2666 Hyperx"
      h = 390
  if v == 7:
      g = "2x8GB 3200 Crucial"
      h = 410
  if v == 8:
      g = "1x8GB 3200 Goodram"
      h = 180
  if v == 9:
      g = "2x8GB 3200 Crucial RED"
      h = 420
  if v == 10:
      g = "2x8GB 3200 Viper 4 B"
      h = 410
  if v == 11:
      g = "2x16GB 3200 G.S Ripjaws V"
      h = 420
  if v == 12:
      g = "2x8GB 2666 Goodram"
      h = 360
  if v == 13:
      g = "2x8GB 3200 G.S Aegis"
      h = 380
  if v == 14:
      g = "2x8GB 3200 Goodram"
      h = 400
  if v == 15:
      g = "2x8GB 3200 G.S Ripjaws"
      h = 400
  if v == 16:
      g = "2x8GB 3200 Corsair RGB"
      h = 530
  if v == 17:
      g = "2x8GB 3200 Adata D20"
      h = 740
  if v == 18:
      g = "2x4GB 3200 Viper 4 B"
      h = 240
  if v == 19:
      g = "2x16GB 3200 Hyperx RGB"
      h = 850
  if v == 20:
      g = "2x16GB 3200 Hyperx"
      h = 830
#DRIVE
  if q == 0: 
      i = None
      j = 0
  if q == 1:
      i = "Samsung 980 500GB"
      j = 300
  if q == 2:
      i = "WD SN550 1TB"
      j = 470 
  if q == 3:
      i = "Goodram CX400 512GB"
      j = 230
  if q == 4:
      i = "Crucial MX500 500GB"
      j = 260
  if q == 5:
      i = "Samsung 980 1TB"
      j = 590
  if q == 6:
      i = "Samsung 870 evo 500GB"
      j = 350
  if q == 7:
      i = "Seagate Barracuda 2TB"
      j = 240
  if q == 8:
      i = "Kioxia exceria 240GB"
      j = 140
  if q == 9:
      i = "Crucial BX500 240GB"
      j = 150
  if q == 10:
      i = "Samsung 870 evo 1TB"
      j = 500
  if q == 11:
      i = "Gigabyte 512GB M.2"
      j = 270
  if q == 12:
      i = "Kioxia Exceria 480GB"
      j = 220
  if q == 13:
      i = "Goodram CX400 256GB"
      j = 140
  if q == 14:
      i = "Kingston A2000 500GB"
      j = 240
  if q == 15:
      i = "Kingston KC2500 500GB"
      j = 330
  if q == 16:
      i = "Goodram CX400 1TB"
      j = 430
  if q == 17:
      i = "Samsung 870 qvo 1TB"
      j = 450
  if q == 18:
      i = "Samsung 970 evo 500GB"
      j = 420
  if q == 19:
      i = "WD blue sata 500GB"
      j = 260
  if q == 20:
      i = "Goodram CX400 128GB"
      j = 90
#PSU
  if w == 0: 
      k = None
      l = 0
  if w == 1:
      k = "SPC Vero L3 600w"
      l = 250 
  if w == 2:
      k = "SPC Vero L3 500w"
      l = 200
  if w == 3:
      k = "SPC Supremo FM2 750w"
      l = 450
  if w == 4:
      k = "BeQuiet StrPow11 850w"
      l = 700
  if w == 5:
      k = "SPC Vero M3 700w"
      l = 300
  if w == 6:
      k = "SPC Supremo FM2 650w"
      l = 400
  if w == 7:
      k = "Gigabyte P850GM 850w"
      l = 470 
  if w == 8:
      k = "SPC Supremo M2 550w"
      l = 300
  if w == 9:
      k = "BeQuiet SysPow9 600w"
      l = 270
  if w == 10:
      k = "BeQuiet PurPow11 600w"
      l = 400
  if w == 11:
      k = "Chieftec Smart 500w"
      l = 200
  if w == 12:
      k = "SPC Supremo l2 650w"
      l = 360
  if w == 13:
      k = "SPC Vero m3 600w"
      l = 270
  if w == 14:
      k = "SPC Supremo l2 550w"
      l = 280
  if w == 15:
      k = "BeQuiet SysPow9 700w"
      l = 330
  if w == 16:
      k = "Corsair CV550 550w"
      l = 200
  if w == 17:
      k = "BeQuiet StrPow11 750w"
      l = 600
  if w == 18:
      k = "Corsair RM750x 750w"
      l = 540
  if w == 19:
      k = "Corsair TX750M 750w"
      l = 400
  if w == 20:
      k = "SPC Elementum e2 450w"
      l = 170
#COOLING
  if u == 0: 
      m = None
      n = 0
  if u == 1:
      m = "SPC Fera 5"
      n = 120
  if u == 2:
      m = "SPC Fortis 3"
      n = 160
  if u == 3:
      m = "SPC Fera 5 dual"
      n = 150
  if u == 4:
      m = "SPC Spartan 4"
      n = 70 
  if u == 5:
      m = "BeQuiet Pure Rock 2"
      n = 170 
  if u == 6:
      m = "SPC Spartan 4 Max"
      n = 90 
  if u == 7:
      m = "BeQuiet Dark Rock 4"
      n = 280 
  if u == 8:
      m = "SPC Grandis 3"
      n = 200 
  if u == 9:
      m = "SPC Navis 240 RGB"
      n = 320 
  if u == 10:
      m = "BeQuiet Dark Rock Pro4"
      n = 360 
  if u == 11:
      m = "SPC Navis 240 ARGB"
      n = 380
  if u == 12:
      m = "BeQuiet Pure Rock 2"
      n = 150
  if u == 13:
      m = "SPC Fera 3 ARGB"
      n = 150
  if u == 14:
      m = "SPC Fortis 3 ARGB"
      n = 190
  if u == 15:
      m = "SPC Spartan 4 ARGB"
      n = 90
  if u == 16:
      m = "MSI MAG Core LQ 240R"
      n = 520
  if u == 17:
      m = "SPC Navis 360 ARGB"
      n = 500
  if u == 18:
      m = "Scythe Mugen 5"
      n = 230
  if u == 19:
      m = "SPC Grandis 3 ARGB"
      n = 250
  if u == 20:
      m = "Arctic LF II 240"
      n = 370
#CASE
  if t == 0: 
      o = None
      p = 0
  if t == 1:
      o = "BeQuiet Pure Base 500DX"
      p = 400
  if t == 2:
      o = "SPC Signum SG1 TG"
      p = 230
  if t == 3:
      o = "SPC Regnum RG6V TG"
      p = 280
  if t == 4:
      o = "BeQuiet Pure Base 500 W"
      p = 280
  if t == 5:
      o = "SPC Regnum RG6V TG ARGB"
      p = 340
  if t == 6:
      o = "SPC Signum SG1"
      p = 190
  if t == 7:
      o = "BeQuiet Pure Base 500"
      p = 270
  if t == 8:
      o = "SPC Signum SG1V TG ARGB"
      p = 310
  if t == 9:
      o = "SPC Armis AR1"
      p = 140
  if t == 10:
      o = "SPC Ventum VT4V TG ARGB"
      p = 300
  if t == 11:
      o = "MSI MAG Forge 101M"
      p = 300    
  if t == 12:
      o = "BeQuiet Pure Base 500"
      p = 300    
  if t == 13:
      o = "SPC Signum SG1X RGB"
      p = 330
  if t == 14:
      o = "Krux Pallas"
      p = 220  
  if t == 15:
      o = "SPC Signum SG7V ARGB"
      p = 440
  if t == 16:
      o = "SPC Ventum VT4V"
      p = 250
  if t == 17:
      o = "SPC Armis AR6X ARGB"
      p = 400
  if t == 18:
      o = "Krux Trek"
      p = 130
  if t == 19:
      o = "Krux Mirror"
      p = 250
  if t == 20:
      o = "Krux Leda"
      p = 280
    
  s = b+d+f+h+j+l+n+p
  print("First - choose your CPU:")
  print("{0} - {1} {2}".format(a,b,"zł"))
  print("          ")
  print("Now choose GPU:")
  print("{0} - {1} {2}".format(c,d,"zł"))
  print("          ")
  print("Now choose MOBO:")
  print("{0} - {1} {2}".format(e,f,"zł"))
  print("          ")
  print("Now choose your RAM:")
  print("{0} - {1} {2}".format(g,h,"zł"))
  print("          ")
  print("Now choose your drives:")
  print("{0} - {1} {2}".format(i,j,"zł"))
  print("          ")
  print("Now choose PSU:")
  print("{0} - {1} {2}".format(k,l,"zł"))
  print("          ")
  print("Now choose additional cooling:")
  print("{0} - {1} {2}".format(m,n,"zł"))
  print("          ")
  print("Now choose case:")
  print("{0} - {1} {2}".format(o,p,"zł"))
  print("----------------")
  print("summary: {0} {1}".format(s,"zł"))