package prova;

import java.sql.*;
import java.util.Scanner;

public class pInsercio {
    private static final String URL = "jdbc:mysql://127.0.0.1:3306/sakila";
    private static final String USER = "root";
    private static final String PWD = "";

    public static void main(String[] args) {
        try (Connection connexio = DriverManager.getConnection(URL, USER, PWD);
             Scanner scanner = new Scanner(System.in)) {

            System.out.println("Connexió creada correctament.");

            boolean sortir = false;
            while (!sortir) {
                mostrarMenu();
                System.out.print("Opció: ");
                String opcio = scanner.nextLine().trim();

                switch (opcio) {
                    case "1":
                        crearActor(connexio, scanner);
                        break;
                    case "2":
                        llegirActors(connexio);
                        break;
                    case "3":
                        actualitzarActor(connexio, scanner);
                        break;
                    case "4":
                        eliminarActor(connexio, scanner);
                        break;
                    case "5":
                        sortir = true;
                        break;
                    default:
                        System.out.println("Opció no vàlida. Tria 1-5.");
                }

                System.out.println();
            }

            System.out.println("Finalitzant programa.");

        } catch (SQLException e) {
            System.out.println("Error de connexió: " + e.getMessage());
        }
    }

    private static void mostrarMenu() {
        System.out.println("--- Menú CRUD d'actors ---");
        System.out.println("1. Crear actor");
        System.out.println("2. Llistar actors");
        System.out.println("3. Actualitzar actor");
        System.out.println("4. Eliminar actor");
        System.out.println("5. Sortir");
    }

    private static void crearActor(Connection connexio, Scanner scanner) {
        String firstName = llegirText(scanner, "Nom: ");
        String lastName = llegirText(scanner, "Cognom: ");

        String sql = "INSERT INTO actor (first_name, last_name) VALUES (?, ?)";
        try (PreparedStatement ps = connexio.prepareStatement(sql)) {
            ps.setString(1, firstName);
            ps.setString(2, lastName);
            int files = ps.executeUpdate();
            System.out.println("Registres inserits: " + files);
        } catch (SQLException e) {
            System.out.println("Error en la creació: " + e.getMessage());
        }
    }

    private static void llegirActors(Connection connexio) {
        String sql = "SELECT actor_id, first_name, last_name FROM actor ORDER BY actor_id";
        try (Statement st = connexio.createStatement();
             ResultSet rs = st.executeQuery(sql)) {
            System.out.println("actor_id | first_name | last_name");
            while (rs.next()) {
                int id = rs.getInt("actor_id");
                String firstName = rs.getString("first_name");
                String lastName = rs.getString("last_name");
                System.out.printf("%d | %s | %s%n", id, firstName, lastName);
            }
        } catch (SQLException e) {
            System.out.println("Error en la lectura: " + e.getMessage());
        }
    }

    private static void actualitzarActor(Connection connexio, Scanner scanner) {
        int id = llegirEnter(scanner, "actor_id de l'actor a actualitzar: ");
        String firstName = llegirText(scanner, "Nou nom: ");
        String lastName = llegirText(scanner, "Nou cognom: ");

        String sql = "UPDATE actor SET first_name = ?, last_name = ? WHERE actor_id = ?";
        try (PreparedStatement ps = connexio.prepareStatement(sql)) {
            ps.setString(1, firstName);
            ps.setString(2, lastName);
            ps.setInt(3, id);
            int files = ps.executeUpdate();
            if (files > 0) {
                System.out.println("Actor actualitzat correctament.");
            } else {
                System.out.println("No s'ha trobat cap actor amb actor_id=" + id + ".");
            }
        } catch (SQLException e) {
            System.out.println("Error en l'actualització: " + e.getMessage());
        }
    }

    private static void eliminarActor(Connection connexio, Scanner scanner) {
        int id = llegirEnter(scanner, "actor_id de l'actor a eliminar: ");
        String sql = "DELETE FROM actor WHERE actor_id = ?";
        try (PreparedStatement ps = connexio.prepareStatement(sql)) {
            ps.setInt(1, id);
            int files = ps.executeUpdate();
            if (files > 0) {
                System.out.println("Actor eliminat correctament.");
            } else {
                System.out.println("No s'ha trobat cap actor amb actor_id=" + id + ".");
            }
        } catch (SQLException e) {
            System.out.println("Error en l'eliminació: " + e.getMessage());
        }
    }

    private static String llegirText(Scanner scanner, String prompt) {
        System.out.print(prompt);
        return scanner.nextLine().trim();
    }

    private static int llegirEnter(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
            String línia = scanner.nextLine().trim();
            try {
                return Integer.parseInt(línia);
            } catch (NumberFormatException e) {
                System.out.println("Introdueix un nombre enter vàlid.");
            }
        }
    }
}