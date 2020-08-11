import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class MyserviceService {
  myUrl: string = "http://localhost:5000";

  constructor( private http: HttpClient, private router: Router) { }

  getTable()
  {
    return this.http.get(this.myUrl + '/tables')
  }

  getData(tablename)
  {
    return this.http.get(this.myUrl+"/select/"+tablename)
  }

  getHiddenData(tablename)
  {
    return this.http.get(this.myUrl+"/select/hidden/"+tablename)
  }

  posttable(tablename)
  {
    return this.http.post(this.myUrl+'/testing',
      {
        tablename
      })
  }

  postData(rowData, tablename)
  {
    return this.http.post(this.myUrl + "/update/" + tablename,
      {
        rowData
      })
  }
  
  postDel(delData, tablename)
  {
    return this.http.post(this.myUrl + "/s_delete/" + tablename,
    {
      delData
    })
  }
}
  // deleteData(id_del){
  //   return this.http.delete("http://localhost:5000/dummy/" + id_del); }  
  // putDData(id_del){
  //   return this.http.put("http://localhost:5000/dummy/" + id_del,
  //   {
  //     "id":id_del,
  //     "name": "dmalmalka",
  //   })

