# CyberIncident API

Sistem Pelaporan dan Pengelolaan Insiden Keamanan Siber Berbasis REST API

## Identitas Mahasiswa

| Keterangan | Informasi |
|---|---|
| Nama | Rizki Ramadani |
| NIM | 23.83.1015 |
| Kelas | TK070 |
| Program Studi | Teknik Komputer |
| Universitas | Universitas Amikom Yogyakarta |
| Mata Kuliah | Pemrograman Web Lanjut |
| Tugas | Ujian Tengah Semester (UTS) |

## 1. Tentang Project

CyberIncident API adalah project sederhana yang saya buat menggunakan Python Flask untuk mengelola laporan insiden keamanan siber.

Project ini dibuat agar data kejadian keamanan, seperti percobaan login mencurigakan atau gangguan pada sistem, bisa dicatat dan dikelola dengan lebih terstruktur.

Melalui API ini, kita dapat menambahkan laporan, melihat data yang sudah tersimpan, mengubah status penanganan, dan menghapus laporan yang tidak diperlukan.

Project ini menggunakan data simulasi dan dibuat untuk memenuhi tugas UTS mata kuliah Pemrograman Web Lanjut.

## 2. Fitur Project

Beberapa fitur yang tersedia:

- Mengelola data pengguna (Users).
- Mengelola data aset (Assets).
- Mengelola kategori insiden (Categories).
- Membuat dan mengelola laporan insiden (Incidents).
- Menambahkan riwayat penanganan insiden.
- Melakukan pencarian, filter, dan pagination.
- Melakukan validasi data yang dikirim melalui API.
- Menampilkan respons dalam format JSON.

## 3. Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman |
| Flask | Framework REST API |
| Flask-SQLAlchemy | ORM untuk pengelolaan database |
| SQLite | Database yang digunakan |
| Flask-Migrate | Pengelolaan perubahan database |
| Postman | Pengujian API |
| pytest | Pengujian otomatis |
| GitHub | Penyimpanan source code |

## 4. Cara Menjalankan Project

Project ini dapat dijalankan melalui terminal VS Code.

### Membuat Virtual Environment

```bash
python3 -m venv venv
```

### Mengaktifkan Virtual Environment

Untuk macOS atau Linux:

```bash
source venv/bin/activate
```

Untuk Windows:

```bash
venv\Scripts\activate
```

### Menginstall Library

```bash
pip install -r requirements.txt
```

### Mengisi Database dengan Data Contoh

```bash
python seed.py
```

### Menjalankan Server

```bash
python run.py
```

Jika berhasil, server akan berjalan di alamat:

`http://127.0.0.1:5000`

Untuk memastikan API berjalan, buka:

`http://127.0.0.1:5000/api/v1/health`

## 5. Daftar Endpoint API

Berikut endpoint utama yang tersedia dalam project.

| Method | Endpoint | Keterangan |
|---|---|---|
| GET | `/api/v1/health` | Mengecek kondisi API |
| GET | `/api/v1/users` | Menampilkan pengguna |
| POST | `/api/v1/users` | Menambahkan pengguna |
| GET | `/api/v1/users/<id>` | Melihat detail pengguna |
| PUT | `/api/v1/users/<id>` | Mengubah pengguna |
| DELETE | `/api/v1/users/<id>` | Menghapus pengguna |
| GET | `/api/v1/assets` | Menampilkan aset |
| POST | `/api/v1/assets` | Menambahkan aset |
| GET | `/api/v1/assets/<id>` | Melihat detail aset |
| PUT | `/api/v1/assets/<id>` | Mengubah aset |
| DELETE | `/api/v1/assets/<id>` | Menghapus aset |
| GET | `/api/v1/categories` | Menampilkan kategori |
| POST | `/api/v1/categories` | Menambahkan kategori |
| GET | `/api/v1/categories/<id>` | Melihat detail kategori |
| PUT | `/api/v1/categories/<id>` | Mengubah kategori |
| DELETE | `/api/v1/categories/<id>` | Menghapus kategori |
| GET | `/api/v1/incidents` | Menampilkan laporan insiden |
| POST | `/api/v1/incidents` | Membuat laporan insiden |
| GET | `/api/v1/incidents/<id>` | Melihat detail insiden |
| PUT | `/api/v1/incidents/<id>` | Memperbarui insiden |
| DELETE | `/api/v1/incidents/<id>` | Menghapus insiden |
| GET | `/api/v1/incidents/<id>/updates` | Melihat riwayat penanganan |
| POST | `/api/v1/incidents/<id>/updates` | Menambahkan riwayat penanganan |

`<id>` diganti dengan nomor ID data yang ingin diakses.

## 6. Contoh Penggunaan API

Pengujian API dilakukan menggunakan Postman.

### Menampilkan Laporan Insiden

Method: `GET`

Endpoint:

```text
http://127.0.0.1:5000/api/v1/incidents
```

### Menambahkan Laporan Insiden

Method: `POST`

Endpoint:

```text
http://127.0.0.1:5000/api/v1/incidents
```

Contoh Body JSON:

```json
{
  "title": "Percobaan Login Mencurigakan",
  "description": "Terdeteksi aktivitas login mencurigakan pada server simulasi.",
  "severity": "high",
  "status": "open",
  "asset_id": 1,
  "category_id": 1,
  "user_id": 1
}
```

ID pengguna, aset, dan kategori harus disesuaikan dengan data yang tersedia.

### Mengubah Status Insiden

Method: `PUT`

Endpoint:

```text
http://127.0.0.1:5000/api/v1/incidents/2
```

Contoh Body JSON:

```json
{
  "status": "investigating"
}
```

### Menghapus Insiden

Method: `DELETE`

Endpoint:

```text
http://127.0.0.1:5000/api/v1/incidents/2
```

## 7. Pengujian Project

Pengujian dilakukan secara manual menggunakan Postman dan secara otomatis menggunakan pytest.

Hasil pengujian manual:

| Pengujian | Status HTTP | Hasil |
|---|---|---|
| GET laporan insiden | 200 OK | Berhasil |
| POST laporan baru | 201 Created | Berhasil |
| PUT laporan insiden | 200 OK | Berhasil |
| DELETE laporan insiden | 200 OK | Berhasil |
| GET data yang sudah dihapus | 404 Not Found | Sesuai harapan |
| POST tanpa data wajib | 400 Bad Request | Sesuai harapan |

Untuk menjalankan pengujian otomatis:

```bash
python -m pytest -v
```

Pada pengujian yang sudah dilakukan, terdapat 4 test dan semuanya berhasil.

## 8. Struktur Database

Project ini menggunakan lima tabel utama:

1. **Users:** menyimpan data pengguna atau pelapor.
2. **Assets:** menyimpan informasi aset yang berkaitan dengan insiden.
3. **Incident Categories:** menyimpan kategori insiden keamanan.
4. **Incidents:** menyimpan laporan kejadian keamanan.
5. **Incident Updates:** menyimpan riwayat pembaruan atau penanganan insiden.

Tabel-tabel tersebut saling berhubungan melalui relasi database sehingga informasi insiden dapat dikaitkan dengan pengguna, aset, dan kategorinya.

## 9. Dokumentasi Tambahan

Project ini juga dilengkapi beberapa file pendukung:

- `PROPOSAL.md` untuk penjelasan proposal UTS.
- `openapi.yaml` untuk dokumentasi spesifikasi API.
- `CyberIncident.postman_collection.json` untuk pengujian menggunakan Postman.
- Folder `tests/` untuk pengujian otomatis.

## 10. Batasan Project

CyberIncident API masih berupa prototipe sederhana. Beberapa batasannya adalah:

- Menggunakan data simulasi.
- Belum memiliki tampilan frontend.
- Belum menggunakan autentikasi dan otorisasi.
- Menggunakan SQLite untuk pengembangan lokal.
- Tidak melakukan scanning atau eksploitasi jaringan.

## 11. Rencana Pengembangan UAS

Untuk pengembangan selanjutnya, saya berencana menambahkan:

- Login dan autentikasi menggunakan JWT.
- Pembatasan akses berdasarkan role pengguna.
- Dashboard untuk melihat data laporan.
- Deployment API agar bisa diakses secara online.
- Pengujian dan validasi yang lebih lengkap.

## 12. Kesimpulan

Dari pembuatan project CyberIncident API ini, saya belajar bagaimana membangun REST API menggunakan Flask, menghubungkan aplikasi dengan database, menggunakan ORM, membuat endpoint CRUD, serta melakukan pengujian melalui Postman dan pytest.

Walaupun masih sederhana, project ini sudah dapat digunakan sebagai contoh sistem pencatatan dan pengelolaan insiden keamanan siber berbasis REST API.