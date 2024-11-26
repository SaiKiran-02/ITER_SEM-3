package ASSIGNMENT_01;

import java.util.Scanner;


public class QUESTION_01{
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       System.out.println("Enter the number till you want to add.");
       int n = sc.nextInt();
       int sum = 0;
       for (int i = 1; i<=n; i++) {
           sum += i;
       } 

       System.out.println("sum of ");
       System.out.println(n);
       System.out.print(" natural number is : ");
       System.out.println(sum);

       sc.close();
    }
}