import cv2

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

# Mendapatkan ukuran frame dari kamera
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Mendefinisikan codec dan membuat objek VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('keluaran.mp4', fourcc, 20.0, (width, height))

while(cap.isOpened()):
    # Membaca frame dari kamera
    ret, frame = cap.read()

    if ret == True:
        # Menulis frame ke file video
        out.write(frame)

        # Menampilkan frame di jendela
        cv2.imshow('frame',frame)

        # Keluar dari loop jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Membebaskan kamera dan objek VideoWriter
cap.release()
out.release()

# Menutup semua jendela
cv2.destroyAllWindows()
