import lp.*;

/**
 * @author Pedro García 
 *
 */
public class UsaCosa4 {

	public static void main(String[] args)
	{
		Cosa4 perro = new Cosa4("Perro",4);
		Cosa4 pato = new Cosa4("Pato",2);
		Cosa4 hormiga = new Cosa4("Hormiga",6);
		
		System.out.println(perro.getPatas()+" "+ perro.getNombre());
		System.out.println(pato.getPatas()+" "+ pato.getNombre());		
		
		Cosa4 lista [] = new Cosa4[3];
		lista[0] = perro;
		lista[1] = pato;
		lista[2] = hormiga;
		
		for (int i=0;i<lista.length;i++)
			System.out.println(lista[i].getNombre());
	}
}
