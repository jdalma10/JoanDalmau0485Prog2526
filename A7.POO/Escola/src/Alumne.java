
public class Alumne {

	private String nom, dni, email;
	private int edat;
	
	
	public Alumne(String nom, String dni, String email, int edat) {
		this.nom = nom;
		this.dni = dni;
		this.email = email;
		this.edat = edat;
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


	public String getEmail() {
		return email;
	}


	public void setEmail(String email) {
		this.email = email;
	}


	public int getEdat() {
		return edat;
	}


	public void setEdat(int edat) {
		this.edat = edat;
	}
	
	public String toString() {
		return this.nom + "-" + this.dni;
	}



	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Alumne other = (Alumne) obj;
		if (nom == null) {
			if (other.nom != null)
				return false;
		} else if (!nom.equals(other.nom))
			return false;
		return true;
	}
	
	
	
	
	
	
	
	
	
	
	
	
}
