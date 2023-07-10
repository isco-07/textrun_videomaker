import cv2
import numpy as np

# Размеры видео
width, height = 100, 100

# Создание объекта для записи видео
video_writer = cv2.VideoWriter("runtext_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height))

# Текст для бегущей строки
text = input()
pos_x = 100
# Цикл по времени для создания видео длиной 3 секунды
for t in np.arange(0, 3, 0.03):
    # Создание пустого изображения
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # Отрисовка текста на изображении
    cv2.putText(image, text, (pos_x, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (139, 219, 255), 2)
    pos_x -= 1 + int(0.4 * len(text))
    # Запись изображения в видео
    video_writer.write(image)

# Закрытие объекта записи видео
video_writer.release()
