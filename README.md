# google-drive-takeout

A simple tool to perform merging of the drive data exported out from google takeout.


DISCLAIMER:

The script will not delete zip files by default. But my use case required me to delete the zip files on the fly so I implemented it.


> Known issues:

Extracting a zip file has some complications when using on windows.

It will most likely not work on windows because on Windows, if a file's path contains spaces or special characters like `!@#$%^&*(){}:"|<>?/,.;'~` it will freak out.

It will most likely work perfectly on linux.
