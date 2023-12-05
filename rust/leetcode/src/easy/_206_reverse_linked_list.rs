struct Solution;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev = None;
        let mut curr = head;

        while let Some(mut curr_node) = curr {
            let next_temp = curr_node.next.take();
            curr_node.next = prev;
            prev = Some(curr_node);
            curr = next_temp;
        }

        prev
    }
}

#[test]
fn test() {
    assert_eq!(
        Solution::reverse_list(Some(Box::new(ListNode {
            val: 1,
            next: Some(Box::new(ListNode {
                val: 2,
                next: Some(Box::new(ListNode::new(3)))
            }))
        }))),
        Some(Box::new(ListNode {
            val: 3,
            next: Some(Box::new(ListNode {
                val: 2,
                next: Some(Box::new(ListNode::new(1)))
            }))
        }))
    );
}
