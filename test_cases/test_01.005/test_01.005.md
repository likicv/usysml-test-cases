# Test Case #01.005: A `Part` element with no type specified

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

A `Part` element may have no type specified, as shown above for the
elements `partnotype1` and `partnotype2`.


## Rules/constraints

None.

## Discussion

The possibility that a `Part` element has no type specified opens
the question how to handle this situation in the implementation.

