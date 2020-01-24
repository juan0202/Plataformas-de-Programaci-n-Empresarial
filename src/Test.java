
public class Test {

	public static void main(String[] args) {
		
		Laberinto l2 = new Laberinto();
		Pacman p2 = new Pacman(1,1,"derecha");
		l2.LlenarLaberinto();
		p2.Mover();
		p2.Mover();
		assert(p2.getX() == 1 && p2.getY() == 3);
		assert(l2.label[p2.getX()][p2.getY()].equals("X"));
		assert(p2.getDirActual() == "derecha");
		Pacman p3 = new Pacman(1,2,"izquierda");
		assert(p3.getDirActual() == "izquierda");
		p2.Mover();
		assert(p2.getX() == 1 && p2.getY() == 4);
		assert(l2.label[p2.getX()][p2.getY()].equals(" "));
		assert(l2.validarPosicion(p2.getX(), p2.getY(), "derecha") == true);

	}

}
