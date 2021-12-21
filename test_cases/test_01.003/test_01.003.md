# Test Case #01.003: Element Classifiers

## Description

Every element is associated with a Classifier SysMLv2 textual notation.

## SysML v2 textual notation

```sysml
{% include "test_01.003.sysml" %}
```

## Expected output

```
{% include "test_01.003.output" %}
```

## Comments
1. In output above the element Cassifiers are shown in square brackets
(`Package`, `PartDef`, and `Part`)
2. The following development in notation is adoped: instead of saying
the element `Root.PackageVehicles` is associated with a Classifer
`Package`, it can be said the element `Root.PackageVehicles` is `Package`.

## Rules/constraints

Every processed element is associated with a Classifier.
