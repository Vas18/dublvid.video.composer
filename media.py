from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import requests
from urllib.parse import urlparse

#Получаем имя файла
def GetFilename(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    filename = path.split('/')[-1]
    return filename

def DownloadData(url):
    # Отправляем GET-запрос для скачивания данных
    response = requests.get(url)

    # Проверяем статус ответа
    if response.status_code == 200:
        #Формируем путь до файла
        save_path = f"media/{GetFilename(url)}"
        
        # Открываем файл для записи
        with open(save_path, 'wb') as f:
            # Записываем данные из ответа в файл
            f.write(response.content)
        print("Скачивание завершено. Данные сохранены в", save_path)
        return save_path
    else:
        print("Ошибка при скачивании данных:", response.status_code)

#Функция для наложения голоса и музыки на видео
def MakeVideo(video_path, voice_path, background_music_path):
    #Формирование названия
    output_path = video_path.replace("video", "result")

    #Считываем видео
    video_clip = VideoFileClip(video_path)

    #Считываем голос
    voice_clip = AudioFileClip(voice_path)

    #Считываем фон, обрезаем его, и уменьшаем громкость до 10%
    background_music_clip = AudioFileClip(background_music_path)
    background_music_clip = background_music_clip.set_duration(video_clip.duration)
    background_music_clip = background_music_clip.volumex(0.1)

    #Собираем аудио в одно
    new_audioclip = CompositeAudioClip([voice_clip, background_music_clip])

    #Убираем звук у оригинального видео
    video_clip = video_clip.set_audio(None)

    #Накладываем аудио и сохраняем файл
    final_video_clip = video_clip.set_audio(new_audioclip)
    final_video_clip.write_videofile(output_path, codec='libx264')

    return True

