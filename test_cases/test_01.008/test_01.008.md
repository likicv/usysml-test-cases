# Test Case #01.008: `Part` with no type specified

## Description

A `Part` element with no type may be specified.

## SysML v2 textual notation

```sysml
{% include "test_01.008.sysml" %}
```

## Expected output

```
{% include "test_01.008.output" %}
```

## Comments

A `Part` element may have no type, as shown above for the elements
`partnotype1` and `partnotype2`. This opens the question, what is
the type of such element after parsing?


## Rules/constraints

None.
