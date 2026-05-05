package prova;

import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {
        try {
            ActorDAO model = new ActorDAO();
            SwingCrudView view = new SwingCrudView();
            new SwingCrudController(view, model);
        } catch (SQLException e) {
            System.err.println("Error de connexió: " + e.getMessage());
            System.exit(1);
        }
    }
}