import os 

from random import randint

class ImageManager():
    def __init__(self, folder_path):

        self.image_directory = folder_path
        self.song_thumbnails_directory = folder_path  + "/song_thumbnails"
        self.song_thumbnails_placeholder_directory = folder_path + "/song_thumbnails/placeholder_thumbnails"

    def get_image_list(self, folder_path):

        image_path_list = []
        image_name_list = []

        # loop through the folder
        image_files = os.listdir(folder_path)

        for image_path in image_files:
            
            # get file based on extension jpg, png and webp
            if image_path.endswith("jpg") or image_path.endswith("png") or image_path.endswith("webp"):

                # add path to list
                image_path_list.append(os.path.join("assets\\images\\song_thumbnails", image_path))

                # get image name from file name
                image_name = image_path.split(".")[0].replace("_", " ")
                # add name to list
                image_name_list.append(image_name)

        return image_path_list, image_name_list
    
    def get_placeholder_thumbnail(self):

        random_index = randint(0, 2)

        image_path_list = []

        # loop through the folder
        image_files = os.listdir(self.song_thumbnails_placeholder_directory)

        for image_path in image_files:

            # get file based on extension jpg, png and webp
            if image_path.endswith("jpg") or image_path.endswith("png") or image_path.endswith("webp"):

                # add path to list
                image_path_list.append(os.path.join("assets\\images\\song_thumbnails", "placeholder_thumbnails", image_path))

        return image_path_list[random_index]

    


