# jamarrange.io
![Latest stable version](https://img.shields.io/badge/stable%20version-0.2.4-blue.svg)

The only media player that knows your music the way you know it.

# Contents

- [Layout design](mediaplayer/layout1.py)
- [Functionality tests](mediaplayer/source_code.py)
- [File arrangement](filerepo/musicrepo.py)
- [Filesorting](documentation/filesorting.md)
- [Getting to know you](documentation/userlearning.md)
- [Tutorials](tutorials/readme.md)

---
## Getting started
jamarrange is built on python 2. More specifically 2.7.12. It should work fairly well for python 2.7.10 and 2.7.11 as well.

##### WXpython
jamarrange utilises WXpython for it's GUI capabilities and functionalities. To develop using WXpython modules, simply download and setup WXpython for mac as instructed for your machine and the specific python version you are running on the [following link](https://www.wxpython.org/download.php).

##### Tinytag
jamarrange relies on the Tinytag plugin to handle media file metadata. The installation details for setting up and installing TinyTag on python 2 can be found on the [following link](https://pypi.python.org/pypi/tinytag/).

Tiny tag is a library that allows you to access file meta data (mainly audio files within jamarrange). It supports:
- MP3
- OGG
- OPUS
- MP4
- M4A
- FLAC
- WMA
- Wave files

To begin (once installed). Simply import your library and use the TinyTag.get() function to get all the metadata contained within a desired file. Use the file local directory as a string input as illustrated below.

    from tinytag import TinyTag
    tag = TinyTag.get('/some/music.mp3')
    print('This track is by %s.' % tag.artist)
    print('It is %f seconds long.' % tag.duration)

Listed below is a list of possible attributes you can get with TinyTag:

    tag.album         # album as string
    tag.albumartist   # album artist as string
    tag.artist        # artist name as string
    tag.audio_offset  # number of bytes before audio data begins
    tag.bitrate       # bitrate in kBits/s
    tag.disc          # disc number
    tag.disc_total    # the total number of discs
    tag.duration      # duration of the song in seconds
    tag.filesize      # file size in bytes
    tag.genre         # genre as string
    tag.samplerate    # samples per second
    tag.title         # title of the song
    tag.track         # track number as string
    tag.track_total   # total number of tracks as string
    tag.year          # year or data as string

To access file cover images from ID3 tags you can follow the example below:

    tag = TinyTag.get('/some/music.mp3', image=True)
    image_data = tag.get_image()


## File arrangement
Identify your music files and arrange them accordingly in a desired local storage folder. Using audio fingerprinting technology, the application accurately identifies artists, albums, and songs to accurately arrange your files.

## Contribution
Want to contribute? Simply clone the latest master repository (and version) and create a branch under your name.

---
# About
![Numstack™ logo](assets/numstack_logo.png)

This project is continuously created and updated by the Numstack™ team.
The Numstack team creates applications for people (and the world they live in). They're a group of "academics", that constantly research the impacts of their work on the lives of those around them.

Visit the Numstack website to learn more about the [Numstack team](http://www.numstack.co.za/) and how they are changing your world.
