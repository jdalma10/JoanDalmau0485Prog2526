/**
 * @author Pedro García 
 *
 */
public class UsaCosa3 {

	public static void main(String[] args) 
	{
		Cosa3 perro = new Cosa3("Perro",4);
		Cosa3 pato = new Cosa3("Pato",2);
		Cosa3 hormiga = new Cosa3("Hormiga",6);
		
		Cosa3.setCuernos(7);
		System.out.println(Cosa3.getCuernos());
		
		System.out.println(perro.getPatas()+" "+ perro.getNombre()+" "+perro.getCuernos());
		System.out.println(pato.getPatas()+" "+ pato.getNombre()+" "+pato.getCuernos());		
		
		
	}
}
