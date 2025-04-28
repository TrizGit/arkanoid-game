# Presentasi Proyek “Arkanoid” Game

## Tujuan Proyek
Mengembangkan sebuah permainan 2D yang sederhana namun menarik.
## Deskripsi
Pemain dapat mengontrol platform untuk memantulkan bola dan menghancurkan musuh di layar.

## Pada permainan ini, saya menggunakan...
### Class
 - Area  
Parent class untuk mengelola dimensi objeck dan deteksi tabrakan
```py
class Area():
    def __init__(self, x, y, w, h, color=None):
        self.rect = pygame.Rect(x, y, w, h)
        if color:
            self.fill_color = color
        else:
            self.fill_color = bg
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
```
- Picture  
Child class dari `Area` untuk menangani objek berbasis gambar.
```py
class Picture(Area):
    def __init__(self, filename, x=0, y=0, w=0, h=0):
        Area.__init__(self, x=x, y=y, w=w, h=h, color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
```
- Label  
Child class dari `Area` untuk menampilkan teks.
```py
class Label(Area):
    def setText(self, text, fSize, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fSize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
```
### Objeknya
- Platform  
![platform](/platform.png)  
Platform dikontrol oleh pemain dengan menekan keyboard, `A` untuk bergerak ke kiri dan `D` untuk bergerak ke kanan.
- Bola  
![bola](/ball.png)  
Objek utama untuk interaksi permainan.
- Monster  
![monster](/enemy.png)  
Rintangan yang harus dihancurkan oleh pemain.
### Logika Permainan
- Pegerakan bola dengan perubahan arah berdasarkan tabrakan
- Kondisi menang kalah berdasarkan hasil permainan
- Handle platform dengan keyboard
## Pengembangan proyek masa depan
1. Menambahkan animasi ketika terjadi tabrakan
2. Suara/Background musik selama game dimainkan
3. Level dengan tingkat kesulitan yang bervariasi
## Screenshot
![ss_1](/pic_1.png)  
![ss_2](/pic_2.png)