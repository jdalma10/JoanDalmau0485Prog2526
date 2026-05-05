package prova;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.List;

public class SwingCrudController {
    private SwingCrudView view;
    private ActorDAO model;

    public SwingCrudController(SwingCrudView view, ActorDAO model) {
        this.view = view;
        this.model = model;

        // Add listeners
        view.getCreateBtn().addActionListener(new CreateListener());
        view.getReadBtn().addActionListener(new ReadListener());
        view.getUpdateBtn().addActionListener(new UpdateListener());
        view.getDeleteBtn().addActionListener(new DeleteListener());

        // Load initial data
        loadActors();
    }

    private void loadActors() {
        try {
            List<Actor> actors = model.readActors();
            view.getTableModel().setRowCount(0);
            for (Actor actor : actors) {
                view.getTableModel().addRow(new Object[]{actor.getActorId(), actor.getFirstName(), actor.getLastName()});
            }
        } catch (SQLException e) {
            view.showError("Error loading actors: " + e.getMessage());
        }
    }

    private class CreateListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String first = view.getFirstNameField().getText().trim();
            String last = view.getLastNameField().getText().trim();
            if (first.isEmpty() || last.isEmpty()) {
                view.showMessage("Omple tots els camps.");
                return;
            }
            try {
                Actor actor = new Actor(first, last);
                model.createActor(actor);
                view.showMessage("Actor creat.");
                loadActors();
            } catch (SQLException ex) {
                view.showError("Error: " + ex.getMessage());
            }
        }
    }

    private class ReadListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            loadActors();
        }
    }

    private class UpdateListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String idText = view.getIdField().getText().trim();
            String first = view.getFirstNameField().getText().trim();
            String last = view.getLastNameField().getText().trim();
            if (idText.isEmpty() || first.isEmpty() || last.isEmpty()) {
                view.showMessage("Omple tots els camps.");
                return;
            }
            try {
                int id = Integer.parseInt(idText);
                Actor actor = new Actor(id, first, last);
                model.updateActor(actor);
                view.showMessage("Actor actualitzat.");
                loadActors();
            } catch (NumberFormatException ex) {
                view.showError("ID no vàlid.");
            } catch (SQLException ex) {
                view.showError("Error: " + ex.getMessage());
            }
        }
    }

    private class DeleteListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String idText = view.getIdField().getText().trim();
            if (idText.isEmpty()) {
                view.showMessage("Introdueix ID.");
                return;
            }
            try {
                int id = Integer.parseInt(idText);
                model.deleteActor(id);
                view.showMessage("Actor eliminat.");
                loadActors();
            } catch (NumberFormatException ex) {
                view.showError("ID no vàlid.");
            } catch (SQLException ex) {
                view.showError("Error: " + ex.getMessage());
            }
        }
    }
}