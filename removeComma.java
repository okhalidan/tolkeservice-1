// Made by Trolle & Khalle 2014
import java.util.Scanner;

public class removeComma {

	public static void main(String[] args) {
		// Spørger brugeren om at indtaste en værdi.
		System.out.print("Please enter an integer between 1,000 and 999,999:");
		// Registrer hvad der bliver tastet på keyboard.
		Scanner in = new Scanner(System.in);
		// læser værdien og gemmer den som en streng
		String inputNumber = in.nextLine();
		// giver længden af værdien som er indtastet.
		int lengthNumber = inputNumber.length();
		// 
		String outputNumber = inputNumber.substring(0, lengthNumber-4) +
				inputNumber.substring(lengthNumber-3);
		// udskriver med ny linje den nye værdi uden kommaer.
		System.out.println(outputNumber);
	}
}
