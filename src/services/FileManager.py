import os
import yt_dlp

from src.utils.helpers import generate_id

class FileManager():
    def __init__(self, ouput_folder = None):

        self.container_folder = ouput_folder

        # yt-dlp options for downloading MP3
        self.ydl_options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(self.container_folder, '%(title)s.%(ext)s'),
            'ffmpeg_location': r'C:\\ffmpeg\\bin',  # Path to FFmpeg's folder
        }

    def download_mp3_file(self, youtube_url):
        """
        Downloads audio from a YouTube URL as an MP3 file.

        Arguments:
            youtube_url (str): The YouTube video URL.

        Returns:
            str: Path to the downloaded MP3 file or an error message.
        """
        try:

            # Use yt-dlp to download the audio
            with yt_dlp.YoutubeDL(self.ydl_options) as ydl:
                info_dict = ydl.extract_info(youtube_url, download = True)
                file_path = ydl.prepare_filename(info_dict).replace('.webm', '.mp3')
                return file_path
            
        except Exception as e:
            return f"Error: {str(e)}"

    def format_file(self, file_path, name, artist):
        """
        correct file name
        """

        song_id = generate_id(os.listdir(self.container_folder))
        name = name.replace(" ", "_")
        artist = artist.replace(" ", "_")

        new_file_name = f"{song_id};{name}-{artist}.mp3"
        new_name = os.path.join("src\\models\\songs", new_file_name)

        # if the the new location is the same as the targed location but with a different file name,
        # the file name will be changed
        os.rename(file_path, new_name) # change file name to correct format

        file_path = os.path.join("src\\models\\songs", new_file_name)   
        return (file_path, song_id)
    


