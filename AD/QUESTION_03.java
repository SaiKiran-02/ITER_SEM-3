import java.util.*;

public class QUESTION_03 {

    public static int fact(int n){
        if (n == 0 || n ==1){
            return 1;
        }
        else{
            return n*fact(n-1);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number for which you want to find factorial: ");
        int n = sc.nextInt();
        System.out.print("factorial of "+n+" is ");
        System.out.println(fact(n));
    }
}
