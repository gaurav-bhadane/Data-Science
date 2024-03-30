import os
import sys
from os.path import abspath, dirname, join

sys.path.insert(0,abspath(join(dirname(__file__), '..')))

from course import course_details


def payment():
    print("This is my Payment File")
    
course_details.course()
