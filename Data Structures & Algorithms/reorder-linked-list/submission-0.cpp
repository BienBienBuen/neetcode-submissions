/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        //recursively do this. First find tail
        //do head->next = &tail (or the pointer that points to tail)
        //do tail->next = head->next
        //reorderList (tail->next)
        ListNode* p = head;
        ListNode* tail = head;

        if (p->next == nullptr || p->next->next == nullptr){
            return ;
        }

        while (tail->next->next != nullptr) {
            tail = tail->next;
        }
        //now tail is the one pointing to the last cell
        tail->next->next = p->next;
        p->next = tail->next;
        ListNode* newHead = tail->next->next;
        tail->next = nullptr;

        reorderList(newHead);

    }
};
