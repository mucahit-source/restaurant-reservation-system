import datetime

# Masa bilgileri
TOTAL_TABLES = 25
BUSINESS_TABLES = 10
NORMAL_TABLES = TOTAL_TABLES - BUSINESS_TABLES

# Günlük rezervasyonlar
reservations_by_day = {}

def reserve_table():
    while True:
        day = input("Merhabalar :) rezervasyon yapacağınız günü giriniz (tarih formatı: yıl-ay-gün): ").strip()

        # Tarih formatı kontrolü
        try:
            datetime.datetime.strptime(day, "%Y-%m-%d")
        except ValueError:
            print("Geçersiz tarih formatı. Lütfen yıl-ay-gün şeklinde girin.")
            continue

        # Günlük rezervasyon listesi oluşturulmamışsa başlat
        if day not in reservations_by_day:
            reservations_by_day[day] = []

        # Günlük doluluk kontrolü
        if len(reservations_by_day[day]) >= TOTAL_TABLES:
            print("Üzgünüm, seçtiğiniz tarihte tüm masalar dolu :(")
            break

        name = input("İsminizi giriniz: ").strip()
        phone = input("Telefon numaranızı giriniz: ").strip()
        table_type = input("Rezervasyonunuz 'normal' sınıf mı 'business' sınıfı mı olsun? ").strip().lower()

        if table_type not in ["normal", "business"]:
            print("Lütfen sadece 'normal' veya 'business' yazınız.")
            continue

        # Günlük rezervasyonları filtrele
        business_today = [i for i in reservations_by_day[day] if i["type"] == "business"]
        normal_today = [i for i in reservations_by_day[day] if i["type"] == "normal"]

        if table_type == "business":
            if len(business_today) < BUSINESS_TABLES:
                table_number = len(business_today) + 1
            else:
                print("Business sınıfı istediğiniz gün maalesef dolu.")
                break
        else:  # normal
            if len(normal_today) < NORMAL_TABLES:
                table_number = BUSINESS_TABLES + len(normal_today) + 1
            else:
                print("Normal sınıf istediğiniz gün maalesef dolu.")
                break

        # Rezervasyonu ekle
        reservations_by_day[day].append({
            'name': name,
            'phone': phone,
            'table': table_number,
            'type': table_type
        })

        print(f"{name} için {table_type} sınıfında masa numarası: {table_number}")
        break

def check_table():
    day = input("Merhabalar :) rezervasyon yaptığınız günü giriniz (tarih formatı: yıl-ay-gün): ").strip()

    if day not in reservations_by_day:
        print("Bu gün için hiç rezervasyon bulunamadı.")
        return

    name = input("İsminizi giriniz: ").strip()
    found = False
    for i in reservations_by_day[day]:
        if i["name"].lower() == name.lower():
            print(f"{name} için ayrılan masa numarası: {i['table']}")
            found = True
            break

    if not found:
        print("Girdiğiniz bilgilere göre rezervasyon bulunamadı.")
        choice = input("Yeni rezervasyon yapmak ister misiniz? (evet/hayır): ").strip().lower()
        if choice == "evet":
            reserve_table()

def main():
    print("Hoşgeldiniz")
    while True:
        try:
            print("\n--- Rezervasyon Sistemi ---")
            print("1. Yeni rezervasyon yap")
            print("2. Masa numarasını sorgula")
            print("3. Çıkış")
            choice = input("Seçiminiz: ").strip()
            if choice == "1":
                reserve_table()
            elif choice == "2":
                check_table()
            elif choice == "3":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim. Lütfen 1, 2 veya 3 giriniz.")
        except Exception as e:
            print("Bir hata oluştu:", e)

main()
