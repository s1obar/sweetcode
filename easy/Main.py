import IsPalindrome,RomanToIntegers,LongestCommonPrefix,ValidParentheses,TwoSortedListsMerge

if __name__ == '__main__':
    l1 = TwoSortedListsMerge.createLinkedList([1,2,4])
    l2 = TwoSortedListsMerge.createLinkedList([1,3,4])
    result = TwoSortedListsMerge.toList(TwoSortedListsMerge.mergeTwoLists(l1,l2))
    print(result)