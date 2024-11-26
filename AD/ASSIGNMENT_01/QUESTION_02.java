package ASSIGNMENT_01;

import java.util.*;

public class QUESTION_02{
    public static int arr_min(int arr[]) {
        int min = arr[0];
        for(int i = 1; i < arr.length; i++){
            if (arr[i] < min){
                min = arr[i];
            }
        }
        return min;
    }

    public static int arr_max(int arr[]) {
        int max = arr[0];
        for(int i = 1; i<arr.length; i++){
            if (arr[i] > max){
                max = arr[i];
            }
        }

        return max;
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

        System.out.print("MIN: ");
        System.out.println(arr_min(arr));
        System.out.print("MAX: ");
        System.out.println(arr_max(arr));
    }

}
