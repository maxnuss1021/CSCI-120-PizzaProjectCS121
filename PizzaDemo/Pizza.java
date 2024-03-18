import java.util.*;
public class Pizza {
    //variables to be used later.
    public String[] arr;
    public int price;
    int amount;
    String print = "";
    // constructor takes ina string and the quantity of toppings
    Pizza(String[] arr, int quant) {
        this.arr = arr;
        amount = quant;
        int x = 0;
        //adds the quantity to the final message
        while (x != quant) {
            print += " " + arr[x] + ",";
            x++;
        }

        price = 14 + (2 * amount);
    }
    //when called gives the final message
    public String getString() {
        return "Pizza with toppings:" + print + "\nTotal Price: $" + price;
    }
}
