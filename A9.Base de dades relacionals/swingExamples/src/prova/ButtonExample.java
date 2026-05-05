package prova;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class ButtonExample extends JFrame {
    private int clickCount = 0;
    private JLabel statusLabel;

    public ButtonExample() {
        setTitle("Button Example");
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));
        setSize(320, 140);
        setLocationRelativeTo(null);

        JButton button = new JButton("Click me!");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                clickCount++;
                statusLabel.setText("Clicks: " + clickCount);
            }
        });

        statusLabel = new JLabel("Clicks: 0", SwingConstants.CENTER);

        add(button, BorderLayout.CENTER);
        add(statusLabel, BorderLayout.SOUTH);
        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ButtonExample());
    }
}
