package lab.pkg2.poo;
import java.util.Scanner;

public class Lab2POO {
    
        public static void main(String[] args) {

        int Entrada;
        String ValorEntrada;
        Scanner keyword = new Scanner(System.in);
        
        System.out.println("Ingrese un numero del 1 al 5 para seleccionar la opcion de su entrada,siendo 1. Ñiños(<5años), 2. Niños Mayores(5 a 12 años), 3. Jovenes(13 a 17 años), 4.Adultos(18 a 65 años), 5.Adulto Mayor(>65años)");
        Entrada = keyword.nextInt();
        
        switch(Entrada){
            case 1: ValorEntrada = "0";
                        break;
            case 2: ValorEntrada = "1500";
                        break;   
            case 3: ValorEntrada = "3000";
                        break;
            case 4: ValorEntrada = "5000";
                        break;         
            case 5: ValorEntrada = "2000";
                        break;      
            default: ValorEntrada = "Valor Incorrecto";
        } 
        
        System.out.println("El Valor de la entrada es de: " + ValorEntrada);

    }
    
}
