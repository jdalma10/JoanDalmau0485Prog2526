
public class UsaInstitut {

	public static void main(String[] args) {
		
		Alumne charki = new Alumne("Charki", "3333H", "a@a.com", 20);
		Alumne charkiFals = new Alumne("Charki2", "3333H", "a@a.com", 20);

		
		System.out.println(charki);
		System.out.println(charkiFals);
		System.out.println(charki.equals(charkiFals));
		
		
		Alumne jan = new Alumne("Jan", "444H", "", 18);
		Alumne joel = new Alumne("Joal", "555H", "", 20);
		
		
		Institut jaumehuguet = new Institut("Jaume Huguet");
		Institut narcis = new Institut("Narcis Oller", 150);
		
		jaumehuguet.afegirAlumne(charki);
		jaumehuguet.afegirAlumne(charkiFals);
		narcis.afegirAlumne(jan);
		narcis.afegirAlumne(joel);
		
		System.out.println(jaumehuguet);
		System.out.println("----------");
		System.out.println(narcis);
	}

}
