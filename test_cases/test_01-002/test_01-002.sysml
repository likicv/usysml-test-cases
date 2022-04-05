package PackageVehicles {
  
    part def Vehicle;

    part def Wheel {
        part def Lugbolt;
    }

    part vehicle:Vehicle {
        part w:Wheel;
    }
}
