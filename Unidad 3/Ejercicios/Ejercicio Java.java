import java.util.Scanner;

public class CalculadoraBasica {
    public static void main(String[] args) {
        try ( 
                Scanner scanner = new Scanner(System.in)) {
            System.out.print("Ingresa el primer número: ");
            double numero1 = scanner.nextDouble();
            System.out.print("Ingresa el segundo número: ");
            double numero2 = scanner.nextDouble();
            System.out.println("Selecciona una operación:");
            System.out.println("1. Suma");
            System.out.println("2. Resta");
            System.out.println("3. Multiplicación");
            System.out.println("4. División");
            System.out.print("Ingresa el número de la operación: ");
            int opcion = scanner.nextInt();
            double resultado;
            switch (opcion) {
                case 1 -> {
                    // Suma
                    resultado = numero1 + numero2;
                    System.out.println("El resultado de la suma es: " + resultado);
                }
                case 2 -> {
                    // Resta
                    resultado = numero1 - numero2;
                    System.out.println("El resultado de la resta es: " + resultado);
                }
                case 3 -> {
                    // Multiplicación
                    resultado = numero1 * numero2;
                    System.out.println("El resultado de la multiplicación es: " + resultado);
                }
                case 4 -> {
                    // División
                    if (numero2 != 0) {
                        resultado = numero1 / numero2;
                        System.out.println("El resultado de la división es: " + resultado);
                    } else {
                        System.out.println("Error: No se puede dividir entre cero.");
                    }
                }
                default -> System.out.println("Opción inválida. Por favor selecciona una operación válida.");
            }
        }
    }
}
