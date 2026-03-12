import java.util.ArrayList;

public class Hotel {
	
	private String nom;
	private int estrelles;
	private ArrayList<Habitacio> habitacions;
	private ArrayList<Reserva> reserves;
	
	public Hotel(String nom, int estrelles) {
		super();
		this.nom = nom;
		this.estrelles = estrelles;
		this.habitacions = new ArrayList<>();
		this.reserves = new ArrayList<>();
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public int getEstrelles() {
		return estrelles;
	}

	public void setEstrelles(int estrelles) {
		this.estrelles = estrelles;
	}

	public ArrayList<Habitacio> getHabitacions() {
		return habitacions;
	}
	
	
	
	public ArrayList<Reserva> getReserves() {
		return reserves;
	}

	public void afegirHabitacio(Habitacio h) {
		this.habitacions.add(h);
	}	
	
	public void reservar(Client c, Habitacio h, int nits) {
		h.setOcupada(true);
		Reserva r = new Reserva(reserves.size()+1, c, h, nits);
		this.reserves.add(r);
	}
	
	public String disponibles() {
		String s="";
		for(Habitacio h:habitacions) {
			if(!h.isOcupada()) {      // if (h.isOcupada() == false){  }
				s+=h.toString()+ "\n";
			}
		}
		return s;
	}
	
	public double calcularFactura(String nom) {
		
		for (Reserva r: reserves) {
			
			if(r.getC().getNom().equals(nom)) {
				return r.getH().preuNit() * r.getNits();
			}	
		}
		return 0;
	}
	
	
	

}
