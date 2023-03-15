class SLLNode{
    constructor(val){
        this.value = val
        this.next = null;
    }
}

class SLL {
    // constructor, other methods, removed for brevity
    constructor() {
        this.head = null;
    }

    display() {
    	// neatly display nodes in my list
        var string ="";
        // check if null first , get from display
        if (this.head == null){
            return "";
        }
        string += this.head.value;
        var string2 = this.head.next;
        while (string2 != null) {
            string + string2;
            string2 = string2.next
        }
        return string
    }
 }