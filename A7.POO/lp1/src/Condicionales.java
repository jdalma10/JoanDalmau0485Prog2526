/**
 * @author Pedro García 
 *
 */
public class Condicionales
{

  public static void main(String[] args) {
    
    int a=4;
    
    switch (a) {
      case 0: System.out.println(0); break;
      case 1: System.out.println(1); break;
      default: System.out.println(2); break;
    }
    
    if (a==0) {
      System.out.println(0);
    } else if (a==1) {
      System.out.println(1);
    } else {
      System.out.println(2);
    }
    
    if (a>=0 && a<5)
      System.out.println("Entre 0 y 5");
    
  }
}
