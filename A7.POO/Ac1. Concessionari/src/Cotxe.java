
public class Cotxe {

	private String marca, model, bastidor;
	
	public Cotxe(String bastidor) {
		
		this.bastidor = bastidor;
		
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public String getBastidor() {
		return bastidor;
	}
	
	public String toString() {
		return this.marca +" "+ this.model +" "+ this.bastidor;
	}
	
}
