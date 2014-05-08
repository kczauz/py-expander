import os
import sys


TV_PATH = '/mnt/usb/Media/TV Shows/{series}/Season {season}/{series} - {season}x{episode}{extension}'
MOVIE_PATH = '/mnt/usb/Media/Movies/{title} ({year})/{title} ({year}){extension}'
APP_PATH = '/mnt/usb/Apps/'
MUSIC_PATH = '/mnt/usb/Media/Music'
UNKNOWN_PATH = '/mnt/usb/Downloads/extracted/'

EXTRACTION_FILES_MASK = '770'


LOGFILE = '/var/log/pyexp.log'


EXTRACTION_TEMP_DIR_NAME = '_extracted'


def _find_executable(filename):
    """
    Searches for a file in paths exported to the PATH environmental variable
    :param filename:
    """
    # Search the system path for the executable
    if sys.platform == 'win32':
        filename += '.exe'
    for directory in os.getenv('PATH').split(os.pathsep):
        # Ensure the directory in the path is a real directory
        if os.path.exists(directory):
            files = os.listdir(directory)
            if filename in files:
                # print 'Found ' + filename +' in ' + directory
                return os.path.join(directory, filename)
        else:
            # The directory in the path does not exist
            pass
    raise Exception(filename + ' not found or is not in system PATH')


EXECUTABLE = _find_executable('unrar')  # apt-get install unrar

