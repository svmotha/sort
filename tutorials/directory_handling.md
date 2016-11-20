# Jam arrange | Directory handling


### Folder naming limitations
The current build deals with strings using the python **str** built in function.

Any artist name with any of the special characters listed below should be replaced with a space in order for the folder name to be valid i.e. the directory path can be valid and created.

This is dealt with in the application by the implementation of the replace **replace_special_chars** and **replace_special_chars_files** functions within the Arranger class.

The special characters that these functions handle are listed below.

    < (less than)
    > (greater than)
    : (colon)
    " (double quote)
    / (forward slash)
    \ (backslash)
    | (vertical bar or pipe)
    ? (question mark)
    * (asterisk)
