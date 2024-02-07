#include <iostream>

using namespace std;

int main (){
	
	int AR[5], num, sum = 0;
	cout <<"Enter the size of the array : ";
		cin >> num;
	cout<< "\n Enter the elements of the array :" <<endl;
	for (int i=0; i<num; i++)
		cin>>AR[i];
		for (int i=0; i<num; i++){
			sum +=AR[i];
		}
		cout <<"Sum of array elements :" <<sum;
		return 0;
}