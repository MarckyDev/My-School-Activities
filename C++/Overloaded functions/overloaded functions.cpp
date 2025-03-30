#include <iostream>

using namespace std;

//my overloaded functions
//sphere volume
//z is radius

float volume (const float PI, float z)
{ 
	return ((4 * PI * z * z * z)/3);
}
//cylinder volume
//y is radius, z is height
double volume (const double PI, double y, double z)
{
	return (PI * (y * y )* z);
}
//rectangle Volume
// x is length, y is width, z is height
int volume (int x, int y, int z)
{
	return (x * y * z);
}

int main (){

	int x = 5;
	int y = 4;
	int z = 3;
	
	
	float f1 = 3.1416, f2 = 3;
	double d1 = 3.1416, d2 = 4, d3 = 3;
	int i1 = 5, i2 = 4, i3 = 3;
	
	
	cout << "Sphere Volume : " << volume (f1, f2)<<"\n";
	
	cout << "Cylinder Volume : "<< volume (d1, d2, d3)<<"\n";
	
	cout << "Rectangle Volume : " << volume (i1, i2, i3)<<"\n";
	
	return 0;
}
