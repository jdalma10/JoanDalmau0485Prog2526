import java.util.HashSet;

public class Professor extends Persona {
	
	private HashSet<String> assignatures;

	public Professor(String nom, String adreca) {
		super(nom, adreca);
		this.assignatures = new HashSet<>();
	}
	
	public boolean afegeixAssignatura(String assig) {
		try {
			if(!assignatures.add(assig)) {
				throw new Exception("Assignatura repetida.");
			}
		}catch(Exception e){
			return false;
		}
		return true;
	}
	
	public boolean treureAssignatura(String assig) {
		try {
			
			if(!assignatures.remove(assig)) {
				throw new Exception("Assignatura inexistent.");
			}
			
		}catch(Exception e){
			return false;
		}
		return true;
	}
	
	
	public String toString() {
		String ret = super.toString() + " ";
		for(String a:assignatures) {
			ret += a +"-";
			
		}
		return ret;
	}
	
	public void saluda() {
		System.out.println("Hola soc un Professor");
	}

}
