
public class UserWithoutOffer extends User {

	public UserWithoutOffer(String dni, String name, double priceMinute) {
		super(dni, name, priceMinute);
		
	}
	
	// Metode obl
	public double billAmount() {
		double total = 0;
		for (Conections c : conections) {
			total += c.nMinutes()*priceMinute; 
		}
			return total;
	};
	
	
	

}
