package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)



func main() {
    reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

    nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
    checkError(err)
    n := int32(nTemp)
    
    var count int
    var bin string
    
    count = 1
    bin = ""
    
    for ; n > 1; {
        if n % 2 == 1{
            count +=1
            bin = "1" + bin
        }else{
            bin = "0" + bin
        }        
        n = n / 2
    }

    bin = "1" + bin

    //fmt.Println(bin)
    parts := strings.Split(bin, "0")
    max :=0
    for _, part := range parts{
        if len(part) > max{
            max = len(part)
        }

    }
    
    fmt.Print(max) 
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}
