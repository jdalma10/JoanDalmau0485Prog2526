
public class Client {
	
	private String nom, dni, targeta;

	public Client(String nom, String dni, String targeta) {
		super();
		this.nom = nom;
		this.dni = dni;
		this.targeta = targeta;
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getDni() {
		return dni;
	}

	public void setDni(String dni) {
		this.dni = dni;
	}

	public String getTargeta() {
		return targeta;
	}

	public void setTargeta(String targeta) {
		this.targeta = targeta;
	}
	
	

}
