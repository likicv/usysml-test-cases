package PackageVehicles {

    part def Vehicle {
        attribute def Color;
    }
    part def Wheel;

    part vehicle:Vehicle {
        part w:Wheel[4];
    }
}
