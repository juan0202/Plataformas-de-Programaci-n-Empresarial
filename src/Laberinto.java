
public class Laberinto implements ILaberinto {
	
	String[][] label;
	String[] temp;
	int cant_col,cant_fil;
	
	public Laberinto() {
		
		temp = new In("C:\\Users\\ASUS\\Desktop\\laberinto.txt").readAllLines();
		
		
	}
	
	public void LlenarLaberinto() {
		
		String[] temp2 = new String[temp[0].split(",").length];
		label = new String[temp.length][temp2.length];
		cant_fil = temp.length;
		cant_col = temp2.length;
		
		
		for(int i = 0; i < temp2.length;i++) {
			for(int j = 0; j < temp.length;j++) {
				temp2 = temp[j].split(",");
				label[j][i] = temp2[i];
				
				
			}
		
		}
		
	}
	
	public int getCol() {
		
		return cant_col;
	}
	
	public int getFilas() {
		
		return cant_fil;
	}
	
	public void MostrarLaberinto() {
		StdDraw.setPenColor(StdDraw.BLACK);
		StdDraw.setXscale(-1,this.getCol());
		StdDraw.setYscale(-this.getFilas(), 1);
		
		for(int i = 0; i < this.getCol(); i++) {
			for(int j = 0; j < this.getFilas();j++) {
				
				if(label[j][i].equals("X")) {
					StdDraw.filledSquare(i, -j, 0.5
							);
				}
				
			}
			
		}
		
		
	}
	
	
	
	public void ImprimirLaberinto() {
		
		for(int i = 0; i < temp.length; i++) {
			for(int j = 0; j < temp[0].split(",").length;j++) {
				
				StdOut.println("|" + label[i][j]);
			}
			StdOut.print();
		}
		
	}
	
	public boolean validarPosicion(int x, int y,String direccion) {
		
		switch(direccion) {
		case "derecha":
			if(y < cant_col) {
				if(label[x][y+1].equals(" ")) {
					return true;
				}
			}
			
		
		
			break;
		case "izquierda":
			if(y > 0) {
				if(label[x][y-1].equals(" ")) {
					return true;
				}
				
			}
				
			
			
			break;
			
		case "arriba":
			if(x > 0) {
				if(label[x-1][y].equals(" ")) {
					return true;
				}
				
			}
				
			
			
			break;
			
		case "abajo":
			if(x < cant_fil - 1) {
				if(label[x+1][y].equals(" ")) {
					return true;
				}
				
			}
				
			break;
		}
		
		return false;
		
	}
	
	
	

	

}
