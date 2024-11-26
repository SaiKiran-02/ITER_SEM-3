public class RecursiveLinearSearch {
    public static int recursiveLinearSearch(int[] arr, int target, int index) {
        // base condition
        if (index >= arr.length) {
            return -1;
        }
        // recursive state
        if (arr[index] == target) {
            return index;
        }
        return recursiveLinearSearch(arr, target, index + 1);
    }

    public static void main(String[] args) {
        int[] arr = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 23;
        
        int result = recursiveLinearSearch(arr, target, 0);

        System.out.println("the Index of " + target + " is"+ result)
    }
}