import requests

def SendPost(url, data):
    # Отправка POST-запроса
    response = requests.post(url, json=data)

    # Печать ответа
    print(response.json())

if __name__ == "__main__":
    # URL Flask-приложения
    url = 'http://127.0.0.1:5000/'

    # JSON данные
    data = { 
            "id": "1",
            "videoSrc": "https://dublvideos.blob.core.windows.net/dublvid-source/1-video.mp4", 
            "voiceSrc": "https://dublvideos.blob.core.windows.net/dublvid-source/1-voice.mp3", 
            "bgSoundSrc": "https://dublvideos.blob.core.windows.net/dublvid-source/1-bg.mp3"
    }

    SendPost(url, data)