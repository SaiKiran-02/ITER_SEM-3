public class LinearSearch {
    public static int linearSearch(int[] arr, int target) {
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 23;
        
        int result = linearSearch(arr, target);
        System.out.println("Element " + target + " is at index: " + result);
    }
}