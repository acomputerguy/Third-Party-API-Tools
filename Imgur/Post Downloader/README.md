# Image Downloader

Because scraping is never the answer!

![alt text](https://github.com/acomputerguy/Third-Party-API-Tools/blob/master/Imgur/Post%20Downloader/imgurpython_gui_dltab.PNG)

## Prerequisites

Requires obtaining a client id and secret key from your Imgur account

Required dependencies
-----
Python package manager (for Python >=v3.0)

    $ wget https://bootstrap.pypa.io/get-pip.py
    $ python3 get-pip.py
PyQt5 and Designer (latest version)

    $ apt-get install python3-pyqt5
    $ apt-get install pyqt5-dev-tools
    $ apt-get install qttools5-dev-tools
Python wrapper, size converter, PyYAML

    $ python3 -m pip install imgurpython, hurry.filesize, pyyaml
And run with

    $ python3 sample.py
    
Development Process
-----
Open up the GUI Designer tool with

    $ /usr/lib/x86_64-linux-gnu/qt5/bin/designer (or type in designer and replace 'qt4' with 'qt5'
To write designer changes to the file do:

    $ pyuic5 sample.ui > sample.py
Run the python code with:

    $ python3 sample.py
Source to help get started

https://www.codementor.io/deepaksingh04/design-simple-dialog-using-pyqt5-designer-tool-ajskrd09n
