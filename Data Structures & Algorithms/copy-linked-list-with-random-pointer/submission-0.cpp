/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> map;

        Node* cur = head;
        while (cur != nullptr) {
            Node* copy = new Node(cur->val);
            map[cur] = copy;
            cur = cur->next;
        }
        map[nullptr] = nullptr;


        Node* curr = head;
        while (curr != nullptr) {
            Node* copy = map[curr];
            copy->next = map[curr->next];
            copy->random = map[curr->random];
            curr = curr->next;
        }
        return map[head];

    }
};
