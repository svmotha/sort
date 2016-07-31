from tinytag import TinyTag

reserved_chars = ['<','>',':','"','/','\\','|','?','*']

target = TinyTag.get('C:\\Users\\User\\Music\\Hip Hop\\Hip Hop Mix\\02 Luda  Undisputed.mp3')

temp = str(target.artist)
for i in range(len(reserved_chars)):
    if reserved_chars[i] in temp:
        temp = temp.replace(reserved_chars[i], ' ')
        
