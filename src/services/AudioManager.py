"""

AudioManager class is created to porvide audio controls to mp3 files (play, pause, stop, skip, etc.)

"""

import os
import math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "True" # hide pygame default support prompt
import pygame
from mutagen.mp3 import MP3

from src.utils.helpers import sort_by_id

class AudioManager():
    def __init__(self, folder_path):
        
        # call pygame constructor
        pygame.init()
        pygame.mixer.init(frequency = 48000)

        self.is_statrted = False

        self.folder = folder_path
        self.isRunning = False # state
        self.time_skipped = 0 # time skipped to
        self.offset = 0 # old time point

        # song ended event
        self.MUSIC_END = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.MUSIC_END)

    def load_file(self, file_path):
        """load file and ready to play"""
        file_path_str = str(file_path)
        pygame.mixer.music.load(file_path_str)

    def play(self):
        """play file"""
        self.isRunning = True
        pygame.mixer.music.play()

    def pause(self):
        """pause file"""
        pygame.mixer.music.pause()

    def resume(self):
        """unpause file"""
        self.isRunning = True
        pygame.mixer.music.unpause()

    def skip_to(self, time_point):
        """skip to a particular time stamp in the file"""
        self.time_skipped = time_point
        self.offset = pygame.mixer.music.get_pos() / 1000
        pygame.mixer.music.set_pos(time_point)

    def stop(self):
        """stop file"""
        self.isRunning = False
        pygame.mixer.music.stop()

    def set_volume(self, value):
        """ change voume of the current file"""
        # set_volume() receive value from 0 -> 1
        pygame.mixer.music.set_volume(value / 100)

    def reset_time(self):
        """reset time skipped and old time point"""
        self.time_skipped = 0
        self.offset = 0
        pygame.mixer.music.set_pos(0.0)

    def check_ended(self):
        for event in pygame.event.get():
            if event.type == self.MUSIC_END:
                self.isRunning = False
                return True
        return False
    
    def get_time_stamp(self):
        start_from_init = pygame.mixer.music.get_pos() / 1000

        if self.time_skipped == 0 and self.offset == 0: # song start
            return round(start_from_init)
        
        else: # when running
            return round(start_from_init +  self.time_skipped - self.offset)

    def get_file_duration(self, file_path):
        try:
            audio = MP3(file_path)
            return math.floor(audio.info.length)  # Duration in seconds
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_file_list(self):
        file_list = []

        # loop through the folder
        unsorted_files = os.listdir(self.folder)

        # sort files in index ascending order
        files = sort_by_id(unsorted_files)

        for file_path in files:

            if file_path.endswith(".mp3"):
                file_list.append(os.path.join("src\\models\\songs", file_path))

        return file_list, files


    
    
