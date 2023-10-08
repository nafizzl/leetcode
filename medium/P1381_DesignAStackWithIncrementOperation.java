// Design a stack that supports increment operations on its elements.

// Implement the CustomStack class:

// CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
// void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
// int pop() Pops and returns the top of the stack or -1 if the stack is empty.
// void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
 

class P1381_DesignAStackWithIncrementOperation {
    private ArrayList<Integer> stack;
    private int capacity;
    private int top;                    // ArrayList for stack with int data holders for capacity and index for top of stack

    public CustomStack(int maxSize) {
        stack = new ArrayList();
        capacity = maxSize;
        top = -1;                       // just set the values of variables and initialize arraylist
    }
    
    public void push(int x) {
        if (stack.size() == capacity) {
            return;                     // don' add anything if full
        }
        else {
            top++;
            stack.add(top, x);          // change top index and add
        }
    }
    
    public int pop() {
        if (stack.size() == 0) {
            return -1;                  // return if empty
        }
        else {
            int retVal = stack.get(top);
            stack.remove(top);
            top--;
            return retVal;              // store previous top, change to new top, and return old top val
        }
    }
    
    public void increment(int k, int val) {
        if (k > stack.size()) {
            for (int i = 0; i < stack.size(); i++) {
                stack.set(i, stack.get(i) + val);
            }
        }                               // increment through entire list
        else {
            for (int i = 0; i < k; i++) {
                stack.set(i, stack.get(i) + val);
            }         
        }                               // increment up to index k-1
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */
