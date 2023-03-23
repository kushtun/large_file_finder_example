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
     
     
