// You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

// Find two lines that together with the x-axis form a container, such that the container contains the most water.

// Return the maximum amount of water a container can store.

// Notice that you may not slant the container.

class P11_ContainerWithMostWater {
    public int maxArea(int[] height) {
        int maximum = 0;                         // set the maxinum capacity in a variable
        int i = 0;
        int j = height.length - 1;               // set indices of beginning and end pointer

        while (i != j) {                         // while loop to determine maximum capacities
            if (height[i] < height[j]) {         // ith line is the length of rectangle
                if (height[i] * (j - i) > maximum) {        // replace maximum
                    maximum = height[i] * (j - i);
                }
                i++;                             // move i since it's the smaller pillar
            }
            else {                               // jth line is length of rectangle
                if (height[j] * (j - i) > maximum) {        // replace maximum
                    maximum = height[j] * (j - i);
                }
                j--;                             // move j since it's the smaller pillar
            }
        }
        return maximum;
    }
}
