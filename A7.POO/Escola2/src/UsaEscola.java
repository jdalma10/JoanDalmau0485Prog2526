
public class UsaEscola {

	public static void main(String[] args) {
		
		Persona p = new Persona("Joan", null);
		Estudiant e = new Estudiant("Manel", null, "DAM", 1);
		
		System.out.println(p);
		System.out.println(e);
		
		Professor f = new Professor("Francesc", null);
		
		f.afegeixAssignatura("0483");
		f.afegeixAssignatura("1111");
		f.afegeixAssignatura("1111");
		f.treureAssignatura("1111");
		
		System.out.println(f);
		
		EstudiantInternacional ei = new EstudiantInternacional( "Utter", "", "DAM", 1, "Germany");
		
		System.out.println(ei);
		
		

	}

}
