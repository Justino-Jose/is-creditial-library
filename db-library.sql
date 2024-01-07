
DROP DATABASE db_lib;

CREATE DATABASE db_lib;

USE db_lib;


CREATE TABLE user(
	id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nama_user VARCHAR(50),
    tanggal_lahir DATE,
    pekerjaan VARCHAR(50),
    alamat VARCHAR(100)
);


CREATE TABLE buku(
	id_buku INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nama_buku VARCHAR(50),
    kategori VARCHAR(50),
    stock INT
);


CREATE TABLE peminjaman(
	id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	id_buku INT,
    nama_user VARCHAR(50),
    nama_buku VARCHAR(50),
    tanggal_pinjam DATE,
    tanggal_kembali DATE
);

ALTER TABLE peminjaman ADD FOREIGN KEY (id_user) REFERENCES user(id_user);
ALTER TABLE peminjaman ADD FOREIGN KEY (id_buku) REFERENCES buku(id_buku);
ALTER TABLE user AUTO_INCREMENT=15;

INSERT INTO user VALUES (01, 'Andi', '1995-02-15', 'Mahasiswi', 'Jakarta Pusat');
INSERT INTO user VALUES (02, 'Bambang', '1993-02-15', 'Pegawai', 'Cilincing');
INSERT INTO user VALUES (03, 'karlos', '1980-04-24', 'CEO', 'Sawangan');
INSERT INTO user VALUES (04, 'Davin', '2000-10-03', 'Pelajar', 'Grogol');
INSERT INTO user VALUES (05, 'Kino', '1986-06-27', 'Penganguran', 'Tanjung Barat');
INSERT INTO user VALUES (06, 'Ronald', '1998-08-03', 'Pengangguran', 'Pondok Kopi');
INSERT INTO user VALUES (07, 'Axel', '1989-01-17', 'CEO', 'Kalibata');
INSERT INTO user VALUES (08, 'Tino', '1990-11-04', 'Pegawai Swasta', 'Cibubur');
INSERT INTO user VALUES (09, 'John', '1978-09-04', 'Wiraswasta', 'Rawamangun');
INSERT INTO user VALUES (10, 'Kido', '1995-09-02', 'Mahasiswa', 'Plumpang');
INSERT INTO user VALUES (11, 'Linda', '2002-11-03', 'Pelajar', 'Tebet');
INSERT INTO user VALUES (12, 'Adrian', '1990-05-29', 'Pegawai BUMN', 'Cawang');
INSERT INTO user(nama_user, tanggal_lahir, pekerjaan, alamat) VALUES ('Landy', '2005-09-01', 'Pelajar', 'Duren Sawit');

INSERT INTO buku VALUES (1001, 'Belajar Python', 'Teknologi', 4);
INSERT INTO buku VALUES (1002, 'Naga Emosional ', 'Novel', 1);
INSERT INTO buku VALUES (1003, 'Cantik Itu Dosa', 'Novel', 2);
INSERT INTO buku VALUES (1004, 'Rich Dad Poor Dad', 'Investasi', 1);
INSERT INTO buku VALUES (1005, 'Laa Tazhan', 'Agama', 2);
INSERT INTO buku VALUES (1006, 'Guns, Germs, and Steel', 'Sejarah', 4);
INSERT INTO buku VALUES (1007, '7 Habits', 'Self-Development', 3);
INSERT INTO buku VALUES (1008, 'Belajar Technical Analysis', 'Invenstasi', 1);
INSERT INTO buku VALUES (1009, 'Data Wrangling in SQL', 'Teknologi', 3);



SELECT * FROM buku;
WHERE nama_buku LIKE '%Belajar%';

UPDATE buku SET stock = stock - 1
WHERE id_buku = 1001;
