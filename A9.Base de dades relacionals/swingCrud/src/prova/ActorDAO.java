package prova;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ActorDAO {
    private static final String URL = "jdbc:mysql://127.0.0.1:3306/sakila";
    private static final String USER = "root";
    private static final String PWD = "";
    private Connection conn;

    public ActorDAO() throws SQLException {
        conn = DriverManager.getConnection(URL, USER, PWD);
    }

    public void createActor(Actor actor) throws SQLException {
        String sql = "INSERT INTO actor (first_name, last_name) VALUES (?, ?)";
        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, actor.getFirstName());
            ps.setString(2, actor.getLastName());
            ps.executeUpdate();
        }
    }

    public List<Actor> readActors() throws SQLException {
        List<Actor> actors = new ArrayList<>();
        String sql = "SELECT actor_id, first_name, last_name FROM actor ORDER BY actor_id";
        try (Statement st = conn.createStatement();
             ResultSet rs = st.executeQuery(sql)) {
            while (rs.next()) {
                int id = rs.getInt("actor_id");
                String first = rs.getString("first_name");
                String last = rs.getString("last_name");
                actors.add(new Actor(id, first, last));
            }
        }
        return actors;
    }

    public void updateActor(Actor actor) throws SQLException {
        String sql = "UPDATE actor SET first_name = ?, last_name = ? WHERE actor_id = ?";
        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, actor.getFirstName());
            ps.setString(2, actor.getLastName());
            ps.setInt(3, actor.getActorId());
            ps.executeUpdate();
        }
    }

    public void deleteActor(int id) throws SQLException {
        String sql = "DELETE FROM actor WHERE actor_id = ?";
        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            ps.executeUpdate();
        }
    }

    public void close() throws SQLException {
        if (conn != null) conn.close();
    }
}