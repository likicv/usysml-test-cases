package PackageVehicles1 {
  
    part def Vehicle;
    part def Wheel {
        
    }

    part vehicle:Vehicle {
        part w:Wheel[4];
    }
}

package PackageVehicles2 {

    part def Vehicle;
    part def Wheel;

    part vehicle:Vehicle {
        part def Wheel;
        part w:Wheel[4] {
            part lb:Lugbolt;
        }
    }
}

part def Lugbolt;
