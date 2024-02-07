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
	int length = 5;
	int sum = 0;
	float b, n[ ] = {2, 4, 6, 8, 10};

	//Computing the sum of the current input array
	int j; 
	for (int i= 0; i<length; i++){
		sum += n[i];
	}
		b = printarray (n, length);
		cout<< "The average of the array [5, 10, 15] is "<<b<<endl;
		cout<< "The sum of the elements of the array [5, 10, 15] is "<<sum<<endl;
		
	return 0;
	
}
