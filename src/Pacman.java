

public class Pacman implements IPacman {
	
	int x,y;
    String dirActual,dirInicial;
    
    public Pacman(int x, int y,String dirInicial){
        this.x  = x;
        this.y = y;
        this.dirActual = dirInicial;
        
    }
    
    @Override
    public int getX(){
        return x;
    }
    
    @Override
    public int getY(){
        return y;
    }
    
    
    @Override
    public String getDirActual(){
        return dirActual;
        
    }
    
    public void cambiarDireccion() {
    	
    	if(StdDraw.isKeyPressed(38)){
    		this.dirActual = "arriba";
    	}
    	
    	if(StdDraw.isKeyPressed(40)){
    		this.dirActual = "abajo";
    	}
    	
    	if(StdDraw.isKeyPressed(39)){
    		this.dirActual = "derecha";
    	}
    	
    	if(StdDraw.isKeyPressed(37)){
    		this.dirActual = "izquierda";
    	}
    	
    	
    }
    
    @Override
    public void Mover(){
    	
    	if(this.x > 60){
    		this.x = 0;
    	
    	}
    	if(this.x < 0){
    		this.x = 60;
    	
    	}
    	
    	if(this.y > 60){
    		this.y = 0;
    		
    	}
    	if(this.y < 0){
    		
    		this.y = 60;
    		 
    	}
    	
    	
        
        switch(this.dirActual){
      
            
            case "derecha":
                this.y++;
                break;
		case "izquierda":
                this.y--;
                break;
            case "arriba":
                this.x--;
                break;
            case "abajo":
                this.x++;
                break;
        }
        
      
        
    }
    
    
    public void Limpiar() {
		StdDraw.setPenColor(StdDraw.WHITE);
		StdDraw.filledSquare(this.y, -this.x, 0.5);
		
		
		
	}

    @Override
    public void Mostrar(){
    	 	
    	StdDraw.setPenColor(StdDraw.BLUE);
    	StdDraw.filledCircle(this.y, -this.x, 0.5);
    	
    	
    	
        
    }

}
