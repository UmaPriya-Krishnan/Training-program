package main

import (
	"fmt"

	"github.com/umapriya-krishnan/Training-program/cred"
)

func main() {
	err := cred.Dbconnect()
	if err != nil {
		fmt.Println("Error occured while establishing connection", err)
	} else {
		fmt.Printf("Connection established successfully")
	}

}
