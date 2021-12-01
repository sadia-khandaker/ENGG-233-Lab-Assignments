class Location:
    def __init__(self,location_name,x,y):
        self.name = location_name
        self.x = x
        self.y = y
        
    
    def calculate_distance(self, other):
        distance =((((self.x - other.x )**2) + ((self.y -other.y)**2) )**0.5)
        return distance
        
    def to_string(self):
        return ("Name: "+self.name+", x-coordinate: "+str(self.x)+", y-coordinate: "+str(self.y))

class HospitalList:
    def __init__(self):
        self.hospitals = []
        
    def print_hospital_at(self,i):
        if i<=(len(self.hospitals)-1):
            print (self.hospitals[i].to_string())
        else:
            print("Out of Bounds.")


    def add_new_hospital(self,location_new_hospital):
        self.hospitals.append(location_new_hospital)

    def get_hospital_at(self, i):
        if i<=(len(self.hospitals)-1):
            return self.hospitals[i]
        else:
            print("Out of bounds.")
    
    def to_string(self):
        result = ""
        for i in self.hospitals:
            result = result + i.to_string() + '\n'
        return result


def find_closest_hospital(hospital_list,location_accident):
    smallest_distance=hospital_list.get_hospital_at(0).calculate_distance(location_accident)
    closest = 0

    if len(hospital_list.hospitals) == 0:
        return -1
    else:
        for i in range(1,len(hospital_list.hospitals)):
            distance = hospital_list.get_hospital_at(i).calculate_distance(location_accident)
            if (distance<smallest_distance):
                smallest_distance=distance
                closest = i 
        return hospital_list.get_hospital_at(closest)

def get_location():
    name = input("Enter the location name of hospital: ")
    x = int(input("Enter the x-coordinate of hospital: "))
    y = int(input("Enter the y-coordinate of hospital: "))
    location = Location(name,x,y)
    return location    
        
def main():
    hospital_list = HospitalList()
    for i in range(0,2):
        location = get_location()
        hospital_list.add_new_hospital(location)
    
    print(hospital_list.to_string())
    
    location_accident = Location("A",-12628,7535)
    print(location_accident.to_string())
    
    closest_location = find_closest_hospital(hospital_list, location_accident)
    print("The closest hospital to the accident point is", closest_location.to_string())
    
if __name__ == "__main__":
    
    main()