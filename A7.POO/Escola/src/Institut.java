
public class Institut {
	
	private String nom;
	private int num;
	private Alumne[] llistaAlumnes;
	
	public Institut(String nom) {
		this.nom = nom;	
		this.num = 0;
		this.llistaAlumnes = new Alumne[100];
		
	}
	
	public Institut(String nom, int max) {
		this.nom = nom;
		this.num = 0;
		this.llistaAlumnes = new Alumne[max];
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public int getNum() {
		return num;
	}

	public void setNum(int num) {
		this.num = num;
	}

	public Alumne[] getLlistaAlumnes() {
		return llistaAlumnes;
	}

	public void setLlistaAlumnes(Alumne[] llistaAlumnes) {
		this.llistaAlumnes = llistaAlumnes;
	}
	
	public String toString() {
		
		String retorn = this.nom + "\n";
		
		for (Alumne a:llistaAlumnes) {
			if(a != null) {
				retorn += a.toString()+"\n";
			}
			
		}
		
	/*	for(int i= 0; i<num;i++) {
			retorn += this.llistaAlumnes[i].toString()+"\n";
		}*/
		
		return retorn;
	}
	
	
	
	public void afegirAlumne(Alumne a) {
		
		this.llistaAlumnes[num] = a;
		num++;
		
	}
	
	

}
