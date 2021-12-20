<!-- Generated on 2021-12-20 13:25:44.842993 from script `gendocs.py`
     DO NOT EDIT MANUALY! -->

# Test Case #0001: Fully qualified element names (FQEN) (spiral 1)

## Description

Parsing a `*.sysml` file will generate a FQEN for each element, starting
with `Root`.

## SysML v2 textual notation

```sysml
package PackageVehicles {

    part def Vehicle;
    part def Wheel;

    part vehicle:Vehicle {
        part w:Wheel;
    }
}
```

## Expected output

```
Root.PackageVehicles [Package]
 Root.PackageVehicles.Vehicle [PartDef]
 Root.PackageVehicles.Wheel [PartDef]
 Root.PackageVehicles.vehicle [Part]
    type=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [Part]
      type=Root.PackageVehicles.Wheel
```

## Rules/constraints

1. A `*.sysml` file defines the name space for the elements it contains.
The top level name space bounded by the file is assigned to the element
`Root`.
2. Each curly braces segment defines a name space.
3. Within a `*.sysml` file each FQEN must be uniqe.

## Comments

None.

## Discussion

This Test Case focuses on the requirement for uniqueness of each
FQENs within a sysml file. The following example should generate
an error:

```sysml
package PackageVehicles {

    part def Vehicle;
    part def Wheel;
    part Wheel;

    part vehicle:Vehicle {
        part w:Wheel;
    }
}
```

because in this case both `part def Wheel` and `part Wheel` have the
same FQEN `PackageVehicles.Wheel` (even though the two elements are
associated with different classifiers, `PartDef` and `Part`,
respectively).

# Test Case #0002: Fully qualified element names (FQEN) (an extension of #0001) (spiral 1)

## Description

Parsing of the `*.sysml` file will generate a FQEN for each element, starting
with `Root` SysMLv2 textual notation.

## SysMLv2 textual notation

```sysml
package PackageVehicles {

    part def Vehicle;
    part def Wheel;

    part vehicle:Vehicle {
        part w:Wheel;
    }
}

package PackageStations {
    part def VehicleStation;
}
```

## Expected output

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

## Rules/constraints

1. A \*.sysml file defines the name space for the elements it contains.
The top level name space bounded by the file is assigned to the
element “Root”
2. Any valid element can be nested under the “Root” element (in this
example there are two Package elements)

## Discussion

A potential issue arises when multiple `*.sysml` files are processed.
Let’s assume two files, `Vehicles1.sysml` and `Vehicles2.sysml` with
the following content:

```
file Vehicles1.sysml
file Vehicles2.sysml
part def Vehicle;
part def Wheel;
part def Vehicle;
```

Let’s assume a SysMLv2 processor `sysmlv2`, then processing the first
file will result in:

```
$ sysmlv2 Vehicles1.sysml
Root.Vehicle [PartDef]
Root.Wheel [PartDef]
```

And processing the second file will result in:

```
$ sysmlv2 Vehicles2.sysml
Root.Vehicle [PartDef]
```

When the two files are processed together:

```
$ sysmlv2 Vehicles1.sysml Vehicles2.sysml
```

the FQENs for the element `Root.Vehicle` will create a name clash.

# Test Case #0003: Element Classifiers (spiral 1)

## Description

Every element is associated with a Classifier SysMLv2 textual notation.

## SysMLv2 textual notation

```sysml
package PackageVehicles {

    part def Vehicle;
    part def Wheel;

    part vehicle:Vehicle {
        part w:Wheel;
    }
}

package PackageStations {
    part def VehicleStation;
}
```

## Expected output

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

## Comments
1. In output above the element Cassifiers are shown in square brackets
(`Package`, `PartDef`, and `Part`)
2. The following development in notation is adoped: instead of saying
the element `Root.PackageVehicles` is associated with a Classifer
`Package`, it can be said the element `Root.PackageVehicles` is `Package`.

## Rules/constraints

Every processed element is associated with a Classifier.

# Test Case #0004: ‘Part’ element type (spiral 1)

## Description

A `Part` element may have type.

## SysMLv2 textual notation

```sysml
package PackageVehicles {

    part def Vehicle;
    part def Wheel;

    part vehicle:Vehicle {
        part c;
        part w:Wheel;
    }
}
```

## Expected output

```
Root.PackageVehicles [Package]
 Root.PackageVehicles.Vehicle [PartDef]
 Root.PackageVehicles.Wheel [PartDef]
 Root.PackageVehicles.vehicle [Part]
    type=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.c [Part]
      type=None
  Root.PackageVehicles.vehicle.w [Part]
      type=Root.PackageVehicles.Wheel
```

## Comments

In the expected outpout types of `Part` elements are shown explicitely
with `type= ...`. In the above example `Part c` doesn’t have a type
specified, while `Part w` is of type `Wheel`, which itself is `PartDef`.

## Rules/constraints

1. `Part` elements may optionally have type specified
2. If `Part` element has type specified, the type must be an existing
`PartDef` element

# Test Case #0005: `Part` element syntactical forms (spiral 1)

## Description

Syntactically, `Part` element may appear in several different forms.

## SysMLv2 textual notation

```sysml
package PackageVehicles {

    part def Vehicle;
    part def Wheel;
    part def WheelAxle;

    part test_vehicle:Vehicle;

    part vehicle:Vehicle {
        part a:WheelAxle[2];
        part w:Wheel[4] {
            part def LugBolt;
        }
    }
}

package SupportComponents {

    part parking_space;
    part vehicle_shed[4];

    part repair_shop[2] {
        part def VehicleLift;
    }
}
```
## Expected output

```
Root.PackageVehicles [Package]
 Root.PackageVehicles.Vehicle [PartDef]
 Root.PackageVehicles.Wheel [PartDef]
 Root.PackageVehicles.WheelAxle [PartDef]
 Root.PackageVehicles.test_vehicle [Part]
    type=Root.PackageVehicles.Vehicle
 Root.PackageVehicles.vehicle [Part]
    type=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.a [Part]
      multiplicity=2
      type=Root.PackageVehicles.WheelAxle
  Root.PackageVehicles.vehicle.w [Part]
      multiplicity=4
      type=Root.PackageVehicles.Wheel
   Root.PackageVehicles.vehicle.w.LugBolt [PartDef]
Root.SupportComponents [Package]
 Root.SupportComponents.parking_space [Part]
    type=None
 Root.SupportComponents.vehicle_shed [Part]
    multiplicity=4
    type=None
 Root.SupportComponents.repair_shop [Part]
    multiplicity=2
    type=None
  Root.SupportComponents.repair_shop.VehicleLift [PartDef]
```

## Comments

Several syntactical forms of Part element are illustrated in the above
example:

1. `part parking_space;` — Part without multiplicity, without body,
and without type specified.
2. `part vehicle_shed[4];` — Part with multiplicity, without body,
and without type specified.
3. `part repair_shop[2] { ... }` — Part with multiplicity, with body,
and without type specified.
4. `part test_vehicle:Vehicle;` — Part without multiplicity, without
body, and type specified.
5. `part vehicle:Vehicle { ... }` — Part without multiplicity, with
body, and with type specified.
6. `part a:WheelAxle[2];` — Part with multiplicity, without body,
and with type specified.
7. `part w:Wheel[4] { ... }` — Part with multiplicity, with body,
and with type specified.

When a `Part` element has a specified type, the type must be a defined
`PartDef` element as per Test Case #0004.

## Rules/constraints

An implementation of `part` and `part def` SysMLv2 keywords must support
all seven syntactical forms shown in this Test Case.

# Test Case #0006: Namespace search rules (spiral 1)

## Description

Illustrates the namespace search rules.

## SysMLv2 textual notation

```sysml
package PackageVehicles {

    part def Vehicle;
    part def Wheel;

    part vehicle:Vehicle {
        part def Wheel;
        part w:Wheel[4];
    }
}
```

## Expected output

```
Root.PackageVehicles [Package]
 Root.PackageVehicles.Vehicle [PartDef]
 Root.PackageVehicles.Wheel [PartDef]
 Root.PackageVehicles.vehicle [Part]
    type=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.Wheel [PartDef]
  Root.PackageVehicles.vehicle.w [Part]
      multiplicity=4
      type=Root.PackageVehicles.vehicle.Wheel
```

## Comments

In this example `part def Wheel` exists both withing the `PackageVehicles`
and `part vehicle` namespaces (and furthermore, `part vehicle` namespace
is nested within the `PackageVehicles` namespace). In this case, Part
`w` id typed by PartDef that is within the inner (`part vehicle`)
namespace.

## Rules/constraints

The namespace search starts from its own namespace, then proceeds into
the parent namespaces in the order until the Root namespace is reached.

# Test Case #0007: Namespace search rules (spiral 1)

## Description

Illustrates the namespace search rules.

## SysMLv2 textual notation

```sysml
package PackageVehicles {
  
    part def Vehicle;
    part def Wheel;

    part vehicle:Vehicle {
        part w:Wheel[4];
    }
}
```

## Expected output

```
Root.PackageVehicles [Package]
 Root.PackageVehicles.Vehicle [PartDef]
 Root.PackageVehicles.Wheel [PartDef]
 Root.PackageVehicles.vehicle [Part]
    type=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [Part]
      multiplicity=4
      type=Root.PackageVehicles.Wheel
```

## Comments

This example illustrates execution of the namespace search in the parent
namespace. In this example `part def Wheel` doesn't exists within the `part
vehicle` namespace, and the parent namespace (that of `PackageVehicles`)
is being searched to find PartDef `Wheel`.

## Rules/constraints

The namespace search starts from its own namespace, then proceeds into
the parent namespaces in the order until the Root namespace is reached.
Compare to Test Case #0006.


# Test Case #0008: `Part` with no type specified (spiral 1)

## Description

A `Part` element with no type may be specified.

## SysMLv2 textual notation

```sysml
package PackageVehicles {

    part def Vehicle;
    part def Wheel;
    part partnotype1;

    part vehicle:Vehicle {
        part w:Wheel[4];
        part partnotype2;
    }
}
```

## Expected output

```
Root.PackageVehicles [Package]
 Root.PackageVehicles.Vehicle [PartDef]
 Root.PackageVehicles.Wheel [PartDef]
 Root.PackageVehicles.partnotype1 [Part]
    type=None
 Root.PackageVehicles.vehicle [Part]
    type=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [Part]
      multiplicity=4
      type=Root.PackageVehicles.Wheel
  Root.PackageVehicles.vehicle.partnotype2 [Part]
      type=None
```

## Comments

A `Part` element may have no type, as shown above for the elements
`partnotype1` and `partnotype2`. This opens the question, what is
the type of such element after parsing?


## Rules/constraints

N/A


