import java.awt.Point;

/**
 * @author Pedro García 
 *
 */
public class Cloning {

	public static void main(String[] args) 
	{
		Point p = new Point (1,1);
		Point p2 = p;
		
		p2.setLocation(120,120);
		//Aliasing
		System.out.println("Valor de p:" + p.getX());
		System.out.println("Valor de p2:" + p2.getX());
		
		Point p3 = (Point)p.clone();
		p3.setLocation(40,40);
		System.out.println("Valor de p:" + p.getX());
		System.out.println("Valor de p3:" + p3.getX());

			
		
	}
}
