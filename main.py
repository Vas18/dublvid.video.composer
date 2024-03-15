from flask import Flask, request, jsonify
from media import MakeVideo
from send_request import SendPost
from dotenv import load_dotenv
import os
from connectAZ import Azure

app = Flask(__name__)

@app.route('/', methods=['POST'])
def GetPost():
    # Получаем данные из JSON-запроса
    data = request.json

    #Объявляем класс
    AZ = Azure()

    # Пример обработки данных
    video_id = data.get('id')
    output_src = f"media/{video_id}.mp4"
    video_src = AZ.DownloadBlob(data.get('videoSrc'))
    voice_src = AZ.DownloadBlob(data.get('voiceSrc'))
    bg_sound_src = AZ.DownloadBlob(data.get('bgSoundSrc'))
    
    # Здесь вы можете выполнить обработку данных, например, обработать видео
    result = MakeVideo(video_path=video_src,voice_path=voice_src, background_music_path=bg_sound_src, output_path=output_src)
    print(result)
    load_dotenv()
    url = os.getenv("RESULT_URL")
    data = {'id': video_id, 'resultUrl': result}
    SendPost(url, data)

    # Возвращаем ответ
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)

