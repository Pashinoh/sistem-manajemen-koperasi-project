# 🏦 Sistem Manajemen Koperasi

Proyek ini merupakan aplikasi web sederhana untuk **mengelola data anggota dan pengguna koperasi**, dibuat menggunakan **Python Flask**.  
Tujuan utama proyek ini adalah untuk memenuhi **Tugas Akhir UAS** mata kuliah *Pemrograman Web / Basis Data / Framework Python*.

---

## 🚀 Fitur Utama

✅ **Registrasi & Login User**
- Pengguna dapat mendaftar akun baru (role default: `anggota`)
- Login dan logout dengan sesi aman menggunakan `Flask Session`

✅ **Dashboard Sederhana**
- Menampilkan data dasar dan identitas user yang sedang login

✅ **Struktur Folder Rapi**
- Menggunakan `Blueprint` (modular) untuk pemisahan route `auth` dan `main`

✅ **Database Otomatis**
- Menggunakan `Flask SQLAlchemy` dan `Flask-Migrate`
- Otomatis membuat file database `koperasi.db` saat setup

---

## ⚙️ Persiapan Awal

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Pashinoh/sistem-manajemen-koperasi-project.git
```

## ⚙️ jalankan app
```bash
flask run
