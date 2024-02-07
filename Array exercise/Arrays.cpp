#include <iostream>

using namespace std;

int main (){
	
	int AR[10]; //array for 10 integers
	
	cout<<"Enter 10 integers"<<endl;
		for (int i=0; i<10 ;i++)
			cin>>AR[i];
		cout<<endl;
	cout<< "The integers are: ";
		for (int i=0; i<10;i++)
			cout<<AR[i]<<" ";
		cout<<endl;
		
	return 0;
}