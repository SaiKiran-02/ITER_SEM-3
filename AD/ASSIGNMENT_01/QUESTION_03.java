package ASSIGNMENT_01;
public class QUESTION_03 {
    public static int[] rotateArray(int arr[],int k){
        if (k<=arr.length){
            for(int i = 0; i<=(k-1)/2; i++){
                int temp = arr[i];
                arr[i] = arr[k-i];
                arr[k-i] = temp;
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        int arr[] = {2,3,4,5,7,2,56,65};
        int k = 5;
        System.out.println(rotateArray(arr, k));
    }
}
