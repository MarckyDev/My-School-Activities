import java.util.Arrays;
import java.util.Random;

public class Main {

    /*
    * BUBBLE SORT
    * Swaps the elements the adjacent elements if not in order
    * e.g.[1, 3, 2]
    * Swaps 3 & 2, so it's in order
    * result : [1, 2, 3]
    */

    static void bubbleSort(int[] array){
        //goes through the elements of the array
        for(int i = 0; i < (array.length - 1); i++){
            //defines first the truth value of swapped variable since it will be used for
            //checking if the two elements are swapped
            boolean swapped = false;
            //goes through the previous element of the array
            for(int j = 0; j < (array.length - i - 1); j++){
                //compares the current element [i] to the past element[j]
                if (array[j] > array[j + 1]){
                    //with a temporary variable, we swap the places of the previous and current element
                    int tempArr = array[j];
                    array[j] = array[j+1];
                    array[j + 1] = tempArr;
                }
                swapped = true;
            }
            if(!swapped)
                break;
        }
    }

    /*
    * INSERTION SORT
    * The collection is partially split into a sorted and unsorted portion
    * values in unsorted portion will then be sorted
    * O(n^2), asymptotic notation
    */

    static void insertionSort(int[] array){
        //this for loop scans everything inside the array
        for(int i = 1; i < (array.length-1); i++){
            //this is the temporary variable that will store the value of the element
            int currentValue = array[i];

            //this is to set the value of j to the previous index of i
            int j = i - 1;

            //while j is less than or equal to 0 and the index j of array is greater than  the currentValue then,
            while(j >= 0 && array[j] > currentValue){
                //add 1 to index j then set its value to the array[j]
                //shifts* to the right
                array[j + 1] = array[j];
                //then decrement j
                j--;
            }
            //then set the new value of array[j+1] to the value of our key
            array[j + 1] = currentValue;
        }
    }

    /*
    * SELECTION SORT
    *  - a sorting algorithm that repeatedly selects the smallest and the largest element then swaps it
    */

    static void selectionSort(int[] array){
        //moves through the array
        for(int i = 0; i < (array.length - 1); i++){

            //finds the least value inside the array
            int minimumIndex = i;
            for(int j = i + 1; j < array.length; j++){
                if(array[j] < array[minimumIndex]){
                    minimumIndex = j;
                }

            //this is where the swapping of elements occurs
            //swaps the found minimum element with the first element
            int tempVar = array[minimumIndex];
            array[minimumIndex] = array[i];
            array[i] = tempVar;
            }
        }
    }

    /*
    * MERGE SORT
    * a divide and conquer algorithm that divides the array into smaller arrays which then it sorts
    * once the divided arrays are sorted, then it will be merged and resorted into its original form
    */
    static void mergeSort(int[] array){
        int arrayLength = array.length;
        if (arrayLength < 2){
            return;
        }
        //divides the array into two
        int middleIndex = arrayLength / 2;

        //the left half of the array
        int[] leftHalf = new int[middleIndex];

        //gets the other half of the divided array
        int[] rightHalf = new int[arrayLength - middleIndex];

        //copies the content of the unsorted left half of the array into the left half array
        for(int i = 0; i < middleIndex; i ++){
            leftHalf[i] = array[i];
        }
        /*
        * OR WE COULD USE THE Arrays.arraycopy() method for this one :))
        */

        //copies the content of the unsorted right half of the array into the right half array
        for(int i = middleIndex; i < arrayLength; i ++){
            rightHalf[i - middleIndex] = array[i];
        }

        //merges the sorted values of the left half*
        mergeSort(leftHalf);
        //merges the sorted values of the right half*
        mergeSort(rightHalf);

        //merges all the array
        merge(array, leftHalf, rightHalf);
    }
    static void merge(int[] array, int[] leftHalf, int[] rightHalf){
        //gets the lengths of the left and right arrays
        int leftLength = leftHalf.length;
        int rightLength = rightHalf.length;
        //incrementer for leftHalf(i), rightHalf(j) and array (k)
        int i = 0, j = 0, k = 0;

        //sorts and merges the left and right halves of the divided array
        while (i < leftLength && j < rightLength){
            if (leftHalf[i] <= rightHalf[j]){
                array[k] = leftHalf[i];
                i++;
            }else{
                array[k] = rightHalf[j];
                j++;
            }
            k++;
        }

        //transfers the elements from leftHalf to the input array
        while(i < leftLength){
            array[k] = leftHalf[i];
            i++;
            k++;
        }

        while(j < rightLength){
            array[k] = rightHalf[j];
            j++;
            k++;
        }
    }

    /*
    * QUICKSORT
    * is also a divide and conquer algorithm
    * pivots or focus of the sorting could be the last, first or the middle index
    * recursive sorting algorithm
    */

    //overloaded the quickSort method to simplify the call
    static void quickSort(int[]array){
        quickSort(array, 0, array.length - 1);
    }

    static void quickSort(int[] array, int minIndex, int maxIndex){

        if(minIndex >= maxIndex){
            return;
        }
        //randomly sets the pivot at the last index of the given array
        int pivotIndex = new Random().nextInt(maxIndex - minIndex) + minIndex;
        int pivot = array[pivotIndex];
        swap(array, pivotIndex, maxIndex);

        //partition here
        int leftPointer = partition(array, minIndex, maxIndex, pivot);

        //recursively calls to sort the array
        quickSort(array, minIndex, leftPointer - 1);
        quickSort(array, leftPointer + 1, maxIndex);
    }

    static int partition(int[] array, int minIndex, int maxIndex, int pivot){
        int leftPointer = minIndex;
        int rightPointer = maxIndex - 1;

        while(leftPointer < rightPointer){

            //left pointer scans through the array larger than the pivot starting from the first index of the array
            while(array[leftPointer] <= pivot && leftPointer < rightPointer){
                leftPointer++;
            }
            //right pointer scans through the array less than the pivot starting from the maximum index of the array
            while(array[rightPointer] >= pivot && leftPointer < rightPointer){
                rightPointer--;
            }
            //then swap the value of the left and right pointers
            swap(array, leftPointer, rightPointer);

        }
        //moves the lower index to the left, then the higher index gets moved to the right

        //when left and right pointer points at the same element, swap it to the value of the pivot
        if(array[leftPointer] > array[maxIndex]){
            swap(array, leftPointer, maxIndex);
        }else{
            leftPointer = maxIndex;
        }
        return leftPointer;
    }

    //swap method for quick sort
    static void swap(int[] array, int idx1, int idx2){
        int tempVar = array[idx1];
        array[idx1] = array[idx2];
        array[idx2] = tempVar;
    }

    static int[] randomIntArray(int length){
        Random random = new Random();
        int[] array = new int[length];
        for(int j = 0; j <= array.length - 1; j++){
            int element = random.nextInt(100);
            array[j] = element;
        }
        return array;
    }

    public static void main(String[] args) {

        System.out.println("============\nBUBBLE SORT\n============");

        int[] to_be_sorted = randomIntArray(10);

        //using Arrays Library static function toString() in order to print the array value as a string
        System.out.println("This is the unsorted array\n" + Arrays.toString(to_be_sorted));

        //static method then call with classname.methodName
        Main.bubbleSort(to_be_sorted);

        //using Arrays Library static function toString() in order to print the array value as a string
        System.out.println("This is the sorted array\n" + Arrays.toString(to_be_sorted));

        System.out.println("==============\nINSERTION SORT\n==============");

        //new array declared with the same variable name
        to_be_sorted = randomIntArray(10);

        //using Arrays Library static function toString() in order to print the array value as a string
        System.out.println("This is the unsorted array\n" + Arrays.toString(to_be_sorted));

        //static method then call with classname.methodName
        Main.insertionSort(to_be_sorted);

        //using Arrays Library static function toString() in order to print the array value as a string
        System.out.println("This is the sorted array\n" + Arrays.toString(to_be_sorted));

        System.out.println("==============\nSELECTION SORT\n==============");
        //new array declared with the same variable name
        to_be_sorted = randomIntArray(10);
        //using Arrays Library static function toString() in order to print the array value as a string
        System.out.println("This is the unsorted array\n" + Arrays.toString(to_be_sorted));

        //static method then call with classname.methodName
        Main.selectionSort(to_be_sorted);

        //using Arrays Library static function toString() in order to print the array value as a string
        System.out.println("This is the sorted array\n" + Arrays.toString(to_be_sorted));

        System.out.println("==============\nMERGE SORT\n==============");
        //new array declared with the same variable name
        to_be_sorted = randomIntArray(15);

        //using Arrays Library static function toString() in order to print the array value as a string
        System.out.println("This is the unsorted array\n" + Arrays.toString(to_be_sorted));

        //static method then call with classname.methodName
        Main.mergeSort(to_be_sorted);

        //using Arrays Library static function toString() in order to print the array value as a string
        System.out.println("This is the sorted array\n" + Arrays.toString(to_be_sorted));

        System.out.println("==============\nQUICK SORT\n==============");
        //new array declared with the same variable name
        to_be_sorted = randomIntArray(20);

        //using Arrays Library static function toString() in order to print the array value as a string
        System.out.println("This is the unsorted array\n" + Arrays.toString(to_be_sorted));

        //static method then call with classname.methodName
        Main.quickSort(to_be_sorted);

        //using Arrays Library static function toString() in order to print the array value as a string
        System.out.println("This is the sorted array\n" + Arrays.toString(to_be_sorted));
    }
}