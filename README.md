# puny.py-script
Python script for IDNA encode/decode

### Usage examples:

```
./puny.py exāmple.com exāmple2.com
xn--exmple-4za.com
xn--exmple2-t3a.com
```

```
./puny.py exāmple.com exāmple2.com -o test.txt
cat test.txt                                  
xn--exmple-4za.com
xn--exmple2-t3a.com
```

```
./puny.py -ri test.txt
exāmple.com
exāmple2.com
```

```
./puny.py -h
usage: puny.py [-h] [-i [INPUT]] [-o [OUTPUT]] [-r] [-V] [-d | -q] [domain [domain ...]]

Encode to/decode from idna

positional arguments:
  domain                domain names (divided by space)

optional arguments:
  -h, --help            show this help message and exit
  -i [INPUT], --input [INPUT]
                        input file (default stdin)
  -o [OUTPUT], --output [OUTPUT]
                        output file (default stdout)
  -r, --reverse         decode from idna
  -V, --version         show program's version number and exit
  -d, --debug           debug output
  -q, --quiet           suppress warnings
```
