package prova;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class RadioButtonExample extends JFrame {
    public RadioButtonExample() {
        setTitle("RadioButton Example");
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));
        setSize(360, 180);
        setLocationRelativeTo(null);

        JPanel panel = new JPanel(new GridLayout(0, 1));
        JRadioButton optionA = new JRadioButton("Option A");
        JRadioButton optionB = new JRadioButton("Option B");
        JRadioButton optionC = new JRadioButton("Option C");
        ButtonGroup group = new ButtonGroup();
        group.add(optionA);
        group.add(optionB);
        group.add(optionC);
        optionA.setSelected(true);

        JLabel selectedLabel = new JLabel("Selected: Option A", SwingConstants.CENTER);

        ActionListener listener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                selectedLabel.setText("Selected: " + e.getActionCommand());
            }
        };

        optionA.setActionCommand("Option A");
        optionB.setActionCommand("Option B");
        optionC.setActionCommand("Option C");
        optionA.addActionListener(listener);
        optionB.addActionListener(listener);
        optionC.addActionListener(listener);

        panel.add(optionA);
        panel.add(optionB);
        panel.add(optionC);

        add(new JLabel("Pick one option:", SwingConstants.CENTER), BorderLayout.NORTH);
        add(panel, BorderLayout.CENTER);
        add(selectedLabel, BorderLayout.SOUTH);
        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new RadioButtonExample());
    }
}
