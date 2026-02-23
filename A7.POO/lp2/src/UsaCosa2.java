
/**
 * @author Pedro Garc�a 
 *

 */
public class UsaCosa2 {

	public static void main(String[] args) {
		
		Cosa2 therian = new Cosa2();
		Cosa2 perro = new Cosa2("Perro",4);
		Cosa2 pato = new Cosa2("Pato",2);
		Cosa2 hormiga = new Cosa2("Hormiga",6);
		
		System.out.println(perro.getPatas()+" "+ perro.getNombre());
		System.out.println(pato.getPatas()+" "+ pato.getNombre());		
		
		Cosa2 lista [] = new Cosa2[3];
		lista[0] = perro;
		lista[1] = pato;
		lista[2] = hormiga;
		
		for (int i=0;i<lista.length;i++)
			System.out.println(lista[i].getNombre());
		
		
		
		
		
	}


	
}
