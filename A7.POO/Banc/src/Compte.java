
public class Compte {
	 
	private String numeroCompte;
	private Titular titular;
	private double saldo;
	
	public Titular getTitular() {
		return titular;
	}

	public void setTitular(Titular titular) {
		this.titular = titular;
	}

	public Compte(String numeroCompte, Titular t, double saldo) {
		this.numeroCompte = numeroCompte;
		this.titular = t;
		this.saldo = saldo;
	}
	
	public Compte(String numeroCompte, Titular t) {
		this.numeroCompte = numeroCompte;
		this.titular = t;
		this.saldo = 0;
	}

	public String getNumeroCompte() {
		return numeroCompte;
	}

	public void setNumeroCompte(String numeroCompte) {
		this.numeroCompte = numeroCompte;
	}

	public double getSaldo() {
		return saldo;
	}

	
	
	

}
