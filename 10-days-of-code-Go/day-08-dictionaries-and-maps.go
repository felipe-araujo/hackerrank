package main

import (
	"bufio"
	"fmt"
	"strconv"
	"strings"

)

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	var n string
	fmt.Scanln(&n)
	scanner := bufio.NewScanner(os.Stdin)
	n := scanner.Text()
	times, _ := strconv.Atoi(n)

	var book = make(map[string]string)
	var name string
	var tel string
	var line string
	for t := 0; t < times; t++ {
		line = scanner.Text()
		words := strings.Fields(someString)
		//fmt.Scanln(&tel)
		name = words[0]
		tel = words[1]
		book[name] = tel
	}
	//fmt.Println(book)

	var query string
	for {
		_, err := fmt.Scanln(&query)
		if err != nil {
			break
		}

		if val, ok := book[query]; ok {
			fmt.Println(query + "=" + val)
		} else {
			fmt.Println("Not found")
		}
	}
}
