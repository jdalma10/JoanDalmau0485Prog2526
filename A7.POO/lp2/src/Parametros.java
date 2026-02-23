

/**
 * @author Pedro García 
 *
 
 */
public class Parametros {

	public static void main(String[] args) 
	{
		Cosa2 c = new Cosa2("Perro",2);
		int i = 2;
		
		System.out.println(c.getPatas()+ " "+ i);
		
		modificaValores(c,i);
		
		System.out.println(c.getPatas()+ " "+ i);
		
	}
	
	public static void modificaValores(Cosa2 cosa , int j)
	{
		cosa.setPatas(90);
		j = 90;
		
	}
	
}
