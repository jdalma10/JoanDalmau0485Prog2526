/**
 * @author Pedro García 
 *
 */
public class Basicos
{

  public static void main(String[] args) {
    
    int a, b;
    double c, d;
    char e, f;
    boolean g, h;
    
    b = 3;
    a = b+1;
    System.out.println(a);    
    
    c = 2.0 * 3.756;
    System.out.println(c);
    
    d = c++;
    System.out.println(d);
    
    e = 'a';
    System.out.println(e);
    
    g = true;
    h = g && false;
    
    System.out.println(h);
    h = g || false;
    
    System.out.println(h);
    
  }
}
