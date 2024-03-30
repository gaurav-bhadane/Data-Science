import os
import sys
from os.path import abspath, dirname, join

sys.path.insert(0,abspath(join(dirname(__file__), '..')))
# for collapsing path independencies above code is written

# from payment import payment_details


def course():
    print("This is my Course File")
    
# payment_details.payment()
    
# Packages: They are basically Folders (Directories)
# Modules: The individual file is known as Module