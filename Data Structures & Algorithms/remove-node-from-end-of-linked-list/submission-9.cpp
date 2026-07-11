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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* p = head;
        ListNode* q = head;

        if (head->next == nullptr && n == 1) {
            return nullptr;
        }

        for (int i = 0; i < n; i++) {
            q = q->next;
        }

        if (q == nullptr) {
            ListNode* newhead = head->next;
            delete head;
            head = nullptr;
            return newhead;
        }

        ListNode* prev = p;
        while (q != nullptr) {
            q = q->next;
            prev = p;
            p = p->next;
        }

        ListNode* remove = prev->next;
        prev->next = remove->next;
        delete remove;
        remove = nullptr;
        return head;

    }
};
