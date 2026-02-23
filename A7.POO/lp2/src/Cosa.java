

/**
 * @author Pedro Garc�a 
 *
 */
public class Cosa 
{
	public int patas;
	private String nombre;



	public void setPatas(int patas)
	{
		this.patas = patas;
	}
	public int getPatas()
	{
		return this.patas;
	}
	public void setNombre(String nombre)
		{
			this.nombre = nombre;
		}
	public String getNombre()
	{
		return nombre;
	}

	public String toString(){
			return this.nombre + this.patas;
		}

	

	
}
