package cred

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)
github.com/umapriya-krishnan/Training-program v0.0.0-20201119122526-f8d989c4d61f h1:fDxzN9gZznZXKXwVXjLGP2jZRToRCmEWbgw6zVQFOEA=
github.com/umapriya-krishnan/Training-program v0.0.0-20201119122526-f8d989c4d61f/go.mod h1:9bUq9cPRq8gOzAeo0AY/iDpaPYlqP7exCHIHzZzMQck=

const (
	host     = "localhost"
	port     = 5432
	user     = "postgres"
	password = "password123"
	dbname   = "db"
)

func Dbconnect() (err error) {
	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {
		return err
	}
	err = db.Ping()
	if err != nil {
		return err
	}
	return nil
}
