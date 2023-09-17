import sqlite3

connection=sqlite3.connect("Okul.db")

crsr=connection.cursor()
"""SELECT KOMUTU ILE VERI ÇEKME"""
# crsr.execute("select * from Ogrenciler where OgrenciID=13")
# ogrenciler=crsr.fetchone()
# print(ogrenciler)


"""INSERT KOMUTU ILE VERI EKLEME"""
# ogrenci_ad=input("Ad bilgisini giriniz")
# crsr.execute(f"insert into Ogrenciler (OgrenciAd)values('{ogrenci_ad}')")
# connection.commit()


# """Update KOMUTU ILE VERI GÜNCELLEME"""
# guncel_ogrenci_ad=input("Güncel Ad bilgisini giriniz")
# crsr.execute(f"update Ogrenciler set OgrenciAd='{guncel_ogrenci_ad}' where OgrenciID=15")
# connection.commit()

# """Delete KOMUTU ILE VERI GÜNCELLEME"""
# silinecek_id1=int(input("id bilgisini giriniz"))
# silinecek_id2=int(input("id bilgisini giriniz"))
#1.YÖNTEM
# crsr.execute(f"delete from Ogrenciler where OgrenciID in('{silinecek_id1}','{silinecek_id2}')  ")
#2.YÖNTEM
# crsr.execute(f"delete from Ogrenciler where OgrenciID='{silinecek_id1}' or  OgrenciID='{silinecek_id2}'")
# connection.commit()


"""
SQL QUERY 

SELECT=>Veri tabanındaki istenilen tabloları ekrana getirir. 


UPDATE => Tablo içerisindeki bir veya birden fazla satırda bulunan sütun bilgilerini güncellemeye yarar.

DELETE => Veri tabanından herhangi bir veriyi silmeye yarar.

Insert => Veri tabanına veri eklemeye yarar.
"""















