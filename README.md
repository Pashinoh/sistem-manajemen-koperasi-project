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

## 📂 Struktur Folder

koperasi/
│
├── app.py
├── models/
│ └── models.py
├── routes/
│ ├── auth_routes.py
│ └── main_routes.py
├── templates/
│ ├── login.html
│ ├── register.html
│ └── dashboard.html
├── static/
│ └── style.css
│
├── requirements.txt
├── setup.py
├── .env.example
├── .gitignore
└── README.md

---

## ⚙️ Persiapan Awal

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<username-kamu>/koperasi.git
cd koperasi

python setup.py

cp .env.example .env
```
## ⚙️ jalankan app
```bash
flask run
