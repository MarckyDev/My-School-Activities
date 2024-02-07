#include <iostream>

using namespace std;

int main (){
	int element, j;
	cout << "Enter the number of elements from (1 to 10)" <<endl;
	cin >>element;
	double n[element];
	for(int j=0; j<element; j++){
		cout<<"Element values [" << j <<"] : "<<endl;
		cin>> n[j];
	}

	int largest = n[0];
	
	for(int i=1;i<element;i++){
		
			if (largest < n[0])			
		
			largest = n[0];
	cout << "The largest element is : "<< largest <<endl;
	break;
	}
	return 0;
}