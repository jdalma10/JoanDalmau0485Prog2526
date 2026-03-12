
public class UsaEscola {

	public static void main(String[] args) {
		
	
		
		
		Estudiant e = new Estudiant("Manel", null, "DAM", 1);
		e.saluda();
		

		
		Professor f = new Professor("Francesc", null);
		f.saluda();
		
		f.afegeixAssignatura("0483");
		f.afegeixAssignatura("1111");
		f.afegeixAssignatura("1111");
		f.treureAssignatura("1111");
		

		EstudiantInternacional ei = new EstudiantInternacional( "Utter", "", "DAM", 1, "Germany");
		

		
		
		Escola jh = new Escola();
		jh.persones.add(e);
		jh.persones.add(f);
		jh.persones.add(ei);

		for(Persona p : jh.persones) {
			System.out.println(p);
			
		}

	}

}
