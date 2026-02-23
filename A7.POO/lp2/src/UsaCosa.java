
/**
 * @author Pedro Garc�a 
 *
 */
public class UsaCosa {

	
	public static void main(String[] args) {
		
		Cosa c = new Cosa();
		
		c.patas = 2;  // Mala praxis
		c.setPatas(2);
		c.setNombre("bicho");


		

		int patas = c.getPatas();
		System.out.println(c.getPatas()+" "+ c.getNombre());
		c.setPatas(55);
		System.out.println(c.getPatas()+" "+ c.getNombre());

		Cosa c2 = new Cosa();
		c2.setNombre("Pokembo");
		c2.setPatas(8);
		
		System.out.println(c2);
	}
}
