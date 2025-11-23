/*
given an array for each subarray of a specified length, find the smallest element in the subarray, among all these smallest elements, determine the largest one.
the subarray are formed by taking consecutives elements starting from each position in the array with each subarray having the specified length.
The last valid subarray ends exactly at the last element of the array

Example: 

n = 5, the number of elements
arr=[1,2,3,4,5]
k = 2

For subarray size k= 2 the subarrays are [1,2], [2,3],[3,4] and [4,5] and the minima are [1,2,3,4] the final answer is 4, the maximun of these


*/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.List;

public class sliding_windows_maxmin {

    public static void main(String[] args) {

        //List<Integer> arr= List.of(1,2,3,4,5);
        //int k=2;
        List<Integer> arr= List.of(1,3,-1,-3,5,3,6,7);
        int k=3;
        System.out.println(maxMin(arr,k));
    }

    public static int maxMin_1(List<Integer> arr, int k) {
        int maxOfMins = Integer.MIN_VALUE;

        for (int i = 0; i <= arr.size() - k; i++) {
            int currentMin = Integer.MAX_VALUE;

            for (int j = i; j < i + k; j++) {
                if (arr.get(j) < currentMin) {
                    currentMin = arr.get(j);
                }
            }
            if (currentMin > maxOfMins) {
                maxOfMins = currentMin;
            }
        }
        return maxOfMins;
    }



    public static int maxMin_2(List<Integer> arr, int k) {
        
        if (arr == null || arr.isEmpty() || k <= 0 || k > arr.size()) {           
            throw new IllegalArgumentException("Invalid inputs");
        }
        int maxOfMins = Integer.MIN_VALUE;
        for (int i = 0; i <= arr.size() - k; i++) {
            List<Integer> currentSubarray = arr.subList(i, i + k);
            int minInSubarray = Collections.min(currentSubarray);

            if (minInSubarray > maxOfMins) {
                maxOfMins = minInSubarray;
            }
        }
        return maxOfMins;
    }

 public static int maxMin(List<Integer> arr, int k) {
        if (arr == null || arr.isEmpty() || k <= 0 || k > arr.size()) {
            throw new IllegalArgumentException("Invalid inputs");
        }
        
        int n = arr.size();        
        Deque<Integer> dq = new ArrayDeque<>();
        List<Integer> minimumsList = new ArrayList<>();

        for (int i = 0; i < n; i++) {

            while (!dq.isEmpty() && arr.get(dq.peekLast()) >= arr.get(i)) {
                dq.removeLast();
            }
            dq.addLast(i);
            while (!dq.isEmpty() && dq.peekFirst() <= i - k) {
                dq.removeFirst();
            }
            if (i >= k - 1) {
                minimumsList.add(arr.get(dq.peekFirst()));
            }
        }
        return Collections.max(minimumsList);
    }


}


