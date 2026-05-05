package prova;

import java.awt.*;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import javax.swing.*;

public class CheckBoxExample extends JFrame {
    private JLabel messageLabel;

    public CheckBoxExample() {
        setTitle("CheckBox Example");
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(new GridLayout(0, 1, 10, 10));
        setSize(340, 200);
        setLocationRelativeTo(null);

        JCheckBox option1 = new JCheckBox("Option 1");
        JCheckBox option2 = new JCheckBox("Option 2");
        JCheckBox option3 = new JCheckBox("Option 3");
        messageLabel = new JLabel("Select options to see status.", SwingConstants.CENTER);

        ItemListener listener = new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                updateMessage(option1.isSelected(), option2.isSelected(), option3.isSelected());
            }
        };

        option1.addItemListener(listener);
        option2.addItemListener(listener);
        option3.addItemListener(listener);

        add(option1);
        add(option2);
        add(option3);
        add(messageLabel);
        setVisible(true);
    }

    private void updateMessage(boolean a, boolean b, boolean c) {
        messageLabel.setText("Selected: " +
                (a ? "1 " : "") +
                (b ? "2 " : "") +
                (c ? "3" : ""));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new CheckBoxExample());
    }
}
