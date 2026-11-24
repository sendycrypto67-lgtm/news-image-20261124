# BUILD LOG, news-image-20261124

Tanggal build: 24 November 2026.
Bounty: make.fun, Sum up 24 November's world news in one image.
Pot: $100 untuk 50 pemenang. Entri tutup 26 Nov 2026 00:00 UTC.
Status API saat dicek: open, accepting, gratis, 903 submissions.

## Desain

Mengikuti formula v2 edisi 20261123 yang terbukti lebih baik: hierarki
koran klasik, bukan grid rata.

- Halaman krem, masthead serif THE WORLD TODAY, baris tanggal
  TUESDAY 24 NOVEMBER 2026, lalu deck miring satu baris.
- HERO STORY dominan di atas: NATO, ilustrasi lebar penuh dan headline
  satu baris paling besar.
- 5 cerita lain di bawah dalam grid 3 di baris pertama dan 2 di baris
  kedua, masing-masing dengan tag kategori merah kecil, headline tebal,
  dan sub-caption.
- Font adaptif: headline mengecil sampai muat, maksimal 3 baris.
  Sub-caption grid dibungkus maksimal 2 baris supaya tetap terbaca pada
  lebar kolom, teksnya lengkap tanpa dipotong.
- Footer: Six stories from 24 November 2026 | Sources: Reuters, AP,
  Times of India.
- Tidak ada angka korban di mana pun, tidak ada spekulasi sebagai fakta,
  tidak ada em-dash di teks mana pun.

## Ilustrasi

6 ilustrasi editorial flat baru dibuat dengan media image tool, semuanya
tanpa teks, huruf, atau angka di dalam gambar:

1. Hero NATO. Pesawat early-warning AWACS dengan piringan radar besar di
   atas badan pesawat, terbang di atas pedesaan Polandia.
2. KOREA. Dua jet tempur lepas landas di atas pulau berbatu dengan mercusuar
   dan stasiun radar di bukit.
3. LIBYA. Kapal perang korvet di pelabuhan saat senja, drone laut kecil
   mendekat dengan asap mengepul.
4. CLIMATE. Pulau Pasifik rendah dengan palem dan rumah kayu, awan badai
   gelap dan ombak naik ke pantai.
5. MEXICO. Pasukan elit mengawal tahanan terborgol menuju helikopter pada
   malam hari di jalan kota Meksiko.
6. NVIDIA. Pebisnis berjas berjalan keluar dari pintu kaca kantor pusat
   perusahaan teknologi saat matahari terbit.

Semua ilustrasi diperiksa visual sebelum dipakai. Perbaikan saat review:
crop hero pertama memotong piringan radar AWACS, diperbaiki dengan titik
pusat crop lebih tinggi sehingga piringan radar terlihat jelas. Crop
NVIDIA pertama memotong sosok pebisnis, diperbaiki dengan titik pusat crop
lebih rendah.

## Compose

Compose memakai Python dan Pillow lewat script build-time di luar repo
(work/build.py), script itu tidak masuk repo. Layout awal meluber 26 px
di bawah (footer berakhir di y=1050), diperbaiki dengan mengecilkan
tinggi gambar: hero 186 ke 170, baris 1 ke 100, baris 2 ke 112.
Hasil akhir: footer berakhir di y=1016 dari 1024.

## main.py

Ditulis dari nol berdasarkan spesifikasi, tanpa membaca main.py edisi
sebelumnya. Validator dan copier, Python 3.13 standard library saja:
cek magic PNG, baca IHDR (dimensi maksimal 1024), cek ukuran file
maksimal 1048576 byte, cek CRC chunk dan IEND di akhir, lalu salin
byte-for-byte ke $MAKEFUN_OUTPUT_DIR/entry.png. File bukan PNG atau
melebihi batas ditolak dengan exit 1. Tanpa network, deterministik.

## Verifikasi

- entry.png: 1024x1024, 769050 byte, di bawah batas 1 MiB.
- main.py dijalankan 2x ke direktori berbeda, sha256 output identik
  dengan file repo (lihat hasil di bawah).
- Tes negatif: file bukan PNG ditolak exit 1, PNG 1200x1200 ditolak
  exit 1.
- Repo berisi tepat 5 file: main.py, entry.png, BUILD_LOG.md,
  README.md, LICENSE.

## Hasil verifikasi

```
sha256 entry.png: 092e2dc8ee9af1f39bf57097efc977666f3a562fd93d324b623106428a4c40a7
```

Dua run main.py ke direktori berbeda menghasilkan sha256 yang sama dengan
file repo di atas. Tes negatif (bukan PNG, PNG 1200x1200) keduanya ditolak
dengan exit 1.

## Verifikasi koordinator (24 Nov ~08:30 WIB)
- Baca visual entry.png: masthead, tanggal TUESDAY 24 NOVEMBER 2026, deck, hero NATO (AWACS dengan piringan radar jelas), 5 cerita bawah (Korea, Libya, Climate, Mexico, NVIDIA), footer sumber. Tanpa cacat teks, tanpa angka korban, tanpa em-dash.
- main.py 2x run ke dir berbeda, sha256 output identik dengan file repo (092e2dc8...). Tes negatif non-PNG exit 1 (bad magic bytes).
- Edit koordinator: tambah cek trailing bytes setelah IEND di read_chunks (output tidak berubah, sha256 tetap 092e2dc8).
- README 4x make.fun (3 badge), LICENSE ada baris SPDX.
