from flask import Flask, request, jsonify
from media import MakeVideo, DownloadData
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def GetPost():
    # Получаем данные из JSON-запроса
    data = request.json

    # Пример обработки данных
    video_id = data.get('id')
    video_src = DownloadData(data.get('videoSrc'))
    voice_src = DownloadData(data.get('voiceSrc'))
    bg_sound_src = DownloadData(data.get('bgSoundSrc'))
    
    # Здесь вы можете выполнить обработку данных, например, обработать видео
    MakeVideo(video_src, voice_src, bg_sound_src)

    # Возвращаем ответ
    response = {'id': video_id}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)

