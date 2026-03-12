
public class Reserva {
	
	private int id;
	private Client c;
	private Habitacio h;
	private int nits;
	
	public Reserva(int id, Client c, Habitacio h, int nits) {
		super();
		this.id = id;
		this.c = c;
		this.h = h;
		this.nits = nits;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public Client getC() {
		return c;
	}

	public void setC(Client c) {
		this.c = c;
	}

	public Habitacio getH() {
		return h;
	}

	public void setH(Habitacio h) {
		this.h = h;
	}

	public int getNits() {
		return nits;
	}

	public void setNits(int nits) {
		this.nits = nits;
	}
	
	

	
}
