import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class MyserviceService {
  tableUrl: string = "http://127.0.0.1:5000/tables ";
  myUrl: string = "http://localhost:5000"
  tes:string= "http://127.0.0.1:5000/testing";

  constructor( private http: HttpClient,
    private router: Router) { }
  getTable(){
    return  this.http.get(this.tableUrl)
  }
  getData(tablename){
    return  this.http.get(this.myUrl+"/"+tablename)
  }
  posttable(tablename){
    return this.http.post(this.tes,
      {
        tablename
      })
    }
  postData(rowData, tablename){
    return this.http.post(this.myUrl + "/update_" + tablename,
      {
        rowData
      })
  }
  postDel(delData, tablename){
    return this.http.post(this.myUrl + "/delete_" + tablename,
    {
      delData
    })
  }

  deleteData(id_del){
    return this.http.delete("http://localhost:5000/dummy/" + id_del); }  
  putDData(id_del){
    return this.http.put("http://localhost:5000/dummy/" + id_del,
    {
      "id":id_del,
      "name": "dmalmalka",
    })
  }
}