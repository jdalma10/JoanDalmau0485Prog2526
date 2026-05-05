package prova;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.*;

public class TextFieldExample extends JFrame {
    public TextFieldExample() {
        setTitle("TextField Example");
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(new GridLayout(3, 1, 10, 10));
        setSize(360, 180);
        setLocationRelativeTo(null);

        JLabel label = new JLabel("Type something and press Enter or the button:", SwingConstants.CENTER);
        JTextField textField = new JTextField();
        JButton copyButton = new JButton("Copy text to label");
        JLabel resultLabel = new JLabel("", SwingConstants.CENTER);

        textField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                    resultLabel.setText(textField.getText());
                }
            }
        });

        copyButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                resultLabel.setText(textField.getText());
            }
        });

        add(label);
        add(textField);
        add(copyButton);
        add(resultLabel);
        pack();
        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TextFieldExample());
    }
}
