#include <iostream>
#include <cstddef>

using namespace std;	

class Node{
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d){
            data = d;
            left = NULL;
            right = NULL;
        }
};
class Solution{
    public:
  		Node* insert(Node* root, int data) {
            if(root == NULL) {
                return new Node(data);
            }
            else {
                Node* cur;
                if(data <= root->data){
                    cur = insert(root->left, data);
                    root->left = cur;
                }
                else{
                    cur = insert(root->right, data);
                    root->right = cur;
               }

               return root;
           }
        }

		int getHeight(Node* root){
          return h(root, 0);
        }

        int h(Node* parent, int current){
            int left=current, right=current;
            if(parent == NULL){
                return current;
            }
            if(parent->right != NULL){
                right = h(parent->right, current+1);
            }
            if(parent->left != NULL){
                left = h(parent->left, current+1);
            }
            return (left > right)? left: right;
        }

}; //End of Solution