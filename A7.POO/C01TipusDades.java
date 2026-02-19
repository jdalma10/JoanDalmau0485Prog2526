import java.util.Scanner;

public class C01TipusDades {

    public static void main(String [] args){

        System.out.print("Tipus de dades: ");
        System.out.println();
        System.out.println("Tipus de dades: ");

        int num;   // Declaració
        num = 3;   // Inicialització
        int num2  = 4;
        int num3= 5, num4 = 5;

        System.out.println(num + num2);

        float f1 = 0.5f;
        double d1 = Math.PI;

        System.out.println(num + f1);

        char a = 'a';

        System.out.println(a + num);

        // error : char c = 'cc'
        // error:  char b = "b";

        int cent = 100;
        char cen = (char)cent;   // a = '3'  b = int(a) b = 3

        System.out.println(cen);

        boolean cert = true;


        Scanner input = new Scanner(System.in);
        System.out.print("Posa nom: ");
        String nom = input.nextLine();
        System.out.println(nom);

        System.out.print("Posa numero: ");
        int numero = input.nextInt();
        System.out.println(numero);


        //Condicionals

        if(num > 0){
            //
        }else if(num < 0){
            //
        }else{
            //
        }




        input.close();


    }
}
