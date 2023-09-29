from youtubesearchpython import VideosSearch
from pytube import YouTube
from pathlib import Path

AUDIO_ROOT: Path = Path(".") / "audios"

def download_first_audio(name: str) -> Path:
    videosSearch = VideosSearch(name, limit = 1)
    link = videosSearch.result()["result"][0]["link"]
    return Path(YouTube(link).streams.filter(only_audio=True).first().download(output_path=AUDIO_ROOT))
