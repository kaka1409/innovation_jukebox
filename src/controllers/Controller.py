# packages
import sys
import time

from random import randint

# libs
from PyQt5.QtCore import QTimer

# views
from src.views.MainWindow import MainWindow
from src.views.LoadingScreen import LoadingScreen

# services
from src.services.AudioManager import AudioManager
from src.services.ImageManager import ImageManager
from src.services.FileManager import FileManager
from src.services.MetadataManager import MetadataManager

# models
from src.models.Song import Song

# utils
from src.utils.helpers import get_formated_time

"""
the main controller that will operate everything
"""

class Controller():
    def __init__(self):
        
        # view
        self.view_window = MainWindow()

        # models
        self.model_song = Song # hasn't called the constructor

        # service
        self.service_audio = AudioManager("src/models/songs")
        self.service_image = ImageManager("assets/images")
        self.service_file = FileManager("src/models/songs")
        self.service_metadata = MetadataManager()

        # handle data flow between view, service and models
        self.handle_event_connections()
        self.handle_files()

    def handle_event_connections(self):
        """
        Connect user's events captured by view's widgets to specific functions provided 
        by service to update the state of song objects, song list, etc.
        """

        # Access UI components from view_window
        
        # song's control
        control_frame = self.view_window.player_container.control_frame
        play_button = control_frame.play_button
        pause_button = control_frame.pause_button
        loop_button = control_frame.loop_button
        previous_button = control_frame.previous_button
        next_button = control_frame.next_button
        shuffle_button = control_frame.shuffle_button
        
        # Song progress
        progress_bar = self.view_window.player_container.progress_bar.song_progress

        # options
        volume_bar = self.view_window.player_container.volume_bar

        # Song list
        song_list = self.view_window.menu_frame.song_list_frame.song_list
        confirm_button = self.view_window.menu_frame.menu_footer.confirm_button
        remove_button = self.view_window.menu_frame.menu_footer.remove_button

        # Search bar
        search_bar = self.view_window.menu_frame.search_bar
        search_button = search_bar.search_icon
        reset_button = search_bar.remove_icon
        options_list = search_bar.options_frame.options_list

        # Connect events
        play_button.clicked.connect(
            lambda: self.handle_play_button_event(timer, play_button)
        )

        pause_button.clicked.connect(
            lambda: self.handle_pause_button_event(timer, pause_button)
        )

        loop_button.clicked.connect(
            lambda: self.handle_loop_button_event(loop_button)
        )

        previous_button.clicked.connect(
            lambda: self.handle_previous_button_event(song_list)
        )

        next_button.clicked.connect(
            lambda: self.handle_next_button_event(song_list)
        )

        shuffle_button.clicked.connect(
            lambda: self.handle_shuffle_button_event(shuffle_button)
        )
        
        progress_bar.valueChanged.connect(
            lambda: self.handle_skip_event(progress_bar, pause_button)
        )
        
        volume_bar.valueChanged.connect(
            lambda: self.handle_volume_change(volume_bar)
        )
        
        song_list.itemSelectionChanged.connect(
            lambda: self.handle_song_selection(song_list)
        )

        confirm_button.clicked.connect(
            lambda: self.handle_song_addtion(confirm_button)
        )

        remove_button.clicked.connect(
            lambda: self.handle_song_removal(remove_button, song_list)
        )
        
        search_button.clicked.connect(
            lambda: self.handle_searching(search_button, song_list, options_list)
        )
        
        reset_button.clicked.connect(
            lambda: self.handle_reset_search_input(reset_button, song_list)
        )
        
        options_list.itemSelectionChanged.connect(
            lambda: self.handle_searching_options(options_list)
        )
        
        # Initialize timer for updating song progress
        timer = QTimer()
        timer.timeout.connect(
            lambda: self.handle_song_progress(
                timer, progress_bar, loop_button, shuffle_button,
                play_button, next_button, song_list
            )
        )


    #******************************SONG CONTROL FEATURES******************************#

    def handle_play_button_event(self, timer, play_button):
        """play event"""
        
        # update stacked layout
        stacked_button = play_button.parent().layout
        stacked_button.setCurrentIndex(1)

        # play audio
        if self.service_audio.isRunning:
            self.service_audio.resume()
        else: 
            self.service_audio.play()

        # start updating progress bar
        timer.start(1000)

        # start rotate animation
        thumbnail = self.view_window.player_container.thumbnail
        thumbnail.start_rotating()

    def handle_pause_button_event(self, timer, pause_button):
        """pause event"""

        # update stacked layout
        stacked_button = pause_button.parent().layout
        stacked_button.setCurrentIndex(0)

        # pause audio
        self.service_audio.pause()

        # stop updation progress bar
        timer.stop()

        # pause rotate animation
        thumbnail = self.view_window.player_container.thumbnail
        thumbnail.pause_rotating()

    def handle_loop_button_event(self, loop_button):
        """reload the current file time, progress bar and icon"""
        
        # update loop button icon
        control_frame = loop_button.parent()
        control_frame.update_loop_icon()

    def handle_previous_button_event(self, song_list):
        """handle event when previous button is clicked"""
        current_index = song_list.selectedIndexes()[0].row()

        if current_index == 0:

            last_item_index = song_list.count() - 1 # get the index of the last item
            song_list.setCurrentRow(last_item_index) # set the selection to the last item
        else:

            previous_index = current_index - 1 
            song_list.setCurrentRow(previous_index)
        
    def handle_next_button_event(self, song_list):
        """handle event when next button is clicked"""

        current_index = song_list.selectedIndexes()[0].row() # get the index of the current selection
        last_item_index = song_list.count() - 1 # get the index of the last item

        if current_index == last_item_index:

            song_list.setCurrentRow(0) # set the selection to the first item in the list
        else:

            next_index = current_index + 1 
            song_list.setCurrentRow(next_index)

    def handle_shuffle_button_event(self, shuffle_button):
        """update shuffle state"""
        
        # get the control frame
        control_frame = shuffle_button.parent()

        # update button's icon
        control_frame.update_shuffle_icon()

    #******************************SONG OPTIONS FEATURES******************************#

    def handle_volume_change(self, volume_bar):
        """ handle volume change event"""

        # select widget (volume bar's value and option frame)
        volume_value = volume_bar.value()
        options_frame = volume_bar.parent().parent().options_frame
        
        # updade volume icon
        options_frame.volume_change(volume_value)

        # change volume of the current file
        self.service_audio.set_volume(volume_value)

    #******************************SONG PROGRESS FEATURE******************************#

    def handle_song_progress(
        self, timer, progress_bar, loop_button, 
        shuffle_button, play_button, next_button, song_list
    ):
        """
        update progress bar and current time
        """

        # get progress bar frame
        progress_bar_frame = progress_bar.parent()

        # mapping file duration to progress bar value
        song_duration = self.service_audio.get_file_duration(self.current_song.path)
        time_point = self.service_audio.get_time_stamp()
        progress_bar_max = progress_bar.maximum()

        new_value = round(time_point * (progress_bar_max / song_duration))

        # print(f"""
        # time point: {time_point}
        # time skipped: {self.service_audio.time_skipped}
        # offset: {self.service_audio.offset}""")


        # update progress bar
        progress_bar_frame.change_value(new_value)

        # update current time
        current_time_label = progress_bar_frame.current_time
        current_time_label.setText(get_formated_time(time_point)) 
        
        
        # check if the song has ended (check the current value of song's progress reached its max)
        if time_point == song_duration or new_value == progress_bar_max:
            
            # reset pygame mixer
            self.service_audio.reset_time()
            
            # options
            loop_option = loop_button.parent().is_looped
            shuffle_option = shuffle_button.parent().is_shuffled

            # if the loop option is on
            if loop_option:
                """This block code will be executed if is_looped is on"""

                # reset progress bar
                progress_bar_frame.change_value(0)
                current_time_label.setText("0:00")

                # reload current song
                self.service_audio.load_file(self.current_song.path)

                # play the current song
                self.service_audio.play()

                # update play button
                stacked_button = play_button.parent().layout
                stacked_button.setCurrentIndex(1)

                # click play button
                play_button.click()

            # if the shuffle option is on
            elif shuffle_option:
                """This block code will be executed if is_shuffled is on"""

                end_index = song_list.count() - 1 # index of the last item
                current_song_index = song_list.selectedIndexes()[0].row()

                # get random value ranging from 0 to the index of the last item in the song list
                random_index = randint(0, end_index)
                
                # create a new random if the current random value is the same as the current song index
                while random_index == current_song_index:

                    random_index = randint(0, end_index)

                song_list.setCurrentRow(random_index)

                # click play button
                play_button.click()

            # if no options is on this block code will be executed
            else:

                # stop updating 
                timer.stop()

                # reset to play button
                stacked_button = play_button.parent().layout
                stacked_button.setCurrentIndex(0)

                # stop rotate animation
                thumbnail = self.view_window.player_container.thumbnail
                thumbnail.pause_rotating()

                # go to next song as default
                next_button.click()

                # click play button
                play_button.click()
    
    def handle_skip_event(self, progress_bar, pause_button):
        """update song progress bar according to user skip"""

        if not progress_bar.is_programmic_changed:

            pause_button.click()

            song_duration = self.service_audio.get_file_duration(self.current_song.path)
            current_time = song_duration * (progress_bar.value() / progress_bar.maximum())

            current_time_label = progress_bar.parent().current_time
            current_time_label.setText(get_formated_time(current_time))

            if self.service_audio.is_statrted:
                self.service_audio.skip_to(current_time)
            else:
                self.service_audio.play()
                self.service_audio.pause()
                self.service_audio.skip_to(current_time)
                self.service_audio.is_statrted = True

    #******************************SONG LIST FEATURE******************************#

    def handle_files(self):
        """
        execute files, file_path, image_paths to give the correct format to song objects
        """

        file_paths, file_names = self.service_audio.get_file_list()
        image_paths, image_names = self.service_image.get_image_list(
            self.service_image.song_thumbnails_directory
        )

        # passing metadata from file names to song objects
        song_objects_list =  self.service_metadata.process_files(
            file_paths,
            file_names,
            image_paths,
            image_names,
            self.model_song # Song() class
        )

        self.handle_song_objects(song_objects_list)

    def handle_song_objects(self, song_objects_list):
        """
        get information from song objects and update it to song list in view (UI)
        """

        song_list_frame = self.view_window.menu_frame.song_list_frame
        song_list = self.view_window.menu_frame.song_list_frame.song_list

        # loop through song object list
        for song_object in song_objects_list:
            
            # add song object information to song frame
            song_frame = song_list_frame.create_song_frame(
                song_object.name,
                song_object.artist,
                song_object.thumbnail,
            )

            # add song frame to layout
            song_list_frame.add_song_frame(song_frame, song_object)

        # set the first song is selected as default
        song_list.item(0).setSelected(True)

    def handle_song_selection(self, song_list):
        """update player frame when another song is selected"""

        selected_song = song_list.selectedItems()[0]
        song_object = selected_song.object_key
        self.current_song = song_object

        # Stop current song
        self.service_audio.stop()
        self.service_audio.is_statrted = False

        # Load new song
        self.service_audio.load_file(song_object.path)

        # Update UI components
        player_container = self.view_window.player_container
        player_container.thumbnail.change_thumbnail(song_object.thumbnail)
        player_container.song_name.setText(song_object.name)
        player_container.artist_name.setText(song_object.artist)
        
        # Reset time display and progress
        player_container.progress_bar.current_time.setText("0:00")
        player_container.progress_bar.change_value(0)
        player_container.progress_bar.end_time.setText(song_object.duration)

        # Reset controls
        player_container.control_frame.stack_button_frame.layout.setCurrentIndex(0)

        # reset thumbnail animation
        player_container.thumbnail.reset_animation()
        
    def handle_song_addtion(self, confirm_button):
        """
        update song list when a new song is added
        """

        # menu footer
        menu_footer = self.view_window.menu_frame.menu_footer

        # add window inputs
        song_name_input = menu_footer.song_name_input
        artist_name_input = menu_footer.artist_input
        song_link_input = menu_footer.link_input

        # get song inputs
        song_name = song_name_input.text()
        artist_name = artist_name_input.text()
        song_link = song_link_input.text()


        # get a random placeholder thumbnail
        placeholder_thumbnail = self.service_image.get_placeholder_thumbnail()

        song_list_frame = self.view_window.menu_frame.song_list_frame

        # create the song_frame
        song_frame = song_list_frame.create_song_frame(
            song_name,
            artist_name,
            placeholder_thumbnail
        )
        
        # download file from youtube link
        downloaded_path = self.service_file.download_mp3_file(song_link)

        # format the file name
        file_name_path, song_id = self.service_file.format_file(
            downloaded_path,
            song_name,
            artist_name
        )

        # the song duration
        file_duration = self.service_audio.get_file_duration(file_name_path)
        song_duration = get_formated_time(file_duration)

        # create the song object
        song_object = self.model_song(
            song_id,
            song_name,
            artist_name,
            song_duration,
            file_name_path,
            placeholder_thumbnail,
            song_link
        )

        # add the song frame to song list
        song_list_frame.add_song_frame(song_frame, song_object)

        # hide the pop up window
        menu_footer.close_add_song_window()

        # clear the inputs
        song_name_input.clear()
        artist_name_input.clear()
        song_link_input.clear()

        # select the added song
        song_list = song_list_frame.song_list
        added_index = song_list.count() - 1
        song_list.setCurrentRow(added_index)

    def handle_song_removal(self, remove_button, song_list):
        """
        update song list when a song is deleted
        """

        current_index = song_list.currentIndex().row()
        song_list.takeItem(current_index)

        # selected_song = song_list.selectedItems()[0]
        # song_object = selected_song.object_key

        # delete song file
        # self.service_file.delete_file(song_object.path)
    
    #******************************SEARCHING FEATURE******************************#

    def handle_searching(self, search_input, song_list, options_list):
        """Handle searching function when user input in search bar changes."""
        
        # Get the search input from user
        search_query = search_input.parent().get_search_input()

        # Check which option is chosen, search by song name or artist
        search_by = 'name' if options_list.is_searching_by_name else 'artist'

        # Iterate through the song list, compare the search query with the song name or artist (depending on the option)
        for index in range(song_list.count()):
            item = song_list.item(index)
            attribute = getattr(item.object_key, search_by)

            # Normalize and compare the strings
            if search_query not in attribute.replace(" ", "").lower():
                item.setHidden(True)
            else:
                item.setHidden(False)

        # Check if no song is found a message will be displayed
        song_list_container = song_list.parent()
        song_list_container.message.setVisible(song_list_container.check_list_is_visible())

    def handle_searching_options(self, options_list):
        """handle changing the state as options changed"""

        # get current option's index
        current_option_index = options_list.selectedIndexes()[0].row()

        if current_option_index == 0:
            options_list.is_searching_by_name = True
            options_list.is_searching_by_artist = False
        elif current_option_index == 1:
            options_list.is_searching_by_name = False
            options_list.is_searching_by_artist = True

    def handle_reset_search_input(self, reset_button, song_list):
        """After clicking the button, it will reset the state of the search input and song list"""

        # clear all text in the search input feild
        search_input = reset_button.parent()
        search_input.clear()

        # number of songs in song list
        song_list_length = song_list.count()

        # display all songs to get back to the default state
        for index in range(song_list_length):

            song_item = song_list.item(index)

            # set hidden state of song to false
            song_item.setHidden(False)

        # hide the message 
        song_list.parent().message.setVisible(False)

        # hide the reset button
        reset_button.hide()






    


