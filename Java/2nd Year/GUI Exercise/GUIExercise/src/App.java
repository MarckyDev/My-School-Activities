import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
public class App extends JFrame implements ActionListener, MouseListener{
    JLabel homeLabel, paneLabel;
    JPanel mouseListenerPanel;
    App(){
        

        JButton home = new JButton("Home");
        home.addActionListener(this);
        home.setBackground(null);
        home.setBorder(null);
        home.setFocusable(false);
        home.setBounds(0, 0, 50, 200);
        home.setForeground(Color.WHITE);

        homeLabel = new JLabel("BAHAY");
        homeLabel.setVisible(false);

        JButton clearButton = new JButton("Clear");
        clearButton.addActionListener(clear);
        clearButton.setBackground(null);
        clearButton.setBorder(null);
        clearButton.setFocusable(false);
        clearButton.setBounds(0, 0, 50, 200);
        clearButton.setForeground(Color.WHITE);

        JButton tignanMoto = new JButton("See?");
        tignanMoto.addActionListener(yesNo);
        tignanMoto.setBackground(null);
        tignanMoto.setBorder(null);
        tignanMoto.setFocusable(false);
        tignanMoto.setBounds(0, 0, 50, 200);
        tignanMoto.setForeground(Color.WHITE);


        Box box = Box.createHorizontalBox();
        box.add(home);
        box.add(Box.createHorizontalStrut(10));
        box.add(clearButton);
        box.add(Box.createHorizontalStrut(10));
        box.add(tignanMoto);



        JPanel titlePanel = new JPanel();
        titlePanel.setSize(500, 400);
        titlePanel.setBackground(Color.LIGHT_GRAY);
        titlePanel.add(box);

        //default
        paneLabel = new JLabel("This is an interactive Pane!");

        mouseListenerPanel = new JPanel();
        mouseListenerPanel.setBorder(BorderFactory.createMatteBorder(5,5, 5, 5, Color.GRAY));
        mouseListenerPanel.setBackground(Color.ORANGE);
        mouseListenerPanel.add(paneLabel);
        mouseListenerPanel.setBounds(250, 120,500, 500);
        mouseListenerPanel.addMouseListener(this);


        JPanel contentPanel = new JPanel();
        contentPanel.setLayout(null);
        contentPanel.setBounds(0, 0, 500, 500);
        contentPanel.setVisible(true);
        contentPanel.add(homeLabel, BorderLayout.CENTER);
        contentPanel.add(mouseListenerPanel, BorderLayout.CENTER);

        

        this.setTitle("Random GUI");
        this.add(titlePanel, BorderLayout.NORTH);
        this.add(contentPanel, BorderLayout.CENTER);
        this.setVisible(true);
        this.setSize(1000, 1000);
        this.setLocationRelativeTo(null);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }
    void displayOptionPane(){
        int choice;
        choice = JOptionPane.showConfirmDialog(null, "Wanna relly see?", "See?", JOptionPane.YES_NO_OPTION);
        if (choice == JOptionPane.YES_OPTION){
            JOptionPane.showMessageDialog(null, "SEEEEEE MOAR", "SEEEE", JOptionPane.ERROR_MESSAGE);
        }else if (choice == JOptionPane.NO_OPTION){
            JOptionPane.showMessageDialog(null, "WAI NO :(", "y u no see? :c", JOptionPane.PLAIN_MESSAGE);
        }

    }
    ActionListener yesNo = new ActionListener() {

        @Override
        public void actionPerformed(ActionEvent e) {
            displayOptionPane();
        }
        
    };

    ActionListener clear = new ActionListener (){

        @Override
        public void actionPerformed(ActionEvent e) {
            homeLabel.setVisible(false);
        }

    

};
    public static void main(String[] args) throws Exception {
        new App();
    }


    @Override
    public void actionPerformed(ActionEvent e) {
        homeLabel.setVisible(true);
        
    }
    @Override
    public void mouseClicked(MouseEvent e) {
        paneLabel.setText("YOU CLICKED AND I AM WHITE!!");
        mouseListenerPanel.setBackground(Color.WHITE);
    }
    @Override
    public void mousePressed(MouseEvent e) {
        paneLabel.setText("YOU PRESSED AND I AM GREEN!!");
        mouseListenerPanel.setBackground(Color.GREEN);
    }
    @Override
    public void mouseReleased(MouseEvent e) {
        paneLabel.setText("YOU RELEASED AND I AM PINK!!");
        mouseListenerPanel.setBackground(Color.PINK);
    }
    @Override
    public void mouseEntered(MouseEvent e) {
        paneLabel.setText("YOU ENTERED AND I AM BLACK!!");
        mouseListenerPanel.setBackground(Color.black);
    }
    @Override
    public void mouseExited(MouseEvent e) {
        paneLabel.setText("This is an interactive Pane!");
        mouseListenerPanel.setBackground(Color.ORANGE);
    }

   
}
