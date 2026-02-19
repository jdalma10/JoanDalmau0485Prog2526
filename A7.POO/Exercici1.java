import java.util.Scanner;

public class Exercici1 {

    public static void main (String[] args){
        // text = input("posa un text: )

        String text = "";
        Scanner teclado = new Scanner(System.in);
        System.out.print("Escriu un nom: ");
        text = teclado.nextLine();

        System.out.println("Hola, " + text);
    }
}
