from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

#Функция для наложения голоса и музыки на видео
def MakeVideo(video_path, voice_path, background_music_path, output_path):
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

# Пример использования функции
MakeVideo("media/1-video.mp4", "media/1-voice.mp3", "media/1-bg.mp3", "media/output_video.mp4")
