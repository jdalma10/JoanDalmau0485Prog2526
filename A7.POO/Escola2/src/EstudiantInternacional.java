
public class EstudiantInternacional extends Estudiant {
	
	private String pais;
	
	
	public EstudiantInternacional (String nom, String adreca, String cicle, int curs, String pais) {
		super(nom, adreca, cicle, curs);
		this.pais = pais;
	}
	
	public String toString () {
		return super.toString() + " " + this.pais;
	}
	

}
