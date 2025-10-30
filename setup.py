import os
import subprocess
from dotenv import load_dotenv
from app import app, db

print("🚀 Setup environment Flask Koperasi dimulai...")

# Buat virtual environment jika belum ada
if not os.path.exists('venv'):
    print("📦 Membuat virtual environment...")
    subprocess.run(['python', '-m', 'venv', 'venv'])

# Install requirements
print("📥 Menginstal dependensi...")
pip_path = 'venv\\Scripts\\pip.exe' if os.name == 'nt' else 'venv/bin/pip'
subprocess.run([pip_path, 'install', '-r', 'requirements.txt'])

# Buat folder instance jika belum ada
if not os.path.exists('instance'):
    os.mkdir('instance')

# Load env dan buat database
load_dotenv()
with app.app_context():
    print("🗃️  Membuat database (jika belum ada)...")
    db.create_all()

print("✅ Setup selesai! Jalankan dengan: flask run")
