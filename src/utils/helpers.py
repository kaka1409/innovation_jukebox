"""
This file contain helper functions that will be use across the whole project
"""

import math

from PyQt5.QtWidgets import QApplication

def get_formated_time(time):
    """
    return the correct time format
    """
    minutes = int(math.floor(time / 60))
    seconds = int(math.floor(time)) - minutes * 60
    if seconds in range(0, 10): seconds = "0" + str(seconds)

    return f'{minutes}:{seconds}'

def generate_id(item_list):
    """
    return a new id for the song
    """

    # ok here me out I asure that the last item will has the same value as the length of the list
    # note that index start as 1
    last_index = len(item_list)
        
    # so to get the next id we only need to add 1
    return last_index + 1

def sort_by_id(unsorted_files):
    """
    sort the song list by id
    """
    return sorted(unsorted_files, key = lambda x: int(x.split(';')[0]))

def center_widget(widget, parent_widget):
    """
    center the widget on the screen
    """
    x = (parent_widget.width() - widget.width()) // 2
    y = (parent_widget.height() - widget.height()) // 2
    widget.move(x, y)

def get_text_width(widget):
    """
    return the width of the text in the widget
    """
    return widget.fontMetrics().boundingRect(widget.text()).width()

