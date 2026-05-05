package prova;

import java.awt.*;
import javax.swing.*;

public class LayoutExample extends JFrame {
    public LayoutExample() {
        setTitle("Layout Example");
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));
        setSize(500, 320);
        setLocationRelativeTo(null);

        // North: FlowLayout panel
        JPanel northPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        northPanel.setBorder(BorderFactory.createTitledBorder("FlowLayout"));
        northPanel.add(new JButton("One"));
        northPanel.add(new JButton("Two"));
        northPanel.add(new JButton("Three"));

        // Center: GridLayout panel
        JPanel centerPanel = new JPanel(new GridLayout(2, 2, 10, 10));
        centerPanel.setBorder(BorderFactory.createTitledBorder("GridLayout"));
        centerPanel.add(new JLabel("Row 1, Col 1", SwingConstants.CENTER));
        centerPanel.add(new JLabel("Row 1, Col 2", SwingConstants.CENTER));
        centerPanel.add(new JLabel("Row 2, Col 1", SwingConstants.CENTER));
        centerPanel.add(new JLabel("Row 2, Col 2", SwingConstants.CENTER));

        // South: BorderLayout panel
        JPanel southPanel = new JPanel(new BorderLayout(5, 5));
        southPanel.setBorder(BorderFactory.createTitledBorder("BorderLayout"));
        southPanel.add(new JButton("North"), BorderLayout.NORTH);
        southPanel.add(new JButton("South"), BorderLayout.SOUTH);
        southPanel.add(new JButton("East"), BorderLayout.EAST);
        southPanel.add(new JButton("West"), BorderLayout.WEST);
        southPanel.add(new JLabel("Center", SwingConstants.CENTER), BorderLayout.CENTER);

        add(northPanel, BorderLayout.NORTH);
        add(centerPanel, BorderLayout.CENTER);
        add(southPanel, BorderLayout.SOUTH);

        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new LayoutExample());
    }
}
