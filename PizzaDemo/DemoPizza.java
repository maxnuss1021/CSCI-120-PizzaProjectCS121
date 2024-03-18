import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
import java.awt.*;
//import libraries

public class DemoPizza extends JFrame implements ActionListener {
    //different things to be used in my first JFrame
    public static String[] arr = new String[10];
    ImageIcon icon = new ImageIcon("/Users/maxnussbaum/Desktop/welcomepizza.jpg");
    Image image = icon.getImage();
    Image scaledImage = image.getScaledInstance(460, 340, Image.SCALE_SMOOTH);
    JLabel label = new JLabel(new ImageIcon(scaledImage));
    static int counter = 0;
    JLabel header = new JLabel("($14 pizza) What is your next topping? (+$5) (press quit to quit)");
    JTextField text = new JTextField(20);
    JButton cont = new JButton("Continue");
    JButton quit = new JButton("Quit");
    JButton delivery = new JButton("Delivery?");
    //adds elements
    public DemoPizza() {
        setSize(500, 500);
        setLayout(new FlowLayout());
        add(header);
        add(text);
        add(cont);
        add(quit);
        add(delivery);
        add(label);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        cont.addActionListener(this);
        quit.addActionListener(this);
        delivery.addActionListener(this);
    }
    // different actions done by the user
    @Override
    public void actionPerformed(ActionEvent e) {
        //if continue pressed then it goes to the next screen
        if (e.getSource() == cont) {
            if (counter < 10) {
                arr[counter] = text.getText();
                System.out.println(arr[0]);
                counter++;
                DemoPizza order = new DemoPizza();
                order.setVisible(true);
            } else {
                JOptionPane.showMessageDialog(this, "Maximum limit reached");
            }
        }
        //if you put in too many orders or you decide to quit it will just print your order
        if (e.getSource() == quit || counter == 10) {
            Pizza order = new Pizza(arr, counter);
            Display d1 = new Display(order.getString());
            d1.setVisible(true);
        }
        //if you want delivery you will go to delivery
        if (e.getSource() == delivery) {
            Delivery order = new Delivery(arr, counter);
            order.setVisible(true);
        }
    }
//main function runs the program
    public static void main(String[] args) {
        DemoPizza order = new DemoPizza();
        order.setVisible(true);
    }
}
//this is for deliveries
class Delivery extends JFrame implements ActionListener {
    //variables
    public String[] arr;
    public int counter;
    public String address;
    JLabel header = new JLabel("Address?");
    JTextField text = new JTextField(20);
    JButton cont = new JButton("Continue");
//constructor takes in the array and counter.
    public Delivery(String[] arr, int counter) {
        super();
        this.arr = arr;
        this.counter = counter;
        setSize(500, 500);
        setLayout(new FlowLayout());
        add(header);
        add(text);
        add(cont);
        cont.addActionListener(this);
    }
//tracks when the user hits continue and then calls the final slide
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == cont) {
            address = text.getText();
            DeliverPizza order = new DeliverPizza(address, counter, arr);
            Display d1 = new Display(order.getString());
            d1.setVisible(true);
        }
    }
}

//final slide displays the order
class Display extends JFrame {
    private JLabel message;

    Display(String p) {
        super();
        message = new JLabel(p);
        setSize(1000, 500);
        setLayout(new FlowLayout());
        add(message);
    }
}
