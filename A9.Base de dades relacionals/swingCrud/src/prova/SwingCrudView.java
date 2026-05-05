package prova;

import java.awt.*;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class SwingCrudView extends JFrame {
    private JTextField firstNameField, lastNameField, idField;
    private JButton createBtn, readBtn, updateBtn, deleteBtn;
    private JTable table;
    private DefaultTableModel tableModel;

    public SwingCrudView() {
        setTitle("CRUD Actors");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Input panel
        JPanel inputPanel = new JPanel(new GridLayout(4, 2));
        inputPanel.add(new JLabel("First Name:"));
        firstNameField = new JTextField();
        inputPanel.add(firstNameField);
        inputPanel.add(new JLabel("Last Name:"));
        lastNameField = new JTextField();
        inputPanel.add(lastNameField);
        inputPanel.add(new JLabel("Actor ID (for update/delete):"));
        idField = new JTextField();
        inputPanel.add(idField);

        // Buttons
        JPanel buttonPanel = new JPanel();
        createBtn = new JButton("Create");
        buttonPanel.add(createBtn);
        readBtn = new JButton("Read");
        buttonPanel.add(readBtn);
        updateBtn = new JButton("Update");
        buttonPanel.add(updateBtn);
        deleteBtn = new JButton("Delete");
        buttonPanel.add(deleteBtn);

        // Table
        tableModel = new DefaultTableModel(new String[]{"ID", "First Name", "Last Name"}, 0);
        table = new JTable(tableModel);
        JScrollPane scrollPane = new JScrollPane(table);

        // Add to frame
        add(inputPanel, BorderLayout.NORTH);
        add(buttonPanel, BorderLayout.CENTER);
        add(scrollPane, BorderLayout.SOUTH);

        pack();
        setVisible(true);
    }

    // Getters for components
    public JTextField getFirstNameField() { return firstNameField; }
    public JTextField getLastNameField() { return lastNameField; }
    public JTextField getIdField() { return idField; }
    public JButton getCreateBtn() { return createBtn; }
    public JButton getReadBtn() { return readBtn; }
    public JButton getUpdateBtn() { return updateBtn; }
    public JButton getDeleteBtn() { return deleteBtn; }
    public JTable getTable() { return table; }
    public DefaultTableModel getTableModel() { return tableModel; }

    // Methods to show messages
    public void showMessage(String message) {
        JOptionPane.showMessageDialog(this, message);
    }

    public void showError(String message) {
        JOptionPane.showMessageDialog(this, message, "Error", JOptionPane.ERROR_MESSAGE);
    }
}