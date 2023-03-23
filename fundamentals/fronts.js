class Node{
    constructor(data){
        this.data = data
        this.ext = null;
    }
}

class LinkedList{
    constructor(){
        this.head = null;
    }


addFront(val) {
    let new_node = new Node(val);
    
    if(!this.head){
        this.head = new_node;
        return this;
    }
// checks if empty, from reading, is it lways needed?

    new_node.next = this.head;
    this.head = newNode;
    return this.head;

}

removeFront() {
    if  (this.head == null) {
        return this.head;
    }
    var RemoveNode = this.head;
    this.head = RemoveNode.next; 
    return this.head;
}

Front(){
    if  (this.head == null){
        return this.head;
    }
    else
    {
        return this.head.val
    }
}
}