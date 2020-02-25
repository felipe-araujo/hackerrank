package main

import (	
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

)

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	var n string
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	n = scanner.Text()
	times, err := strconv.Atoi(n)
	if err != nil{
		panic(err)
	}
	//fmt.Printf("times= %d\n", times)

	var book = make(map[string]string)
	var name string
	var tel string
	var line string
	for t := 0; t < times; t++ {
		scanner.Scan()
		line = scanner.Text()
		words := strings.Fields(line)
		//fmt.Print(words)
		name = words[0]
		tel = words[1]
		book[name] = tel
	}
	
	for scanner.Scan(){
		line = scanner.Text()
		if val, ok := book[line]; ok {
			fmt.Println(line + "=" + val)
		}else{
			fmt.Println("Not found")
		}
	}

}
