# usysml-test-cases

uSysML ('micro SysML') Test Cases for SysML v2

© Vladimir Likić <vlad.likic@gmail.com>

© Igor Dejanović <igor.dejanovic@gmail.com>

CC BY-SA 4.0   This work is licensed under the Creative Commons
Attribution-ShareAlike 4.0 International license:
https://creativecommons.org/licenses/by-sa/4.0/


# Background

The objective of the OMG Systems Modeling Language v2 (SysML v2)
is to enable more effective model-based systems engineering (MBSE).
The uSysML (‘micro SysML’) project aims to develop test cases
relevant for the implementation of the SysML v2 specification.
The objective of this work is two-fold: (1) to provide documented
test cases that would assist the MBSE community in the implementation
of the SysML v2 specification; and (2) to generate input that
would be helpful for clarifying or strengthening of the SysML
v2 specification.

To view the test cases please click [here](/test_cases.md), and to
download the summary PDF file please click [here](/test_cases.pdf).


## uSysML

The uSysML project is an approach to the development of test cases
for the SysML v2 textual notation. In the narrow sense, uSysML
refers to a subset of SysML v2 keywords and behaviors, however
what exactly is included in this subset depends on the uSysML
version (see the table below). The purpose of uSysML versioning is
to define a scope that will limit considerations required for
the development of test cases. The currently planned uSysML
versions and their scope are shown in the table below:


| uSysML version | Scope | Status |
| --- | --- | --- |
| v0.01 (spiral 1) | `package`, `part`, `part def` | 8 test cases |
| v0.02 (spiral 2) | +`attribute`, +`attribute def`, //-type comments | 1 test case |
| v0.03 (spiral 3) | +`redefines`, +`subsets`, +`specializes` | None yet |


The key idea behind uSysML is that SysML v2 behaviors are decomposable
in the sense that it would possible to create valid SysML v2 models
with only a subset of the features defined by the full SysML v2
specification (in fact, with just a small subset of the SysML v2
features, for example the keywords `package`, `part`, `part def`,
it would possible to create quite complex models that are fully
compliant with the SysML v2 specification).

The scope of uSysML for each version (or spiral) is fixed for
the purpose of exploring practical issues relevant to the SysML
v2 implementation. While the uSysML project is independent of
any specific implementation, it is sometimes useful to think of
uSysML as being a limited implementation of the SysML v2
specification. Consider the following: an implementation
corresponding to uSysML v0.01 would support only the SysML v2
behaviors associated with the keywords `package`, `part`,
`part def` and nothing else (see the table above). Furthermore,
every model specified by uSysML would be a valid SysML v2 model,
and paresable by the full SysML v2 implementation. The reverse
is not true: because uSysML implementation is limited and the
full SysML v2 specification includes many features outside of
the scope of uSysML, general SysML v2 models would not be
necessarily parseable by an uSysML implementation.

The following references are used in this work:
- Kernel Modeling Language (KerML) (‘1-Kernel_Modeling_Language.pdf’)
- OMG Systems Modeling Language (SysML) (‘2-OMG_Systems_Modeling_Language.pdf’)
- [SysMLv2 Pilot Implementation Prototype](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation)
- Sanford Friedental, “Introduction to the SysML v2 Language Graphical
Notation”, Release: 2021-05-21
- Model Driven Solutions, Inc. “Introduction to the SysML v2 Language
Textual Notation”, Release: 2021-05

This document is a “living document” that is being developed and
maintained by the uSysML team. Henceforth the test cases derived
from this work will be referred to as “uSysML Test Cases”. 


# Understanding uSysML Test Cases

The test cases are organised under the folder `test_cases`, one test
case per folder named 'test_XY-ABC' (where 'XY-ABC' is the test case
unique identifier). Within each test case there are several files,
of which the following are particularly important:

- \*.sysml -- contains the test case SysML v2 textual notation
- \*.output -- contains the test case output (in the uSysML output
notation explained below)
- \*.ipynb -- Jupyter notebook with test case parsed by the SysML
v2 Pilot Implementation

The title of the test case contains a short description of the test
case, and a unique identifier (Test Case ID) which allows it to be
referenced subsequently. The Test Case ID is of the form 'XY-ABC'
where 'XY' refers to the spiral, and 'ABC' is the unique test case
number within a spiral. The spiral shows the scope that the test
case refers to; for example, for a test case that is marked 'spiral 1'
('XY' = 01), only `package`, `part`, and `part def` would have been
expected to be implemented.

Each test case is structured according to the following sections:

- Title -- a short title of the test case together with the number
identifier
- Description -- a description of the test case
- SysML v2 textual notation -- shows SysML v2 textual notation
- Expected output -- shows the expected output of after the parsing of the
SysML v2 textual notation. **Note: what is listed as "output" is not a
SysML v2 notation, but a special notation developed for uSysML Test Cases**.
See the explanations below
- Comments -- any additional comments
- Rules/constraints -- any rules or constraints that we can derive from the
test case considerations
- Discussion -- This section is optional, and give a discussion of the
test case if needed
 

## The notation used in the “Expected output” section

The Test Case "Expected output" section is not SysML v2 notation, rather
this uses a special notation development only for this purpose. The
purpose of the notation is to specify namespaces and possibly additional
features of the parsed elements. The examples are given below with the
explanations.


### Example 1

    Root.PackageVehicles.Vehicle

**Meaning**:

'Vehicle' is in the namespace of 'PackageVehicles', and 'PackageVehicles'
is in the namespace of 'Root'.


### Example 2

    Root.PackageVehicles.Vehicle [PartDef]

**Meaning**:

‘Vehicle' is in the namespace of 'PackageVehicles' which is in the namespace
of 'Root'. 'Vehicle' is `PartDef` i.e. the SysML v2 Cassifier is `PartDef`,
(meaning that the element 'Vehicle' was generated by the SysMLv2 ‘part def’
command).


### Example 3

    Root.PackageVehicles.vehicle [Part]
        type=Root.PackageVehicles.Vehicle

**Meaning**:

- ‘vehicle’ is in the namespace of ‘PackageVehicles’ which is in the namspace
of ‘Root’
- ‘vehicle’ is `Part` of the type ‘Root.PackageVehicles.Vehicle’


### Example 4

Consider a more complex example:

```
Root.PackageVehicles [Package]
 Root.PackageVehicles.Vehicle [PartDef]
 Root.PackageVehicles.Wheel [PartDef]
 Root.PackageVehicles.vehicle [Part]
    type=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [Part]
      type=Root.PackageVehicles.Wheel
Root.PackageStations [Package]
 Root.PackageStations.VehicleStation [PartDef]
```

Here the indendation indicates the namespace level. The indentation level can
be read from the actual output, however the indendation helps guide the eye.
Specifically:

```
Root.PackageVehicles [Package]
```

and 

```
Root.PackageStations [Package]
```

are at the same namespace level, just under the 'Root'. Furthermore, the
element:


```
Root.PackageVehicles.vehicle.w [Part]
```

Is the only element that is in the namespace that is three levels deep.


# Local installation of uSysML test cases

## Project file/folders Layout

- Test cases are written in test_cases/testxxxx folder. 
- The main file is in markdown format (extension `.md`). SysMLv2 model in
  textual notation for the test case is in `.sysml` file (should be named
  `testxxxx.sysml`).
- Expected output for the given model is in `testxxxx.output` file.
- These files (or any other file) may be included in the main `.md` file
using the following syntax.
```
{% include "testxxxx.sysml" %}
```

## Installation steps

To run PDF document generator you need [pandoc](https://pandoc.org/MANUAL.html)
installed for your operating system.

Also, we are using [Jinja2](https://jinja2docs.readthedocs.io/en/stable/) for
file inclusion.

Install pandoc using your OS package manager and then run:

``` sh
./setup.sh
```

This will create a Python environment and install Python dependencies. To
activate the environment run:

``` sh
source venv/bin/activate
```

## Generating documentation locally

Download the project from GitHub with `git clone`:

```
$ git clone https://github.com/likicv/usysml-test-cases
```

From the project root:

```
$ ./gendocs.py
```

or 

``` sh
$ python gendocs.py
```

This will process all the individual test cases and create a cumulative
test case document `test_cases.md`, as well as the corresponding PDF file.
Note that the PDF file creation requires `pandoc` to be installed on your 
system.
