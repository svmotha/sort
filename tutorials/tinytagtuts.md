# Jam arrange | tiny tag tutorials
Tiny tag is a library that allows you to access file meta data (mainly audio files for jam arrange application). It supports:
- MP3
- OGG
- OPUS
- MP4
- M4A
- FLAC
- WMA
- Wave files

These are all through python. It supports python 2 and 3, to learn more and for installation visit the tinytag package index by [clicking here](https://pypi.python.org/pypi/tinytag/).  

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
