package Assignment_3;

import java.util.Scanner;

public class QUESTION_01 {
    public static int sum_of_n_num(int n){
        if (n == 0){
            return 0;
        }
        return n+sum_of_n_num(n-1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number till you want the sum. ");
        int n = sc.nextInt();
        System.out.println(sum_of_n_num(n));
    }
}
