package prova;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class ComboBoxExample extends JFrame {
    public ComboBoxExample() {
        setTitle("ComboBox Example");
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));
        setSize(360, 170);
        setLocationRelativeTo(null);

        String[] colors = {"Red", "Green", "Blue", "Yellow"};
        JComboBox<String> comboBox = new JComboBox<>(colors);
        JLabel selectedLabel = new JLabel("Selected color: " + colors[0], SwingConstants.CENTER);

        comboBox.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                selectedLabel.setText("Selected color: " + comboBox.getSelectedItem());
            }
        });

        add(new JLabel("Choose a color:", SwingConstants.CENTER), BorderLayout.NORTH);
        add(comboBox, BorderLayout.CENTER);
        add(selectedLabel, BorderLayout.SOUTH);
        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ComboBoxExample());
    }
}
