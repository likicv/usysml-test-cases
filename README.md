# usysml-test-cases

uSysML ('micro SysML') Test Cases for SysML v2

CC BY-SA 4.0   This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International license: https://creativecommons.org/licenses/by-sa/4.0/


# File/folders Layout

- Test cases are written in test_cases/testxxxx folder. 
- The main file is in markdown format (extension `.md`). SysMLv2 model in
  textual notation for the test case is in `.sysml` file (should be named
  `testxxxx.sysml`).
- Expected output for the given model is in `testxxxx.output` file.
- This files may be included in the main `.md` file using the following syntax.
```
!include testxxxx.sysml
```

# Installation

To run document generator you need [pandoc](https://pandoc.org/MANUAL.html)
installed for your operating system.

Also, we are using [panflute pandoc-include
filter](https://github.com/DCsunset/pandoc-include) for file inclusion.

Install pandoc using your OS package manager and then run:

``` sh
./setup.sh
```

This will create a Python environment and install Python dependencies. To
activate the environment run:

``` sh
source venv/bin/activate
```

# Generate documentation

From the project root:

```
./gendocs.sh
```

This will process all `.md` files and create a PDF `test_cases.pdf`

