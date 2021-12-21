# usysml-test-cases

uSysML ('micro SysML') Test Cases for SysML v2

© Vladimir Likić <vlad.likic@gmail.com>

© Igor Dejanović <igor.dejanovic@gmail.com>

CC BY-SA 4.0   This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International license: https://creativecommons.org/licenses/by-sa/4.0/


# Background

SysML v2 is the next generation of the OMG Systems Modeling Language (SysML)
currently under development. The objective of SysML v2 to enable more
effective model-based systems engineering (MBSE). The uSysML (‘micro
SysML’) project is an approach to the development of SysML v2 test cases
based on the decomposability of SysML v2. The objective of this work is
twofold: (1) to generate input that may require consideration,
clarification, or strengthening of the SysML v2 specification for
unambigous SysML v2 implementation; and (2) to provide documented 
test cases that would assist the MBSE community in the implementation
of the SysML v2 specification. **The uSysML project aims to generate
specific test cases, associated discussion, and any issues for
consideration.**

To view current test cases please click [here](/test_cases.md), and to
download the summary PDF file please click [here](/test_cases.pdf).


## uSysML

In the wider sense, uSysML is an approach to the development of test
cases for SysML v2. In the narrow sense uSysML refers to a subset of
SysML v2 keywords and behaviours, and what exactly is included in
this subset depends on the uSysML version (see the table below). The
purpose of uSysML versions is to define the scope that will limit
considerations required for the development of Test Cases. The
currently planned uSysML versions are shown in the table below:


| uSysML version | Scope | Status |
| --- | --- | --- |
| v0.01 (spiral 1) | `package`, `part`, `part def`, //-type comments | 8 test cases |
| v0.02 (spiral 2) | +`attribute`, +`attribute def` | None yet |
| v0.03 (spiral 3) | +`redefines`, +`subsets`, +`specializes` | None yet |


The idea behind uSysML is that SysML v2 behavrious are perfectly
decomposable, in the sense that it is possible to create a valid
SysML v2 models with just a subset of features defined by the SysML
v2 specification. While the objective of this project is to generate
test cases and associated discussion that will be useful in any
SysML v2 implementation, it is sometimes useful to think of uSysML
as a specific implementation of the SysML v2 specification. Then
the implementation corresponding to uSysML v0.01 (spiral 1) would
support the behaviours of the keywords `package`, `part`, `part def`
only. We note that with just those three keywords it is possible
to create quite complex, fully compliant SysML v2 models. In other
words, every uSysML model should be a valid SysML v2 model, paresable
by any complete SysML v2 implementation; however the reverse does
not hold, because the full SysML v2 specification includes many
features beyond the scope of uSysML. The scope of uSysML for each
version (or spiral) is fixed for the purpose of test cases and
exploring the practical issues relevant to the implementation of
the SysML v2 textual notation.


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
from this work will be referd to as “uSysML Test Cases”. 


# Understanding uSysML Test Cases

Each uSysML Test Case is associated with a unique number identifier (Test
Case ID) that allows it to be referenced subsequently. The Test Case ID
is given in the test case title, as well as a short description of the
test case and the spiral. The spiral refers to the uSysML version as per
the above table, and this shows the scope that the test case refers to;
for example, for a test case that is marked 'spiral 1', only `package`,
`part`, and `part def` would have been expected to be implemented.

Each test case is structured into the following sections:
- Title -- a short title of the Test Case together with the number identifier
- Description -- a description of the test case
- SysML v2 textual notation -- shows SysML v2 textual notation
- Expected output -- shows the expected output of after the parsing of the
SysML v2 textual notation. **Note: this is not a SysML v2 notation, but a
special notation developed for uSysML Test Cases**. See the explanations
below
- Rules/constraints -- any rules or constraints that we can derive from the
test case considerations
- Comments -- any additional comments
- Discussion -- discussion of the test case, possibly including some negative
examples to highlight the points made, expected output, rules or constraints
 

## The notation used in the “Expected output” section

The Test Case "Expected output" section is not SysML v2 notation, rather
this is a special notation developed for the purpose of uSysML Test Cases.
More specifically, this is a shorthand notation to specify namespaces
and possibly additional features of the parsed elements. Some examples
are given below.


### Example 1

    Root.PackageVehicles.Vehicle

**Meaning**:

'Vehicle' is in the namespace of 'PackageVehicles', and 'PackageVehicles'
is in the namespace of 'Root'.


### Example 2

    Root.PackageVehicles.Vehicle [PartDef]

**Meaning**:

‘Vehicle' is in the namespace of 'PackageVehicles' which is in the namespace
of 'Root'. 'Vehicle' is `PartDef` (i.e. the SysML v2 Cassifier is `PartDef`,
meaning that 'Vehicle' was generated by the SysMLv2 ‘part def’ command).


### Example 3

    Root.PackageVehicles.vehicle [Part]
        type=Root.PackageVehicles.Vehicle

**Meaning**:

- ‘vehicle’ is in the namespace of ‘PackageVehicles’ which is in the namspace
of ‘Root’
- ‘vehicle’ is `Part` of the type ‘Root.PackageVehicles.Vehicle’


# Local installation of test cases

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

This will process all the inidividual test cases and create a cumulative
test case codument `test_cases.md`, as well as the corresponding PDF file
(PDF file creation requires `pandoc` to be installed on the system).
