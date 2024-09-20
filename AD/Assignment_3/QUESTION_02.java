package Assignment_3;

import java.util.*;

public class QUESTION_02 {

    public static int array_min(int arr[], int n , int min ) {
        if(n==0){
            return min;
        }
        else{
            if(arr[n] < min){
                return array_min(arr, n-1, arr[n]);
            }
            else{
                return array_min(arr, n-1, min);
            }
        }
        
    }


    public static int array_max(int arr[], int n , int max ) {
        if(n==0){
            return max;
        }
        else{
            if(arr[n] > max){
                return array_max(arr, n-1, arr[n]);
            }
            else{
                return array_max(arr, n-1, max);
            }
        }
        
    }
   public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter maximum size of array");
    int size = sc.nextInt();
    int arr[] = new int[size];
    System.out.println("Enter the elements of Array.");
    for(int i = 0; i<arr.length; i++){
        arr[i] = sc.nextInt();
    }
    System.out.println("ARRAY: ");
    for(int i = 0; i<arr.length; i++){
         System.out.println(arr[i]);
    }
    System.out.print("max : ");
    System.out.println(array_max(arr,size-1,arr[0]));
    System.out.print("min : ");
    System.out.println(array_min(arr,size-1,arr[0]));
   }
}
