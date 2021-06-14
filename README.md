# py-iostream
A simpler Python iostream

## How to use it
I is similar to C++ iostream

`pin` stands for `sys.stdin`, `pout` stands for `sys.stdout`, perr stands for `sys.stderr`

Below is example code of `pin`, `pout`

Both `pout` and `perr` are `ostream` so the way to use them are same

```python
var = pin.readline()
var = pin.readchar()
var = pin.read()
var = pin.readlist()
var = pin.readtuple()
```

```python
pout.write(args)
pout.writelist(args)
pout.writetuple(args)
pout.print(args)         
pout.printlist(args)     
pout.printtuple(args)    
```

Of course, you can create your own `istream` or `ostream` object

## About `istream`
A input stream in this module

### Private variables and functions
`__buffer`: store left string after process

`__ifile`: store the input file

`__clear_special_char(string)`: return a string with out character '\n' and '\r'

`__buffer_strip_front()`: strip `__buffer` front

`__read_buffer()`: read string from `__ifile` to `__buffer`

### Public variables and functions
`__init__(ifile)`: assign input file of this `istream` object. argument `ifile` needs to be a `file` object. no default argument

`readline()`: read a whole line and return

`readchar()`: read a single character and return

`read(to_type)`: read a varaible until character ' ' and use `to_type` to convert it to the type you want then return

`readlist(to_type)`: read a list from whole line and use `to_type` to convert every element in the list than return

`readtuple(to_type)`: read a tuple from whole line and use `to_type` to convert every element in the tuple than return

## About `ostream`
A output stream in this module

### Private variables and functions
`__ofile`: store the output file

### Public varaibles and functions
`__init__(ofile)`: assign output file of this `ostream` object. argument `ofile` needs to be a `file` object no default argument

`write(*args)`: output all the arguments

`writelist(*args)`: output all the list without quote

`writetuple(*args)`: output all the tuple without quote

`print(*args)`: output all the arguments and add space between every argument than output character '\n'

`printlist(*args)`: output all the lists without quote and add space between every list than output character '\n'

`printtuple(*args)`: output all the tuples without quote and add space between every tuple than output character '\n'

## Declaring `istream` and `ostream` object
### Declaration of default variables
```python
pin = istream(sys.stdin)
pout = ostream(sys.stdout)
perr = ostream(sys.stderr)
```

### Method to declare
```python
Is = istream(open('input_file.txt', 'r'))
Os = ostream(open('output_file.txt', 'w'))
Os = ostream(open('output_file.txt', 'a'))
```