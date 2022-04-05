<!-- Generated on 2022-04-05 21:51:37.871976 from script `gendocs.py`
     DO NOT EDIT MANUALY! -->

# Test Case 01-001: Fully qualified element names (FQEN)


## Description

Parsing a `*.sysml` file will generate a FQEN for each element,
starting with `Root`.


## Scope

The scope of this Test Case is uSysML v0.01, the applicable
keywords are: `package`, `part def`, and `part`.


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
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [PartUsage]
      typed by=Root.PackageVehicles.Wheel
```


## Discussion

Within a sysml file all fully qualified element names (FQENs)
must be uniqe. The following example should generate an error,
because both `part def Wheel` and `part Wheel` have the same
FQEN `PackageVehicles.Wheel`:


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


## Notes


*NOTE 1*: This test case assumes that `*.sysml` file defines the namespace
for the elements it contains. The top level namespace bounded by the file
is assigned to the element `Root`.

*NOTE 2*: Currently, the Pilot implementation pocesses the last example
above with no errors, but issues a warning:

```sysml
WARNING:Duplicate owned member name (1.sysml line : 4 column : 14)
```



# Test Case 01-002: PartDefinition element


## Description

Explores basic properties of a PartDefinition element.


## Scope

The scope of this Test Case is uSysML v0.01, the applicable keywords
are: `package`, `part def`, and `part`.


## SysML v2 textual notation

```sysml
package PackageVehicles {
  
    part def Vehicle;

    part def Wheel {
        part def Lugbolt;
    }

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
  Root.PackageVehicles.Wheel.Lugbolt [PartDef]
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [PartUsage]
      typed by=Root.PackageVehicles.Wheel
```


## Discussion

The keyword `part def` declares a part definition element. A part defintion
element is called *PartDefinition* in the Sysml v2 abstract syntax diagrams.

The base type of every *PartDefinition* is `Parts::Part` from the Systems
Library. This means that every *PartDefintion* is a subclass, directly or
indirectly, of `Parts::Part` from the Systems Library.

An element declared with the keyword `part def` is *PartDefinition*. This
is a *definition element*. The purpose of definition elements is to type
appropriate usage elements. The usage element that can be typed by
*PartDefinition* is *PartUsage*, declared with the keyword `part`.
*PartUsage* is a usage element that represent usage of a part definition.
See [Test Case 01-003](#test-case-01-003-partusage-element) ).

There are other definition elements. For example, the keywords `attribute def`
and `attribute` define *AttributeDefintion* and *AttributeUsage* elements.

In the textual notation example given above, the following elements are
*PartDefinition*:
* `part def Vehicle;` -- 'Vehicle' is *PartDefinition* without the body
specified
* `part def Wheel { part def Lugbolt; }` -- 'Wheel' is *PartDefinition*
with a body which defines its namespace, and declares another
*PartDefinition* 'Lugbolt'.

The nested elements within `part def` are referred to as its features.
Thus in the above example `Wheel` is *PartDefinition* with one feature,
`Lugbolt` which is also *PartDefinition*.


## Notes

None.

# Test Case 01-003: PartUsage element


## Description

Explores basic properties of a PartUsage element.


## Scope

The scope of this Test Case is uSysML v0.01, the applicable keywords
are: `package`, `part def`, and `part`.


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
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [PartUsage]
      typed by=Root.PackageVehicles.Wheel
Root.PackageStations [Package]
 Root.PackageStations.VehicleStation [PartDef]
```


## Discussion and notes



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
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.c [PartUsage]
      typed by=None
  Root.PackageVehicles.vehicle.w [PartUsage]
      typed by=Root.PackageVehicles.Wheel
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
 Root.PackageVehicles.partnotype1 [PartUsage]
    typed by=None
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [PartUsage]
      multiplicity=4
      typed by=Root.PackageVehicles.Wheel
  Root.PackageVehicles.vehicle.partnotype2 [PartUsage]
      typed by=None
```


## Comments

A `Part` element may have no type specified, as shown above for the
elements `partnotype1` and `partnotype2`.


## Rules/constraints

None.


## Discussion

None.

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
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.Wheel [PartDef]
  Root.PackageVehicles.vehicle.w [PartUsage]
      multiplicity=4
      typed by=Root.PackageVehicles.vehicle.Wheel
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
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [PartUsage]
      multiplicity=4
      typed by=Root.PackageVehicles.Wheel
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
 Root.PackageVehicles.test_vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.a [PartUsage]
      multiplicity=2
      typed by=Root.PackageVehicles.WheelAxle
  Root.PackageVehicles.vehicle.w [PartUsage]
      multiplicity=4
      typed by=Root.PackageVehicles.Wheel
   Root.PackageVehicles.vehicle.w.LugBolt [PartDef]
Root.SupportComponents [Package]
 Root.SupportComponents.parking_space [PartUsage]
    typed by=None
 Root.SupportComponents.vehicle_shed [PartUsage]
    multiplicity=4
    typed by=None
 Root.SupportComponents.repair_shop [PartUsage]
    multiplicity=2
    typed by=None
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
`PartDef` element as per [Test Case 01-004](#test-case-01-004-part-element-type-specification).


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
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.w [PartUsage]
      multiplicity=4
      typed by=Root.PackageVehicles.Wheel
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
 Root.'My PackageVehicles'.vehicle [PartUsage]
    typed by=Root.'My PackageVehicles'.Vehicle
  Root.'My PackageVehicles'.vehicle.w [PartUsage]
      multiplicity=4
      typed by=Root.'My PackageVehicles'.Wheel
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
 Root.PackageVehicles.vehicle [PartUsage]
    typed by=Root.PackageVehicles.Vehicle
  Root.PackageVehicles.vehicle.RegistrationNumber [AttributeDef]
  Root.PackageVehicles.vehicle.w [PartUsage]
      multiplicity=4
      typed by=Root.PackageVehicles.Wheel
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

