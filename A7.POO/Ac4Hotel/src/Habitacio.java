
public class Habitacio {
	
	private int num;
	private Categoria categoria;
	private int llits;
	private boolean ocupada;

	public Habitacio(int num, Categoria c, int llits) {
		this.num = num;
		this.categoria = c;
		this.llits = llits;
		this.ocupada = false;
	}

	public int getNum() {
		return num;
	}

	public void setNum(int num) {
		this.num = num;
	}

	public Categoria getCategoria() {
		return categoria;
	}

	public void setCategoria(Categoria categoria) {
		this.categoria = categoria;
	}

	public int getLlits() {
		return llits;
	}

	public void setLlits(int llits) {
		this.llits = llits;
	}
	
	public double preuNit() {
		double preu = 0;
		switch(this.categoria) {
		case normal:
			preu =  60;
			break;
		case luxe:
			preu = 100;
			break;
		case superluxe:
			preu = 200;
			break;
		default:
			break;
			
		}
		return preu;
	}

	public boolean isOcupada() {
		return ocupada;
	}

	public void setOcupada(boolean ocupada) {
		this.ocupada = ocupada;
	}

	@Override
	public String toString() {
		return "Habitacio [num=" + num + ", categoria=" + categoria + ", llits=" + llits + ", ocupada=" + ocupada + "]";
	}
	
	
	
	
}
