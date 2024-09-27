import java.util.*;

public class QUESTION_04 {

    public static int fab (int i, int n, int sum){
        if (i == n){
            return sum;
        }
        else{
            return fab(i+1,n,sum+i);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number for which you want to find nth fabonacci number: ");
        int n = sc.nextInt();
        System.out.print("nth fabonacci num of "+n+" is ");
        System.out.println(fab(n));
    }
}
