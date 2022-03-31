<!-- Generated on 2022-03-31 15:44:31.566732 from script `gendocs.py`
     DO NOT EDIT MANUALY! -->

# Test Case 01-001: Fully qualified element names (FQEN)


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

1. A `*.sysml` file defines the namespace for the elements it contains.
The top level namespace bounded by the file is assigned to the element
`Root`.
2. Each curly braces segment defines a namespace.
3. Within a `*.sysml` file each FQEN must be unique.


## Comments

In the KerML nomenclature the element names ('Vehicle', 'Wheel' 'vehicle',
and 'w') are `humanId`. Per KerML 7.2.2.1:

> However, one of the aliasIds, the humanId, may be entered by the modeler.
> If given, the humanId for an Element has the lexical form of a name.
> However, an Element may be given different names relative to different
> Namespaces (see 7.2.4), while the humanId for an Element is the same
> in all contexts. Any humanIds of the ownedElements of a Namespace must
> be unique (see 7.2.4), but it is otherwise the responsibility of the
> modeler to maintain other structural or uniqueness properties for
> humanIds as appropriate to the model being created.


The following statement requires that no two elements can have the same
`humanId`:

> Any humanIds of the ownedElements of a Namespace must be unique

This can be restated as follows: no two model elements can have the
same FQEN.


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

# Test Case 01-002: Fully qualified element names (FQEN)


## Description

Parsing of the `*.sysml` file will generate a FQEN for each element, starting
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

1. A \*.sysml file defines the namespace for the elements it contains.
The top level namespace bounded by the file is assigned to the
element “Root”
2. Any valid element can be nested under the “Root” element (in this
example there are two Package elements)


## Issues

A potential issue arises when multiple `*.sysml` files are processed.
Let’s assume two files, `Vehicles1.sysml` and `Vehicles2.sysml` with
the following content:

*--file Vehicles1.sysml--*
```
part def Vehicle;
part def Wheel;
```

*--file Vehicles1.sysml--*
```
part def Vehicle;
```

Let’s assume a SysMLv2 processor `sysmlv2` which can take one or more
`*.sysml` files on the input. Then processing the first file will
result in:

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


# Test Case 01-003: Element Classifiers


## Description

Every element is associated with a Classifier.


## SysML v2 textual notation

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
In output above the element Cassifiers are shown in square brackets
(`Package`, `PartDef`, and `Part`). The following development in
notation is adoped: instead of saying the element `Root.PackageVehicles`
is associated with a Classifer `Package`, it can be said the element
'Root.PackageVehicles' is `Package`.


## Rules/constraints

Every processed element is associated with a Classifier.

# Test Case 01-004: ‘Part’ element type specification


## Description

A `Part` element may have type specified.


## SysML v2 textual notation

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

In the expected outpout types of `Part` elements are shown with
`type= ...`.

In the above example `Part c` doesn’t have a type specified, while
`Part w` is of type `Wheel`, which itself is `PartDef`.


## Rules/constraints

1. A `Part` element may optionally have a type specified
2. If `Part` element has type specified, the type must be an existing
`PartDef` element

# Test Case 01-005: A `Part` element with no type specified


## Description

A `Part` element may have no type specified.


## SysML v2 textual notation

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

A `Part` element may have no type specified, as shown above for the
elements `partnotype1` and `partnotype2`.


## Rules/constraints

None.


## Discussion

A `Part` element may have no type specified. This opens the question
how to handle this situation in the implementation so it is consistent
across different implementations.


# Test Case 01-006: Namespace search rules


## Description

Illustrates the namespace search rules.


## SysML v2 textual notation

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

# Test Case 01-007: Namespace search rules


## Description

Illustrates the namespace search rules.


## SysML v2 textual notation

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

Compare to [Test Case 01-006](#test-case-01-006-namespace-search-rules).


# Test Case 01-008: `Part` element syntactical forms


## Description

Syntactically, `Part` element may appear in several different forms.


## SysML v2 textual notation

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
`PartDef` element as per Test Case #01.004.


## Rules/constraints

An implementation of `part` and `part def` SysMLv2 keywords must support
all seven syntactical forms shown in this Test Case.


# Test Case 02-001: A single line note ("//"-type comment)


## Description

This use case addresses //-type comment


## SysML v2 textual notation

```sysml
package PackageVehicles {

    // an indented comment taking the entire line
    part def Vehicle;// an appended comment without white space
    part def Wheel;           // an appended comment with white space

    part vehicle:Vehicle {
        part w:Wheel[4];
    }
}
// a comment taking the entire line
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

A comment embedded within the SysML v2 textual notation is used to
annotate the textual notation. There are multiple types of comments
in SysML v2 (see KerML 7.1.2.3), and specifically KerML distingushes
*notes* and *comments*, where

* *notes* are used to annotate the SysML textual notation and are
discarded during parsing
* *comments* are parsed and into to Comment elements and are stored
as part of the model

This test case addresses only *note*, and furthermore of the two
kind of notes (*singe line note* and *multiline note*) addressed
only a single-line note.


## Rules/constraints

As per KerML 7.1.2.3:

>"A single-line note includes all the text from the initial
>characters '//' up to the next line terminator or the end
>of the input text (whichever comes first)."


# Test Case 02-002: Unrestricted names (basic form)


## Description

Element names can contain spaces when enclosed by single quotes.


## SysML v2 textual notation

```sysml
package 'My PackageVehicles' {

    part def 'Vehicle';
    part def Wheel;

    part 'vehicle':Vehicle {
        part w:Wheel[4];
    }
}
```


## Expected output

```
Root.'My PackageVehicles' [Package]
 Root.'My PackageVehicles'.Vehicle [PartDef]
 Root.'My PackageVehicles'.Wheel [PartDef]
 Root.'My PackageVehicles'.vehicle [Part]
    type=Root.'My PackageVehicles'.Vehicle
  Root.'My PackageVehicles'.vehicle.w [Part]
      multiplicity=4
      type=Root.'My PackageVehicles'.Wheel
```


## References

The spiral 1 test cases use basic names. This test case tests use of
unrestricted names, but only in the basic form without the use of escape
sequences.

As per KerML p20, there are two kinds of names:


> 1. A basic name is one that can be lexically distinguish in itself from
> other kinds of tokens. The initial character of a basic name must be one
> of a lowercase letter, an uppercase letter or an underscore. The remaining
> characters of a basic name are allowed to be any character allowed as an
> initial character plus any digit. However, a reserved keyword may not be
> used as a name, even though it has the form of a basic name (see 7.1.2.7),
> including the Boolean literals true and false.
> 
> 2. An unrestricted name provides a way to represent a name that contains
> any character. It is represented as a non-empty sequence of characters
> surrounded by single quotes. The characters within the single quotes may
> not include non-printable characters (including backspace, tab and newline).
> However, these characters may be included as part of the name itself
> through use of an escape sequence. In addition, the single quote character
> or the backslash character may only be included by using an escape sequence.


## Issues

The SysML v2 example shown in [Test Case 02-002](#test-case-02-002-unrestricted-names-basic-form)
works in the SysMl v2 Pilot implementation, however the visualisation
with `%viz` is unable to handle unrestricted names:


```jupyter
%viz --view=tree 'My PackageVehicles'

ERROR:Couldn't resolve reference to Element ''My'
```


## Rules/constraints

None.

# Test Case 03-001: `attribute def` example use


## Description

Shows possible placement of the `attribute def` statement.


## SysML v2 textual notation

```sysml
// 'attribute def' within the sysml file scope, outside any packages
attribute def ModuleId;

package PackageVehicles {

    // 'attribute def' within a top level package
    attribute def PackageVehiclesID;

    package VehicleAccessories {

        // 'attribute def' within a nested package
        attribute def AccessoryID;

        package SeatCover {
            // 'attribute def' within a second nested package-- no limit to possible nesting
            attribute def SeatCoverColor;
        }
    }

    part def Vehicle {
        // 'attribute def' within 'part def'
        attribute def Color;
    }

    part def Wheel;

    part vehicle:Vehicle {
        // 'attribute def' within 'part'
        attribute def RegistrationNumber;
        part w:Wheel[4];
    }
}
```


## Expected output

```
Root.ModuleId [AttributeDef]
Root.PackageVehicles [Package]
 Root.PackageVehicles.PackageVehiclesID [AttributeDef]
 Root.PackageVehicles.VehicleAccessories [Package]
  Root.PackageVehicles.VehicleAccessories.AccessoryID [AttributeDef]
  Root.PackageVehicles.VehicleAccessories.SeatCover [Package]
   Root.PackageVehicles.VehicleAccessories.SeatCover.SeatCoverColor [AttributeDef]
 Root.PackageVehicles.Vehicle [PartDef]
  Root.PackageVehicles.Vehicle.Color [AttributeDef]
 Root.PackageVehicles.Wheel [PartDef]
 Root.PackageVehicles.vehicle [Part]
    type=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.RegistrationNumber [AttributeDef]
  Root.PackageVehicles.vehicle.w [Part]
      multiplicity=4
      type=Root.PackageVehicles.Wheel
```


## Comments

This Test Case shows `attribute def` when placed:
1. Within the sysml file scope, outside any packages
2. Top level `package`
3. Within a nested package
4. Within a second nested package
5. Within `part def`
6. Within `part`


## Rules/constraints

Within the scope of uSysML v0.03 there are no constraints where `attribute def`
can be used.

