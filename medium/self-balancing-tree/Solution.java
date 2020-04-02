	/* Class node is defined as :
    class Node 
    	int val;	//Value
    	int ht;		//Height
    	Node left;	//Left child
    	Node right;	//Right child

	*/

	static Node insert(Node root,int val)
    {
        Node current = root; 
        Node previous = null;
    	while(current != null){
            previous = current;
            current.ht += 1;
            if(val < current.val){
                current = current.left;
            }else{
                current = current.right;
            }
        }
        Node newNode = new Node();
        newNode.val = val;
        newNode.ht = 0;
        if (val < previous.val){
            previous.left = newNode;
        }else{
            previous.right = newNode;
        }
        
        
        return root;
            
    }