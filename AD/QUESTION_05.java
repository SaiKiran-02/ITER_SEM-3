import java.util.*;

public class QUESTION_05 {

    public static int pow(int a, int n,int p){
        if(n == 0 || a==1){
            return 1;
        }
        else if(n == 1){
            return a;
        }
        else{
            return a*pow(a, n-1);
        }

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number for which you want to find power: ");
        int n = sc.nextInt();
        System.out.println("Enter the base: ");
        int a = sc.nextInt();
        System.out.print("power of "+a+" to the pow "+n+" is ");
        System.out.println(pow(a,n,1));
    }
}
