/**
 * @author Pedro Garc�a 
 *
 */
public class Funcion
{

   public static int maximo(int a, int b) {

    if (a>b)
      return a;
    else if (a<b)
      return b;
    else
      return -1;
    
  }


  public static void saluda(){
    System.out.println("Hola");
  }

  public static String saluda2(String nom){
    return "Hola " + nom; 
  };
  public static void main(String[] args) {
    
    int x = 2;
    int y = 3;
    
    int max = maximo(x,y);
    
    System.out.println(max);  

    saluda();
    String salutacio = saluda2("Joan");
    System.out.println(salutacio);
    
  }
  
}
