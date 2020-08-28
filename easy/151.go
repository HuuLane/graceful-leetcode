package main

import (
	"fmt"
	"strings"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseWords(s string) string {
	if len(s) == 0 {
		return s
	}
	var b strings.Builder
	pos := len(s) - 1

	// from tail to head
	for cur := pos; cur >= 0; cur-- {
		if s[cur] == ' ' {
			if cur != pos {
				b.WriteString(s[cur+1 : pos+1])
				b.WriteByte(' ')
			}
			pos = cur - 1
		}
	}
	if s[0] != ' ' {
		b.WriteString(s[0 : pos+1])
		return b.String()
	}
	// for " "
	if b.Len() == 0 {
		return ""
	}
	ret := b.String()
	return ret[:len(ret)-1]
}

func main() {
	r := reverseWords("   123 hoo ggg   yoo  yoo  d123!!  22")
	fmt.Println(r)
}
