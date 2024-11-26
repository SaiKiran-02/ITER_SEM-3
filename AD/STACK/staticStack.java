
public class staticStack{
    int top;
    int stackArray[];
    int maxsize;

    public staticStack(int size){
        top = -1;
        maxsize = size;
        stackArray = new int[maxsize];
    }

    public void push(int n){
        if (top == maxsize-1){
            System.out.println("Stack is overflow.");
        }
        else{
            top++;
            stackArray[top] = n;
            System.out.println("element pushed.");
            System.out.println(stackArray[top]);
        }
    }

    public  void pop(){
        if (top == -1){
            System.out.println("Stack is underflow");
        }
        else{
            System.out.print("poped element is: ");
            System.out.println(stackArray[top]);
            top--;
        }
    } 
    public static void main(String[] args) {
        staticStack stack = new staticStack(5);
         
        stack.push(10);
        stack.push(20);
        stack.push(30);

        stack.pop();
    }
}