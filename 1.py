import re
import datetime

teks = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."
tanggal_list = re.findall(r'\b(\d{4}-\d{2}-\d{2})\b', teks)

for tanggal in tanggal_list:
    tahun, bulan, hari = tanggal.split('-')
    tanggall = f"{hari}-{bulan}-{tahun}"
    TS = datetime.datetime(2024, 6, 2) 
    TL = datetime.datetime(int(tahun), int(bulan), int(hari))
    selisih_hari = (TS - TL).days
    print(f"{tanggall} 00:00:00 selisih {selisih_hari} hari")