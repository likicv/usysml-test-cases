# Test Case #01.005: `Part` with no type specified

## Description

A `Part` element with no type may be specified.

## SysML v2 textual notation

```sysml
{% include "test_01.005.sysml" %}
```

## Expected output

```
{% include "test_01.005.output" %}
```

## Comments

A `Part` element may have no type, as shown above for the elements
`partnotype1` and `partnotype2`.


## Rules/constraints

None.

## Discussion

If a `Part` element is not specified, this opens the question,
how to handle this situation in the implementation.

