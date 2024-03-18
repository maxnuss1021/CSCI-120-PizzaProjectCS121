public class DeliverPizza extends Pizza{
    //variables
    int newPrice;
    String Address;
    //constructor that takes in the number of toppings and an array of strings
    DeliverPizza ( String Address, int numOfToppings, String [] arr){
        super(arr, numOfToppings);
        this.Address = Address;
        //changes the price based on how expensive the order was.
        if (numOfToppings > 4){
            newPrice = price + 3;
        }
        else{ newPrice = price + 5;}
        //final message
        print = print +" Delivery cost depends on the price of the pizza. It will be delivered to "+ Address;
    }


}
