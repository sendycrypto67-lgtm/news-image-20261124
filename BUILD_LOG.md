# BUILD LOG, news-image-20261124 v2

Tanggal build: 24 November 2026 (malam WIB).
Bounty: make.fun, Sum up 24 November's world news in one image.
Pot: $100 untuk 50 pemenang. Entri tutup 26 Nov 2026 00:00 UTC.
Alasan v2: v1 (submission 01a20b2b-0b33-76d0-a361-04bf72039021)
menempati rank 1971 dari 7302 di ronde 1 (skor 574512), jauh di luar
zona hadiah top 50. Aturan resubmit Sendy 23 Nov: bila posisi
tergeser setelah submit, kirim ulang versi yang lebih baik selama
kompetisi masih buka. v2 dihitung mulai ronde 2 (cutoff 25 Nov 00:00 UTC).

## Desain, dan bedanya dari v1

v1: hero NATO berupa pita lebar di atas, lalu grid 3+2 di bawah.
v2: layout dibalik total.

- Hero baru LIBYA di kolom kiri yang tinggi, bukan pita di atas.
  Gambar hero 520x288, headline tiga baris paling besar di halaman
  (56 px serif bold), caption dua baris.
- Kolom kanan berisi NATO di atas dan KOREA di bawah, ditumpuk
  vertikal, dipisah dari hero oleh garis vertikal tipis.
- Pita bawah berisi tiga cerita sejajar selebar penuh (CLIMATE,
  MEXICO, NVIDIA), masing-masing gambar pendek plus headline dan
  caption.
- Hierarki lebih kuat dari v1: headline hero 56 px dalam tiga baris
  (v1 satu baris), pemisah antar cerita lebih jelas (garis vertikal
  kolom, garis horizontal tebal sebelum pita bawah).
- Masthead tetap THE WORLD TODAY, baris tanggal TUESDAY 24 NOVEMBER
  2026, deck satu baris, footer sumber Reuters, AP, Times of India.
- Font adaptif: headline mengecil sampai muat, maksimal 3 baris
  (hero) atau 2 baris (lainnya). Semua caption lengkap, tidak ada
  yang terpotong.
- Tidak ada angka korban di mana pun, tidak ada spekulasi sebagai
  fakta, tidak ada em-dash di teks mana pun.

## Cerita (fakta sama seperti v1, terverifikasi)

1. LIBYA (hero): Ukraine sinks Russian warship in Libya. Sea drones
   strike a corvette in Benghazi port on Sunday, as the war spreads
   beyond Europe.
2. NATO: NATO sends spy planes to Poland. Early-warning aircraft
   deploy after missiles land on the eastern flank.
3. KOREA: Russian jet sparks Korea alert. Seoul briefly warns
   Ulleung Island after Russian aircraft enter its air defence zone.
4. CLIMATE: COP fallout, Pacific despair. Backlash in Australia as
   Pacific nations despair after talks fail.
5. MEXICO: Mexico captures top drug lord. Elite troops capture
   Chapo Isidro with US intelligence help.
6. NVIDIA: Huang back at Nvidia helm. Jensen Huang reinstated as CEO
   after board inquiry clears him.

## Ilustrasi

6 ilustrasi editorial flat BARU dibuat dengan media image tool,
semuanya tanpa teks, huruf, atau angka di dalam gambar, tidak ada
yang dipakai ulang dari v1:

1. Hero LIBYA. Korvet miring dan tenggelam di pelabuhan saat senja,
   asap mengepul, dua drone laut mendekat, crane pelabuhan dan
   matahari rendah di kejauhan.
2. NATO. Pesawat AWACS dengan piringan radar besar di atas badan
   pesawat, terbang di atas pedesaan.
3. KOREA. Pulau berbatu dengan mercusuar dan kubah radar, dua jet
   tempur menanjak di langit berawan.
4. CLIMATE. Pulau Pasifik rendah dengan palem dan rumah kayu, awan
   badai gelap, ombak membanjiri pantai.
5. MEXICO. Pasukan elit mengawal tahanan terborgol menuju helikopter
   pada malam hari, kendaraan lapis baja dan kaktus di sekitarnya.
6. NVIDIA. Pebisnis berjas kulit berjalan keluar dari pintu kaca
   kantor pusat teknologi saat matahari terbit, pola sirkuit di kaca.

Semua ilustrasi diperiksa visual sebelum dipakai. Perbaikan saat
review:

- Crop pertama NATO memotong bagian atas piringan radar, diperbaiki
  dengan titik pusat crop lebih tinggi (cy 0,30 ke 0,12) sehingga
  piringan terlihat utuh.
- Crop pertama KOREA memotong kedua jet tempur sampai hilang,
  diperbaiki dengan titik pusat crop lebih tinggi (cy 0,45 ke 0,08)
  sehingga jet, mercusuar, dan kubah radar terlihat.
- Crop pertama MEXICO memotong kepala para prajurit, diperbaiki
  dengan titik pusat crop lebih tinggi (cy 0,50 ke 0,22) sehingga
  kepala dan helikopter terlihat.
- Setelah perbaikan, komposisi akhir dicek lagi: semua elemen kunci
  terlihat, tidak ada teks atau bendera di ilustrasi mana pun.

## Compose

Compose memakai Python dan Pillow lewat script build-time di luar
repo (work-v2/build.py), script itu tidak masuk repo. Layout awal
meluber 20 px di bawah (pita bawah berakhir y=1002), diperbaiki
dengan mengecilkan header dan tinggi gambar (hero 296 ke 288,
gambar kanan 148 ke 140, gambar pita bawah 96 ke 84). Hasil akhir:
pita bawah berakhir y=988, garis footer y=994, teks footer y=1002.

## main.py

Ditulis dari nol berdasarkan spesifikasi, tanpa membaca main.py v1.
Validator dan copier, Python 3 standard library saja: cek magic PNG,
baca IHDR (dimensi maksimal 1024 tiap sisi, bit depth dan colour
type valid), cek ukuran file maksimal 1048576 byte, cek CRC32 semua
chunk, cek IEND di akhir file tanpa trailing bytes, lalu salin
byte-for-byte ke $MAKEFUN_OUTPUT_DIR/entry.png. Semua kegagalan
exit 1 dengan pesan ke stderr, termasuk bila MAKEFUN_OUTPUT_DIR
tidak diset. Tanpa network, deterministik.

## Verifikasi

- entry.png: 1024x1024, 594865 byte, di bawah batas 1 MiB.
- main.py dijalankan 2x ke direktori berbeda, sha256 output identik
  dengan file repo (lihat hasil di bawah).
- Tes negatif, semua ditolak exit 1: file bukan PNG, PNG melebihi
  batas byte, trailing bytes setelah IEND, IHDR 1200x1200,
  MAKEFUN_OUTPUT_DIR tidak diset.
- Baca visual entry.png akhir: masthead, tanggal, deck, hero LIBYA
  dominan, 5 cerita lain sesuai brief, footer sumber. Tanpa cacat
  teks, tanpa teks terpotong atau tumpang tindih, tanpa angka korban,
  tanpa em-dash.
- Repo-v2 berisi tepat 3 file: main.py, entry.png, BUILD_LOG.md.
  Tidak ada README.md atau LICENSE (ditambahkan koordinator).

## Hasil verifikasi

```
sha256 entry.png: 7423086f49df630a57d2a5ecc3e563a021ae9da5206d5cb389dedeccf7fe04a3
```

Dua run main.py ke direktori berbeda menghasilkan sha256 yang sama
dengan file repo di atas. Tes negatif (bukan PNG, oversize,
trailing bytes, dimensi 1200x1200, MAKEFUN_OUTPUT_DIR tidak diset)
semuanya ditolak dengan exit 1.
