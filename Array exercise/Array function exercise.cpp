#include <iostream>

using namespace std;

	//average function
	float printarray(float arr[], int length){
		
		int i;
		
		float avg, sum = 0;
		
		for (i=0;i<length;i++){
			sum += arr[i];
		}
		avg = sum/length;
		return avg;
	}
int main(){
	int length = 3;
	int sum = 0;
	float b, n[ ] = {5, 10, 15};

	//Computing the sum of the current input array
	int j; 
	for (int i= 0; i<length; i++){
		sum += n[i];
	}
		b = printarray (n, length);
		cout<< "The average of the array [5, 10, 15] is "<<b<<endl;
		cout<< "The sum of [5, 10, 15] is "<<sum<<endl;
		
	int m = 5;
	int summage = 0;
	float arr[ ] = {2, 4, 6, 8, 10};

	int l;
	//addition of elements
	for (int l=0;l<m;l++){
		summage += arr[l];
	}
		b = printarray (arr, m);		
		cout<< "The Average of the array [2, 4, 6, 8, 10] is "<<b<<endl;
		cout<< "The sum of [2, 4, 6, 8, 10] is "<<summage<<endl;
	
	return 0;
}