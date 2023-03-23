# large-files.py
Example CLI tool for finding large files from a starting path.

## To run:

```python large-files.py -h
usage: large-files.py [-h] [--size_limit [SIZE_LIMIT]] [--file_suffix [FILE_SUFFIX]] path

positional arguments:
  path                  Filepath to use. e.g. /home/me/

optional arguments:
  -h, --help            show this help message and exit
  --size_limit [SIZE_LIMIT], -s [SIZE_LIMIT]
                        Minimum file size limit to apply in MB. e.g. 50. Default: 20
  --file_suffix [FILE_SUFFIX]
                        Optional: specify file type. e.g. '.mp3'
```
     
This tool will walk down the provided path, returning a list of files that meet criteria of size (default >= 20 MB), and optionally filtered by final extension.
So, for example, to find all files larger than 100 MB of type ".zip" in your Downloads directory, you could run:


`python ./large-files.py /home/MyAccount/Downloads -s 100 --file_suffix ".zip"`
