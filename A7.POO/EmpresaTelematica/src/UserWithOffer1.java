
public class UserWithOffer1 extends UserWithOffer {
	// Constructor
	public UserWithOffer1(String dni, String nom, double priceMinute) {
		super(dni,nom,priceMinute);
	}
	
	// Bill amount (double)
	public double billAmount() {
		double total = 0;
		for (Conections c : conections) {
			if(c.nMinutes()>3) {
				total += (c.nMinutes() - 3)*priceMinute; 
			} else {
				total += 0;
			}
		
		}
		return total;
	}
} // Final
