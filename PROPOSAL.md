# Proposal UTS: CyberIncident API

## 1. Judul
CyberIncident API: Sistem Pelaporan dan Manajemen Insiden Keamanan Siber Berbasis REST API.

## 2. Latar belakang
Pelaporan insiden keamanan perlu dicatat secara terstruktur agar informasi kejadian, aset terdampak, tingkat risiko, dan proses penanganan dapat ditelusuri. Pencatatan manual atau tersebar dapat membuat riwayat sulit ditemukan dan status penanganan kurang jelas. Proyek ini membuat API sederhana sebagai prototipe untuk mengelola data insiden menggunakan data simulasi.


## 3. Rumusan masalah
1. Bagaimana menyimpan laporan insiden keamanan secara terstruktur?
2. Bagaimana menghubungkan insiden dengan pelapor, aset, dan kategori?
3. Bagaimana memudahkan pencarian, filter, dan pelacakan status insiden?

## 4. Tujuan
Membangun REST API yang menyediakan pengelolaan laporan insiden, aset, pengguna, kategori, dan riwayat penanganan dengan operasi CRUD, filter, pencarian, dan pagination.

## 5. Pengguna
- Reporter: membuat dan melihat laporan.
- Analyst: memeriksa laporan dan mencatat penanganan.
- Admin (role data): mengelola data prototipe.

Role pada versi awal hanya disimpan sebagai data; autentikasi dan pembatasan akses belum diterapkan.


## 6. Fitur
- CRUD users, assets, incident categories, incidents.
- Incident update/history untuk mencatat status dan catatan penanganan.
- Pencarian judul, filter status/severity, pagination.
- Validasi input dan JSON response.

## 7. Teknologi
Python, Flask, Flask-SQLAlchemy (ORM), SQLite, Flask-Migrate, pytest, Postman, GitHub.

## 8. Batasan
- Data contoh bersifat simulasi.
- API belum memakai autentikasi atau otorisasi.
- Tidak melakukan scanning, eksploitasi, atau pemeriksaan jaringan.
- Belum ada frontend; API diuji dengan Postman.
- SQLite dipakai untuk pengembangan lokal.

## 9. Pengembangan untuk UAS
- Implementasi JWT dan role-based access control.
- Deployment pada layanan hosting.
- Dashboard frontend dan visualisasi.
- Dokumentasi OpenAPI lebih lengkap.
- Perluasan automated tests dan hardening konfigurasi.
