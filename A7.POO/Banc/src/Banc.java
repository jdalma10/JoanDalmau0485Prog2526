
public class Banc {
	private int contador;
	private Compte[] llista; 
	private String nom_banc;

	public Banc(String nom_banc) {
		this.contador = 0;
		this.nom_banc = nom_banc;
		this.llista = new Compte[5];
	}

	public String getNom_banc() {
		return nom_banc;
	}

	public void setNom_banc(String nom_banc) {
		this.nom_banc = nom_banc;
	}
	public void nouCompte(Compte c01) {
		 llista[contador]=c01;
		 contador++;
		 
	}
	public String toString() {
		String retorno =  "Nom: "+this.nom_banc;
		retorno = retorno + "\n";
		
		for(Compte x:llista) {   // for x in llista:   // for(int i= 0; i<contador; i ++){}  - for i in range(contador):)
			if(x!=null) {
				retorno = retorno + "Compte: "+ x.getNumeroCompte() + " Saldo: " + x.getSaldo()+"\n";
				Titular t = x.getTitular();
				retorno = retorno + "DNI: " + t.getDni()+ "Nombre: "+ t.getNombre()+" "+t.getCognom() +"\n";
			}
			retorno = retorno + "\n";	  	
		}
		return retorno;
	}
	


}