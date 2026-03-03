
public class Concessionari {
	
	private Cotxe[] llista;
	private int contador;
	
	public Concessionari() {
		this.llista =  new Cotxe[5];
		this.contador = 0;
	}
	
	public void nouCotxe(Cotxe c) {
		
		this.llista[contador] = c;
		this.contador++;
		
	}
	
	public Cotxe buscaCotxe(String bas) {
		
		for(int i = 0; i< contador; i++) {
			if(llista[i].getBastidor().equals(bas)) {
				return llista[i];
			}
		}
		return null;
	}
	
	
	
	
	public String toString() {
		String resultat = "Cotxes en concessionari: \n";
		for(int i = 0; i< contador; i++) {
			resultat+= llista[i] + "\n";
		}
		
		
		
		return resultat;
	}
	
	


}
