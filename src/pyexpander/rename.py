#!/usr/bin/env python

# rename and move a list of files to their appropriate directory

import re, os
import errno
import shutil
import subprocess
from pyexpander import config
from pyexpander import categorize
from pyexpander.log import get_logger
from pyexpander import postprocess
logger = get_logger('rename')

def gen_files(path, glob):
    pattern = re.compile(glob)
    for root, dirs, files in os.walk(path):
        for f in files:
            if pattern.search(f):
                fullpath = os.path.join(root,f)
                filename, filextention = os.path.splitext(fullpath)
                yield fullpath



if __name__== "__main__":

    stats = {}
    mem_used = {}
    for origpath in gen_files("/mnt/usb/Downloads/complete/Orphan.Black.S01.720p.HDTV.x264-FF/_extracted/unpacked_1/", "mkv"):
        destpath = categorize.get_categorized_path(origpath)

        postprocess._create_extraction_path(os.path.dirname(destpath))
        try:
            # Move\Copy all relevant files to their location (keep original files for uploading)
            print "move %s to %s" %(origpath, destpath)
            shutil.move(origpath, destpath)

            logger.info('%s %s to %s' % ("shutil.move", origpath, destpath))
            subprocess.check_output(['chmod', config.EXTRACTION_FILES_MASK, '-R', os.path.dirname(destpath)])
        except OSError as e:
            logger.exception("Failed to %s %s : %s" % ("shutil.move", origpath, e))
        except IOError as e:
            logger.exception("Failed to %s %s : %s" % ("shutil.move", origpath, e))

        try:
            os.rmdir(os.path.dirname(origpath))
        except OSError as ex:
            if ex.errno == errno.ENOTEMPTY:
                print "%s not empty yet.." %origpath
        except IOError as ex:
                logger.exception("Failed to remove %s: %s" % (origpath, e))
