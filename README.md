# reNamer: A tool for regex based file renaming.

## License

Copyright (C) Oliver 'kfsone' Smith <oliver@kfs.org>, Sep 2017
Released under the MIT license.
https://github.com/

## Usage

Choose a directory from the file system browser on the left, which will show you a list of files on the right.

Enter a regex to match in the "From" input box and hit enter, then type your substitution pattern in the "To" box and hit enter again. When the patterns are valid the text will turn blue.

Also, once you've provided valid patterns, the directory list will change to show which files would be affected and what their new names would be.

Files marked with '|' symbols will be renamed; files marked with the '*' symbol would result in a file-name conflict (and the file list will turn red).

Once you have valid from and to patterns that affect at least one file without causing any duplicate file names, the "Apply" button will become available for you to [try] and change the files.

The list will then refresh itself with the new list of files in the directory.


## TODO:

* Improve the handling of changes to the from/to, right now it entirely depends on you hitting return,
* More tool tips,
* Use a better list control so that I can color-highlight filenames that are being changed,
* Fix any bugs,


