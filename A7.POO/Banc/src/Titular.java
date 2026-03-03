
public class Titular {
	private String dni;
	private String nombre;
	private String cognom;
	
	public Titular(String dni, String nombre, String cognom) {
		this.dni = dni;
		this.nombre = nombre;
		this.cognom = cognom;
	}

	public String getDni() {
		return dni;
	}

	public void setDni(String dni) {
		this.dni = dni;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCognom() {
		return cognom;
	}

	public void setCognom(String cognom) {
		this.cognom = cognom;
	}
	
	
	
}
