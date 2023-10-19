from youtubesearchpython import VideosSearch
from pytube import YouTube
from pathlib import Path

from cache import cached

AUDIO_ROOT: Path = Path(".") / "audios"

def remove_old(path):
    path.unlink()

def get_link(name):
    videosSearch = VideosSearch(name, limit = 1)
    return videosSearch.result()["result"][0]["link"]

@cached(20, on_expiration=remove_link)
def download_audio(link):
    return Path(YouTube(link).streams.filter(only_audio=True).first().download(output_path=AUDIO_ROOT))

def download(name):
    return download_audio(get_link(name))

