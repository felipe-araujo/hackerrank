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

    var arr [][]int32
    for i := 0; i < 6; i++ {
        arrRowTemp := strings.Split(readLine(reader), " ")

        var arrRow []int32
        for _, arrRowItem := range arrRowTemp {
            arrItemTemp, err := strconv.ParseInt(arrRowItem, 10, 64)
            checkError(err)
            arrItem := int32(arrItemTemp)
            arrRow = append(arrRow, arrItem)
        }

        if len(arrRow) != int(6) {
            panic("Bad input")
        }

		arr = append(arr, arrRow) 
    }

    var max_s int32
    max_s = 7 * (-9)
    for i := 1; i < len(arr)-1; i++{
        for j := 1; j < len(arr[0])-1; j++{
            s := arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            s += arr[i][j]
            s += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if s > max_s{
                max_s = s
            }
        }
    }

    fmt.Println(max_s)
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
