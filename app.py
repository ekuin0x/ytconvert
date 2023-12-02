from flask import Flask, render_template, request
import yt_dlp
from contextlib import redirect_stdout
from pathlib import Path
import io
from pydub import AudioSegment


app = Flask(__name__)

@app.route('/')
def index() :

    youtube_id = "https://www.youtube.com/watch?v=ISOkbRMDFUI&ab_channel=Amadeo%C4%8Cela"
    ctx = {
        "outtmpl": "-",
        'logtostderr': True
    }
    buffer = io.BytesIO()
    with redirect_stdout(buffer), YoutubeDL(ctx) as foo:
        foo.download([youtube_id])

    data = AudioSegment.from_file(buffer, format="mp4")
    return 'YESSSS'
    #data.export("hello.mp3", format='mp3')

    return render_template("index.html")

if __name__ == "__main__" :
    app.run()