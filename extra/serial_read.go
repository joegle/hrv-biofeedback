// Copyright (c) 2014 Joseph Wright <joegle@gmail.com>
// License: BSD 3 clause

/*
COMPILE:
 $ go build serial_read.go
*/
package main

import (
        "github.com/tarm/goserial"
        "log"
	"time"
	"fmt"
	//"os"
	"bufio"
)

func main() {
        c := &serial.Config{Name: "/dev/ttyUSB0", Baud: 115200}
        s, err := serial.OpenPort(c)
        if err != nil {
                log.Fatal(err)
        }

     	reader := bufio.NewReader(s)

	for {

		reply, err := reader.ReadBytes('\n')
		switch err {
		case nil:
			fmt.Print(string(reply))		
		default:
			time.Sleep(time.Second/40)

		}
	}
}
