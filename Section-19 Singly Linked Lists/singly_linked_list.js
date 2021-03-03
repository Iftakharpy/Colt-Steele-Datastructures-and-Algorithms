class Node{
    constructor(value){
        this.value = value
        this.next = undefined
    }
}


class Singly_Linked_List{
    empty_repr = "Empty"
    constructor(value){
        this.head = new Node(value)
        this.tail = this.head

        this.length = 0
        if (this.value !== undefined){
            this.length = 1
        }
    }

    show(){
        let string = ""
        let temp = this.head
        while(temp!==undefined){
            string += `${temp.value} -> `
            temp = temp.next
        }
        
        string = string.slice(0,string.length-4)
        return (string==='undefined') ? this.empty_repr : string
    }

    push(value){
        if (value===undefined){
            throw TypeError("Inserting undefined values are not allowed")
        }
        let new_node = new Node(value)

        if (this.length==0){
            this.head = new_node
            this.tail = this.head
            this.length = 1
            return
        }

        this.tail.next = new_node
        this.tail = new_node
        this.length += 1
    }

    pop(){
        if (this.length===0){
            return undefined
        }
        else if (this.length===1){
            value = this.head.value
            this.head = new Node()
            this.tail = this.head
            this.length = 0
            return value
        }

        let temp = this.head
        while (temp.next.next!==undefined){
            temp = temp.next
        }

        let value = temp.next.value
        this.tail = temp
        temp.next = undefined
        this.length -= 1
        return value
    }
}




//test
a = new Singly_Linked_List()

// for (i=0;i<20;i++){
//     a.push(i)
// }

console.log(a.show())