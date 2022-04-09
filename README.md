# usysml-test-cases

uSysML ('micro SysML') Test Cases for SysML v2

© Vladimir Likić <vlad.likic@gmail.com>

© Igor Dejanović <igor.dejanovic@gmail.com>

CC BY-SA 4.0   This work is licensed under the Creative Commons
Attribution-ShareAlike 4.0 International license:
https://creativecommons.org/licenses/by-sa/4.0/


# Links

To view the test cases please click [here](/test_cases.md), and to
download the summary PDF file please click [here](/test_cases.pdf).


# Background

The objective of the OMG Systems Modeling Language v2 (SysML v2)
is to enable more effective model-based systems engineering (MBSE).
The uSysML (‘micro SysML’) project aims to develop test cases
relevant for learning and implementation of the SysML v2 specification.
The objective of the uSysML project is two-fold: (1) to provide
documented test cases that would be useful to the MBSE community
in implementations of the SysML v2 specification; and (2) to
generate examples that cold be helpful for clarifying or
strengthening of the SysML v2 specification.


**NOTE: the uSysML project isn't a SysML v2 implementation, rather
it is a collection of test cases that are intended to be useful
for creating a SysML v2 implementation.**


## uSysML

The uSysML project is an approach to the development of test cases
for the SysML v2 textual notation. It refers to two things: in
the narrow sense, 'uSysML' refers to a subset of SysML v2 keywords
and behaviors; in the broader sense, 'uSysML' refers to the
collection of test cases developed under this GitHub project.
The purpose of uSysML versioning is to define a scope that will
limit considerations required for the development of test cases.
The currently planned uSysML versions and their scope are shown
in the table below:


| uSysML version | Scope | Status |
| --- | --- | --- |
| v0.01 (spiral 1) | `package`, `part`, `part def` | 5 test cases |
| v0.02 (spiral 2) | +//-type comments, +unrestricted element names | 2 test cases |
| v0.03 (spiral 3) | +`attribute def`, +`attribute` | 1 test case |
| v0.04 (spiral 4) | +`redefines`, +`subsets` | None yet |
| v0.1  | defined by all versions <0.1 | N/A |


The key idea behind uSysML is that SysML v2 behaviors corresponding
to different spirals are fully decomposable, and uSysML focuses only
on a small subset of the full SysML v2 language. This idea could be
explained by using a simple calculator language. Let's assume a
calculator language that implements only addition and multiplication
of two positive integers. Complex computing environments, for example
[R](https://www.r-project.org/) and
[GNU Octave](https://www.gnu.org/software/octave/index), implement
a superset of such calculator language. In other words, the
following concrete calculator syntax would work in both
[R](https://www.r-project.org/)
and [GNU Octave](https://www.gnu.org/software/octave/index):


```
> 2 + 2
4
> 1 * 2
2
```

Every such simple calculator command could run in
[R](https://www.r-project.org/) or
[GNU Octave](https://www.gnu.org/software/octave/index) with a
predictable outcome. However the other way around doesn't
hold: [R](https://www.r-project.org/) and
[GNU Octave](https://www.gnu.org/software/octave/index)
implement many additional features, and can handle much more
complex command input. It could be said that the 'simple
calculator language' is a small subset of the
[R](https://www.r-project.org/) and
[GNU Octave](https://www.gnu.org/software/octave/index)
languages. uSysML relates to the full SysML v2 language feature
set in a similar way.

It would possible to create valid SysML v2 models with the
subset of the SysML v2 features defined by the uSysML spiral 1
(only the keywords `package`, `part`, and `part def`). And
furthermore, by using such subset it would possible to create
quite complex SysML v2 models.

The scope of uSysML for each version (or spiral) is fixed for
the purpose of exploring practical issues relevant to the SysML
v2 implementation. While the uSysML project is independent of
any specific implementation, it is sometimes useful to think of
uSysML as being a limited implementation of the SysML v2
specification. Consider an implementation corresponding to
uSysML v0.01 that supports only the SysML v2 keywords `package`,
`part`, `part def` and nothing else (see the table above).
Every model specified by such implementation would be a valid
SysML v2 model, and paresable by the full SysML v2 implementation.
The reverse is not true: because uSysML implementations are
limited general SysML v2 models would not be necessarily
parseable by an uSysML implementation.


# References

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
- uSysML output -- shows the expected output of after the parsing of the
SysML v2 textual notation. **Note: what is listed as "output" is not a
SysML v2 notation, but a special notation developed for uSysML Test Cases**.
See the explanations below
- Comments -- any additional comments
- Rules/constraints -- any rules or constraints that we can derive from the
test case considerations
- Discussion -- This section is optional, and give a discussion of the
test case if needed
 

## The notation used in the “uSysML output” section

In each Test Case the "uSysML output" section is not SysML v2 notation,
rather this uses a special notation development only for the purpose
of uSysML. The purpose of the notation is to specify namespaces and
possibly additional features of the parsed elements. The examples are
given below with the explanations.


### Example 1

    Root.PackageVehicles.Vehicle

**Meaning**:

`Vehicle` is in the namespace of `PackageVehicles` and `PackageVehicles`
is in the namespace of `Root`.


### Example 2

    Root.PackageVehicles.Vehicle [PartDef]

**Meaning**:

`Vehicle` is in the namespace of `PackageVehicles` which is in the namespace
of `Root`. Furthermore, `Vehicle` is *PartDefinition* element (meaning that
the element `Vehicle` was generated by the SysMLv2 ‘part def’ command).


### Example 3

    Root.PackageVehicles.vehicle [Part]
        typed by=Root.PackageVehicles.Vehicle

**Meaning**:

- `vehicle` is in the namespace of `PackageVehicles` which is in the namspace
of `Root`
- `vehicle` is *PartUsage* typed by *PartDefinition* `Root.PackageVehicles.Vehicle`


### Example 4

Consider a more complex example:

```
Root.PackageVehicles [Package]
 Root.PackageVehicles.Vehicle [PartDef]
 Root.PackageVehicles.Wheel [PartDef]
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [PartUsage]
      typed by=Root.PackageVehicles.Wheel
Root.PackageStations [Package]
 Root.PackageStations.VehicleStation [PartDef]
```

The indentation indicates the namespace level. The namespace level can be
read from the actual textual output, however the indentation helps guide
the eye. Specifically:

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
Root.PackageVehicles.vehicle.w [PartUsage]
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
