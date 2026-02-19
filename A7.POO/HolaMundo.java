public class HolaMundo {

    public static void main (String [] args) {
        //Programa de prova
        int edat = 25;
        int edat2 = 25;

        boolean permis = true;

        if(permis == true){
            System.out.println("Tens permís");
        }
        else if(!permis){   // else if (permis != true)
            System.out.println("No tens permís");
        }
        else{
            System.out.println("No ho se");
        }

        //for i in range(3):   - 0 1 2
        //for i in range(1,3):  - 1,2
        //for i in range(1,4,2): - 1,3
        System.out.print("For: ");
        for(int i=0;i<3;i++){  // 0 1 2
            System.out.println(i);
        }
        int j = 0;
        System.out.print("While: ");
        while(j < 3){
            System.out.println(j);
            j++;
        }

        System.out.print("Do ... while: ");
        int z = 100;
        do{
            System.out.println(z);
            z++;
        }while(z<10);


        System.out.println(edat + edat2);
        System.out.println("Hola mundo: " + edat);
    }
}
