import math

# import other services
from src.services.AudioManager import AudioManager
from src.services.ImageManager import ImageManager

# helpers function
from src.utils.helpers import get_formated_time

class MetadataManager():
    def __init__(self):
        
        self.audio_manager = AudioManager("src/models/songs")
        self.image_manager = ImageManager("assets/images")


    def get_file_id(self, file_name):
        """
        extract and return file's id
        """

        """
        file_name.split(";") = [id, name-artist.mp3]
        file_name.split(";")[0] = id
        """

        return file_name.split(";")[0]
    
    def get_song_name(self, file_name):
        """
        extract and return file's name
        """

        """
        file_name.split(";") = [id, name-artist.mp3]
        file_name.split(";")[0] = id
        file_name.split(";")[1] = name-artist.mp3
        file_name.split(";")[1].split("-") = [name, artist.mp3]
        file_name.split(";")[1].split("-")[0] = name
        """

        return (file_name.split(";")[1]).split("-")[0].replace("_", " ")
    
    def get_artist(self, file_name):
        """
        extract and return file's artist
        """

        """
        file_name.split(";") = [id, name-artist.mp3]
        file_name.split(";")[0] = id
        file_name.split(";")[1] = name-artist.mp3
        file_name.split(";")[1].split("-") = [name, artist.mp3]
        file_name.split(";")[1].split("-")[1] = artist.mp3
        (file_name.split(";")[1].split("-")[1]).split(".") = [artist, mp3]
        (file_name.split(";")[1].split("-")[1]).split(".")[0] = artist
        """

        return (file_name.split(";")[1].split("-")[1]).split(".")[0].replace("_", " ")

    def process_files(self, file_paths, file_names, image_paths, image_names, song_class):
        """
        extract metadata from file
        """
        
        song_objects_list = [] # store song objects

        try:
            for index, name in enumerate(file_names):
                
                # get medata from file name
                song_id = self.get_file_id(name)
                song_name = self.get_song_name(name)
                artist = self.get_artist(name)
                song_path = file_paths[index]

                # get information from file name
                file_duration = self.audio_manager.get_file_duration(song_path) # duration

                # correct duration format
                song_duration = get_formated_time(file_duration)

                # execute thumbnail list (ensure that file_names and image_names list has the same length)
                for index, image_name in enumerate(image_names):

                    if song_name == image_name:
                        thumbnail_path = image_paths[index]

                song_object = (song_class)(
                    song_id,
                    song_name,
                    artist,
                    song_duration,
                    song_path,
                    thumbnail_path,
                    # youtube link
                )

                song_objects_list.append(song_object)

            return song_objects_list
        
        except:
            return None
        
    