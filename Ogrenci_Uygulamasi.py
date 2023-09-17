from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
import sys
from Giris_Ekrani import *
from Menu_Ekrani import *
from Kayit_Ekrani import *
from Ogrenci_Bilgi_Ekrani import *
import sqlite3

con=sqlite3.connect("Okul.db")
crsr=con.cursor()
class Giris_Ekrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_girisyap.clicked.connect(self.GirisKontrol)
    def GirisKontrol(self):
        con=sqlite3.connect("Okul.db")
        crsr=con.cursor()
        if self.ui.txt_kullaniciadi.text().strip()=="" or self.ui.txt_parola.text().strip()=="":
            QMessageBox.critical(None, "BİLGİ", "Kullanıcı adı veya şifre boş geçilemez!")
        else:
            ka = self.ui.txt_kullaniciadi.text()
            sifre=self.ui.txt_parola.text()
            giris_sorgusu=f"select * from Calisanlar where CalisanKa='{ka}' and CalisanSifre='{sifre}'"
            crsr.execute(giris_sorgusu)
            kisi=crsr.fetchone()
            if kisi:
                QMessageBox.information(None,"BİLGİ","GİRİŞ BAŞARILI")
                self.hide()
                self.menu=Menum()
                self.menu.show()
            else:
                QMessageBox.critical(None, "BİLGİ", "GİRİŞ BAŞARISIZ")



class Menum(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Menu()
        self.ui.setupUi(self)
        self.ui.btn_ogrekle.clicked.connect(self.KayitEkraniAc)
        self.ui.btn_bilgiler.clicked.connect(self.BilgiEkraniAc)
    def KayitEkraniAc(self):
        self.hide()
        self.register_screen=RegisterScreen()
        self.register_screen.show()
    def BilgiEkraniAc(self):
        self.hide()
        self.bilgi_ekrani=OgrenciBilgiEkrani()
        self.bilgi_ekrani.show()


class RegisterScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = KayitEkranim()
        self.ui.setupUi(self)
        self.ui.btn_ekle.clicked.connect(self.KayitEt)
        self.ui.btn_sifirla.clicked.connect(self.EkraniSifirla)
    def KayitEt(self):
        try:
            ad=self.ui.txt_ad.text()
            soyad=self.ui.txt_soyad.text()
            tc=self.ui.txt_tc.text()
            hobiler=self.ui.cmb_hobiler.currentText()
            dogum_tarihi=self.ui.dt_dogumtarihi.date().toString("yyyy-MM-dd")
            veli_adi=self.ui.txt_veliadi.text()
            veli_tel=self.ui.txt_velitel.text()
            ekleme_sorgusu=f"insert into Ogrenciler (OgrenciAd,OgrenciSoyad,OgrenciTc,OgrenciHobi,OgrenciDogumTarihi,OgrenciVeliAd,OgrenciVeliTel)values('{ad}','{soyad}','{tc}','{hobiler}','{dogum_tarihi}','{veli_adi}','{veli_tel}')"
            crsr.execute(ekleme_sorgusu)
            con.commit()
            #VERİLERİ SIFIRLAMAK İÇİN KULLANILAN KOD
            self.ui.txt_ad.setText("")
            self.ui.txt_soyad.setText("")
            self.ui.txt_tc.setText("")
            self.ui.cmb_hobiler.setCurrentText("")
            #self.ui.dt_dogumtarihi.date().toString("yyyy-MM-dd")
            self.ui.txt_veliadi.setText("")
            self.ui.txt_velitel.setText("")
            self.ui.cmb_hobiler.setCurrentIndex(-1)

        except:
            QMessageBox.information(None,"UYARI","KAYIT GERÇEKLEŞMEDİ")
    def EkraniSifirla(self):
        self.ui.txt_ad.setText("")
        self.ui.txt_soyad.setText("")
        self.ui.txt_tc.setText("")
        self.ui.cmb_hobiler.setCurrentText("")
        # self.ui.dt_dogumtarihi.date().toString("yyyy-MM-dd")
        self.ui.txt_veliadi.setText("")
        self.ui.txt_velitel.setText("")
        self.ui.cmb_hobiler.setCurrentIndex(-1)

class OgrenciBilgiEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Bilgi_Ekrani()
        self.ui.setupUi(self)
        self.ui.txt_idara.setDisabled(True)
        self.ui.txt_tcara.setDisabled(True)
        self.ui.btn_ograra.clicked.connect(self.AramaYap)
        self.ui.btn_herkes.clicked.connect(self.HerkesiGetir)
        self.ui.btn_ekle.clicked.connect(self.Bilgi_Guncelle)
        self.ui.btn_aktifet.clicked.connect(self.AktifEt)
        self.ui.tbl_ogrenciler.cellClicked.connect(self.Hucreden_Verial)
        #==========================================
        #İTEMLARI TABLOYA YAZDIRMA KOMUTLARIR
        self.HerkesiGetir()


    def Bilgi_Guncelle(self):
        if self.ui.txt_id.text().strip()=="":
            QMessageBox.critical(None,"UYARI","ID BİLGİSİ BOŞ GEÇİLEMEZ")
        else:
            con=sqlite3.connect("Okul.db")
            crsr=con.cursor()
            id=int(self.ui.txt_id.text())
            ad=self.ui.txt_ad.text()
            soyad=self.ui.txt_soyad.text()
            tc=self.ui.txt_tc.text()
            hobiler=self.ui.cmb_hobiler.currentText()
            dogumtarihi=self.ui.dt_dogumtarihi.date().toString("yyyy-MM-dd")
            veli_adi=self.ui.txt_veliadi.text()
            veli_tel=self.ui.txt_velitel.text()
            guncelleme_sorgusu=f"update Ogrenciler set OgrenciAd='{ad}',OgrenciSoyad='{soyad}',OgrenciTc='{tc}',OgrenciHobi='{hobiler}',OgrenciDogumTarihi='{dogumtarihi}',OgrenciVeliAd='{veli_adi}',OgrenciVeliTel='{veli_tel}' where OgrenciID='{id}' "
            crsr.execute(guncelleme_sorgusu)
            con.commit()
            self.HerkesiGetir()
    def Hucreden_Verial(self,satir,sutun):
        satir_verisi=[]
        for i in range(self.ui.tbl_ogrenciler.columnCount()):
            item=self.ui.tbl_ogrenciler.item(satir,i)
            if item is not None:
                satir_verisi.append(item.text())
            else:
                satir_verisi.append(None)

        self.ui.txt_id.setText(satir_verisi[0])
        self.ui.txt_ad.setText(satir_verisi[1])
        self.ui.txt_soyad.setText(satir_verisi[2])
        self.ui.txt_tc.setText(satir_verisi[3])
        self.ui.cmb_hobiler.setCurrentText(satir_verisi[4])
        self.ui.dt_dogumtarihi.setSpecialValueText(satir_verisi[5])
        self.ui.txt_veliadi.setText(satir_verisi[6])
        self.ui.txt_velitel.setText(satir_verisi[7])
    def AktifEt(self):
        if self.ui.rdb_tc.isChecked():
            self.ui.txt_tcara.setEnabled(True)
            self.ui.txt_idara.setEnabled(False)
        else:
            self.ui.txt_idara.setEnabled(True)
            self.ui.txt_tcara.setEnabled(False)

    def AramaYap(self):
            if self.ui.txt_tcara.isEnabled():
                tc=self.ui.txt_tcara.text()
                crsr.execute(f"select * from Ogrenciler where OgrenciTc='{tc}'")
                veriler = crsr.fetchall()
                print(veriler)
                basliklar = [baslik[0] for baslik in crsr.description]
                self.ui.tbl_ogrenciler.setHorizontalHeaderLabels(basliklar)
                self.ui.tbl_ogrenciler.verticalHeader().setVisible(False)
                self.ui.tbl_ogrenciler.setRowCount(len(veriler))
                self.ui.tbl_ogrenciler.setColumnCount(len(veriler[0]))

                for column, baslik in enumerate(basliklar):
                    item = QTableWidgetItem(baslik)
                    self.ui.tbl_ogrenciler.setHorizontalHeaderItem(column, item)
                for row, satir_verileri in enumerate(veriler):
                    for column, veri in enumerate(satir_verileri):
                        item = QTableWidgetItem(str(veri))
                        self.ui.tbl_ogrenciler.setItem(row, column, item)
                self.ui.tbl_ogrenciler.show()
            elif self.ui.txt_idara.isEnabled():
                id = self.ui.txt_idara.text()
                crsr.execute(f"select * from Ogrenciler where OgrenciID='{id}'")
                veriler = crsr.fetchall()
                print(veriler)
                basliklar = [baslik[0] for baslik in crsr.description]
                self.ui.tbl_ogrenciler.setHorizontalHeaderLabels(basliklar)
                self.ui.tbl_ogrenciler.verticalHeader().setVisible(False)
                self.ui.tbl_ogrenciler.setRowCount(len(veriler))
                self.ui.tbl_ogrenciler.setColumnCount(len(veriler[0]))

                for column, baslik in enumerate(basliklar):
                    item = QTableWidgetItem(baslik)
                    self.ui.tbl_ogrenciler.setHorizontalHeaderItem(column, item)
                for row, satir_verileri in enumerate(veriler):
                    for column, veri in enumerate(satir_verileri):
                        item = QTableWidgetItem(str(veri))
                        self.ui.tbl_ogrenciler.setItem(row, column, item)
                self.ui.tbl_ogrenciler.show()
            else:
                QMessageBox.critical(None,"BİLGİ","ARAMAK İÇİN TERCİH YAPIN")
    def HerkesiGetir(self):
        crsr.execute("Select * from Ogrenciler")
        veriler = crsr.fetchall()
        basliklar = [baslik[0] for baslik in crsr.description]
        self.ui.tbl_ogrenciler.setHorizontalHeaderLabels(basliklar)
        self.ui.tbl_ogrenciler.verticalHeader().setVisible(False)
        self.ui.tbl_ogrenciler.setRowCount(len(veriler))
        self.ui.tbl_ogrenciler.setColumnCount(len(veriler[0]))

        for column, baslik in enumerate(basliklar):
            item = QTableWidgetItem(baslik)
            self.ui.tbl_ogrenciler.setHorizontalHeaderItem(column, item)
        for row, satir_verileri in enumerate(veriler):
            for column, veri in enumerate(satir_verileri):
                item = QTableWidgetItem(str(veri))
                self.ui.tbl_ogrenciler.setItem(row, column, item)
        self.ui.tbl_ogrenciler.show()


















def main():
    app=QApplication(sys.argv)
    pencere=Giris_Ekrani()
    pencere.show()
    sys.exit(app.exec())


if __name__=="__main__":
    main()












