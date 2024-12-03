class Song():
    def __init__(
            self,
            id = None,
            name = "Unknown",
            artist = "Unknown",
            duration = "0:00",
            path = None,
            thumbnail = None,
            link = None
        ):

        self.id = id
        self.name = name
        self.artist = artist
        self.duration = duration
        self.path = path
        self.thumbnail = thumbnail
        self.link = link
        self.playlist = None # future
        self.genre = None # future

        self.is_favorite = False # default
        self.is_selected = False # set default as not selected


    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_duration(self):
        return self.duration

    def get_path(self):
        return self.path

    def get_thumbnail(self):
        return self.thumbnail

    def get_link(self):
        return self.link

    # future
    # def get_playlist(self):
    #     return self.playlist

    # future
    # def get_genre(self):
    #     return self.genre

    def set_selected(self):
        self.is_selected = not self.is_selected
    def set_thumbnail(self, thumbnail): # future
        self.thumbnail = thumbnail

    def set_favorite(self, is_favorite):
        self.is_favorite = is_favorite

    # future
    # def set_playlist(self, playlist):
    #     self.playlist = playlist

    # def set_genre(self, genre):
    #     self.genre = genre

    
    