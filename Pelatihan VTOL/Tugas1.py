import cv2 as cv

# Menentukan lebar dan tinggi frame video
frame_width = 640
frame_height = 480

# Membuat objek VideoWriter untuk merekam video
out = cv.VideoWriter('output.mp4', cv.VideoWriter_fourcc(*'MP4V'), 25, (frame_width, frame_height))

# Membuka kamera
cap = cv.VideoCapture(0)

while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()

    if ret:
        # Menampilkan frame
        cv.imshow('frame', frame)

        # Menulis frame ke dalam objek VideoWriter
        out.write(frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv.waitKey(1) == ord('q'):
        break

# Membersihkan semua objek dan menutup jendela
cap.release()
out.release()
cv.destroyAllWindows()
