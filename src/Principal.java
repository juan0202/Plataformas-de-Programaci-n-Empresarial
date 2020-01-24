
public class Principal {

	public static void main(String[] args) {
		
		
		Pacman p1 = new Pacman(1,1,"derecha");
		Laberinto l1 = new Laberinto();
		l1.LlenarLaberinto();	
		l1.MostrarLaberinto();
		
		
		
		while(true){
			
			if(StdDraw.isKeyPressed(27)) {
				System.exit(0);
			}
			
			p1.Limpiar();
			p1.cambiarDireccion();
			
			if(l1.validarPosicion(p1.getX(), p1.getY(), p1.getDirActual())) {
		
				p1.Mover();
				
			}
			
			p1.Mostrar();
			StdDraw.pause(130);
			
		}
		
	}

}
	
