#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:15:52 2020

@author: Kelas Kazeters
@Email: msg.kazeters@gmail.com
"""

while True:
    print("======================================================")
    print("Bangun Ruang Apa Yang Mau Anda Cari Jawabannya?")
    print("1. Kubus")
    print("2. Balok")
    pilbaang = int(input("Masukkan Nomor Bangun Ruang : "))
    print("======================================================")
    if pilbaang == 1:
        print("======================================================")
        print("Mau Mencari Jawaban Dari Rumus Apa?")
        print("1. Volume Kubus")
        print("2. Panjang Rusuk Kubus")
        pilrubus = int(input("Masukkan Nomor Rumus : "))
        if pilrubus == 1:
            panrubus = int(input("Masukkan Panjang Rusuk : "))
            # Volume Kubus
            vk = panrubus**3
            print("======================================================")
            print("Jawaban :",vk)
            print("======================================================")
            menvolbus = input("Apakah Anda Ingin Mencoba Lagi [Y/n]?")
            if menvolbus == 'y':
                pass
            else:
                print("Terimakasih Sudah Menggunakan Program Ini!")
                break
        elif pilrubus == 2:
            volbus = int(input("Masukkan Volume Kubus : "))
            # Rumus Panjang Rusuk Kubus
            import math
            prk = math.pow(volbus,1/3.0)
            print("======================================================")
            print("Jawaban :",round(prk))
            print("======================================================")
            menparubus = input("Apakah Anda Ingin Mencoba Lagi [Y/n]?")
            if menparubus == 'y':
                pass
            else:
                print("Terimakasih Sudah Menggunakan Program Ini!")
                break
        else:
            print("Anda Salah Memasukkan Nomor! Mohon Masukkan Nomor Yang Tersedia!")
    elif pilbaang == 2:
        print("======================================================")
        print("Mau Mencari Jawaban Dari Rumus Apa?")
        print("1. Volume")
        print("2. Panjang")
        print("3. Lebar")
        print("4. Tinggi")
        pilrulok = int(input("Masukkan Nomor Rumus : "))
        if pilrulok == 1:
            pb = int(input("Masukkan Panjang Balok : "))
            lb = int(input("Masukkan Lebar Balok : "))
            tb = int(input("Masukkan Tinggi Balok : "))
            
            # Rumus Volume Balok
            vb = pb * lb * tb
            print("======================================================")
            print("Jawaban :",vb)
            print("======================================================")
            menvolok = input("Apakah Anda Ingin Mencoba Lagi [Y/n]?")
            if menvolok == 'y':
                pass
            else:
                print("Terimakasih Sudah Menggunakan Program Ini!")
                break
        elif pilrulok == 2:
            vb1 = int(input("Masukkan Volume Balok : "))
            lb1 = int(input("Masukkan Lebar Balok : "))
            tb1 = int(input("Masukkan Tinggi Balok : "))
            
            # Rumus Mencari P Balok
            mpb = vb1 / (lb1 * tb1)
            print("======================================================")
            print("Jawaban :",mpb)
            print("======================================================")
            menpabalok = input("Apakah Anda Ingin Mencoba Lagi [Y/n]?")
            if menpabalok == 'y':
                pass
            else:
                print("Terimakasih Sudah Menggunakan Program Ini!")
                break
        elif pilrulok == 3:
            vb2 = int(input("Masukkan Volume Balok : "))
            pb2 = int(input("Masukkan Panjang Balok : "))
            tb2 = int(input("Masukkan Tinggi Balok : "))
            
            # Rumus Mencari L Balok
            mlb = vb2 / (pb2 * tb2)
            print("======================================================")
            print("Jawaban :",mlb)
            print("======================================================")
            menlebalok = input("Apakah Anda Ingin Mencoba Lagi [Y/n]?")
            if menlebalok == 'y':
                pass
            else:
                print("Terimakasih Sudah Menggunakan Program Ini!")
                break
        elif pilrulok == 4:
            vb3 = int(input("Masukkan Volume Balok : "))
            pb3 = int(input("Masukkan Panjang Balok : "))
            lb3 = int(input("Masukkan Lebar Balok : "))
           
            # Rumus Mencari T Balok
            mtb = vb2 / (pb3 * lb3)
            print("======================================================")
            print("Jawaban :",mtb)
            print("======================================================")
            menpalok = input("Apakah Anda Ingin Mencoba Lagi [Y/n]?")
            if menpalok == 'y':
                pass
            else:
                print("Terimakasih Sudah Menggunakan Program Ini!")
                break
        else:
            print("Anda Salah Memasukkan Nomor! Mohon Masukkan Nomor Yang Tersedia!")
    else:
        print("Anda Salah Memasukkan Nomor! Mohon Masukkan Nomor Yang Tersedia!")
