import java.util.ArrayList;

public class Company {
	
	private ArrayList <User> users ;
	
	public Company() {
		this.users = new ArrayList <>();
	};
	
	public boolean add(User u) {
		if(users.add(u)) {
			return true;
		}else {
			return false;
		}
		
	};
	
	public void listusers() {
		for (User u: users) {
			System.out.println (u);
		}
		
		
	}


	
	

}




