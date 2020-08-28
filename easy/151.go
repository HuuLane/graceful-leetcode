package main

import (
	"fmt"
	"strings"
)

func reverseWords(s string) string {
	if len(s) == 0 {
		return s
	}
	var b strings.Builder

	// sentinel
	s = " " + s
	// floating window: from tail to head
	for left, right := len(s)-1, len(s)-1; left >= 0; left-- {
		if s[left] == ' ' {
			if left != right {
				b.WriteString(s[left+1 : right+1])
				b.WriteByte(' ')
			}
			right = left - 1
		}
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
