# Test Case #02.001: A single line note ("//"-type comment)

## Description

This use case addresses //-type comment

## SysML v2 textual notation

```sysml
{% include "test_02.001.sysml" %}
```

## Expected output

```
{% include "test_02.001.output" %}
```

## Comments

A comment embedded within the SysML v2 textual notation is used to
annotate the textual notation. There are multiple types of comments
in SysML v2, and this test case addresses only a single-line note.

## Rules/constraints

According to the KerML specification: "A single-line note includes
all the text from the initial characters '//' up to the next line
terminator or the end of the input text (whichever comes first)."
