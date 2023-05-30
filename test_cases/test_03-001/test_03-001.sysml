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
