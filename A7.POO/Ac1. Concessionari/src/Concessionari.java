import java.util.ArrayList;

public class Concessionari {
	
	//private Cotxe[] llista;
	private ArrayList<Cotxe> llista; 
	//private int contador;
	
	public Concessionari() {
		this.llista = new ArrayList<>();
		//this.contador = 0;
	}
	
	public void nouCotxe(Cotxe c) {
		
		llista.add(c);
		
		//this.llista[contador] = c;
		//this.contador++;
		
	}
	
	public Cotxe buscaCotxe(String bas) {
		
		for(Cotxe c:llista) {
			if(c.getBastidor().equals(bas)) {
				return c;
			}
		}
		return null;
		
		/*
		 * for(int i = 0; i< contador; i++) { if(llista[i].getBastidor().equals(bas)) {
		 * return llista[i]; } } return null;
		 */
	}
	
	
	
	
	public String toString() {
		String resultat = "Cotxes en concessionari: \n";
		for(int i = 0; i< llista.size(); i++) {
			resultat+= llista.get(i) + "\n";
		}
		
		
		
		return resultat;
	}
	
	


}
