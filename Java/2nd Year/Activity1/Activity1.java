/* ITEM # 1 ACTIVITY 2
Mapa, Marc Rovic M.
CS-2102
CS-211: OBJECT-ORIENTED PROGRAMMING
OCTOBER 1, 2022
*/

class Main {
    public static void main (String[] args){
        // Square the contents of the array
        int[] Item1Array = {
                2, 3, 5, 100, 7, 3, 5, 3, 1, 4,
                76, 77, 78, 79, 80, 54, 68, 61, 34, 33,
                44, 49, 100, 5, 2, 87, 34, 33, 2, 1,
                4, 5, 8, 2, 1, 8, 5, 3, 2, 1,
                88, 22, 23, 33, 48, 44, 46, 48, 50, 52,
                45, 47, 49, 51, 53, 1, 1, 1, 1, 1,
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                11, 22, 33, 44, 55, 66, 77, 88, 99, 100,
                1000, 2001, 3000, 4001, 5000, 6001, 7000, 8001, 9000, 10001
        };

        for(int value : Item1Array){
            System.out.println(value * value);
        }
    }
}

