import java.util.Scanner;

public class Order {
    static Scanner input = new Scanner(System.in);

    //for global condition, updates in a method
    static int inp = 0;

    //boolean 
    static boolean empty = true;
    //Arrays
    static float[] arr_order = new float[5];
    static float[] item_rice = {39, 45};
    static float[] item_drink = {20, 15};

    //another switch case for adding the prices into the arr_order array
    public static void choice(int src, int destpos) {
        if (inp ==2){
            System.out.println("Is it Ala carte? YES or NO?");
            String lagay = input.nextLine();
            
            switch(lagay){
                //meal case
                case "YES" , "yes":
                System.arraycopy(item_rice, src, arr_order, destpos, 5);
                break;
                case "NO", "no":
                //DRINKS CASE
                System.out.println("Please choose a drink below: ");
                System.out.println("[1] P20.00 Coke Mismo \n[2] P15.00 Gulaman");
                int drink_inp = input.nextInt();
                if (drink_inp == 1){
                    //coke mismo
                    System.arraycopy(item_drink, src, arr_order,destpos, 5);

                } else if(drink_inp == 2){
                    //gulaman
                    System.arraycopy(item_drink, src, arr_order, destpos, 5);
                }
                break;
            }
        }
    }

    //check if the array is empty or has any contents
public static void check_contents(float[] array){
    if (array == null || array.length == 0){
        empty = true;
    }else{
        empty = false;
    }
    }

    public static void main(String[] args) {
        
        
        System.out.println("============== MAIN MENU =============== ");
        System.out.println("Please select from the choices below:");
        System.out.println("[1] Rice Meals");
        System.out.println("[2] Drinks");
        System.out.println("[3] EXIT");
        
        int inp = input.nextInt();
        do{
            switch(inp){
                case 1:
                System.out.println("[1] P39.00 Sisig with rice \n[2] P45.00 Tocilog\n");
                    int inp1 = input.nextInt();
                    if (inp1 == 1){
                        check_contents(arr_order);
                        if (empty == true){
                            choice(0, 0);
                        }else{
                            choice(0,1);
                        }
                    } else if (inp1 == 2){
                        if (empty == true){
                            choice(0, 0);
                        }else{
                            choice(1, 1);
                        }
                    }
                break;
                case 2:
                System.out.println("Please choose a drink below: ");
                System.out.println("[1] P20.00 Coke Mismo \n[2] P15.00 Gulaman");
                int drink_inp = input.nextInt();
                if (drink_inp == 1){
                    //coke mismo
                    if (empty == true){
                        choice(0, 0);
                    }else{
                        choice(0,1);
                    }

                } else if(drink_inp == 2){
                    //gulaman
                    if (empty == true){
                        choice(0, 0);
                    }else{
                        choice(1,1);
                    }
                }
                break;
                case 3:
                break;
                default:
                System.out.println("Invalid input try again");
            }
            ///input.close();
        }while(inp != 3);
        

        
    }

}
