import java.util.ArrayList;

public abstract class User {
	
	private String dni;
	private String name;
	protected double priceMinute;
	protected ArrayList <Conections> conections;
	
	public User(String dni, String name, double priceMinute) {
		this.dni = dni;
		this.name = name;
		this.priceMinute = priceMinute;
		this.conections = new ArrayList <>();
	}
	public abstract double billAmount();
	// Add connection
	public boolean add(Conections c) {
		if (conections.contains(c)) {
			return false;
		} else {
			conections.add(c);
			return true;
		}
	}
	@Override
	public String toString() {
		return "User [dni=" + dni + ", name=" + name + ", priceMinute=" + priceMinute + ", conections=" + billAmount() + "]";
	}
	
	
	
	

}
