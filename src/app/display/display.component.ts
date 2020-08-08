import { Component, OnInit, ViewChild, APP_ID } from '@angular/core';
import { FrontComponent } from '../front/front.component'
import { MyserviceService } from '../myservice.service';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AgGridAngular } from 'ag-grid-angular';

@Component({
  selector: 'app-display',
  templateUrl: './display.component.html',
  styleUrls: ['./display.component.css']
})
export class DisplayComponent implements OnInit {
  @ViewChild('agGrid') agGrid: AgGridAngular;
  // private gridApi;
  // private gridColumnApi;
  public defaultColDef;
  public editType;
  myUrl: string = "http://localhost:5000"
  keys: any[] = [];
  values: any[] = [];
  dataa: any;
  tablename: string;
  rowData: any;
  columnDefs: any[] = [];
  column: any;
  k: any;
  postData: any;
  row: any;
  postDel: any;
  rawData: any[] = [];
  rowD: any;
  abcd: any;
  id: any;
  putDddata: any;
  delData: any;
  val: any;
  constructor(private service:MyserviceService,
              private table: FrontComponent,
              private router: Router,
              private http: HttpClient)
            { 
              this.router.routeReuseStrategy.shouldReuseRoute=()=>false;
              this.editType = 'fullRow';
            }
  display()
  {
    this.keys = [];
    this.tablename = this.table.tablename
    this.rowData =  this.http.get(this.myUrl+"/"+ this.tablename)
    this.service.getData(this.tablename).subscribe((data)=>{  
    this.dataa = data; 
   for(var i in data)
   {
      var key = i;
       val = data[i];
     // console.log(val)
      for(var j in val)
      {
        var sub_val = val[j];
        this.keys.push(j);      
      }
      break;
  }
    this.columnDefs.push({"field": this.keys[0], checkboxSelection: true})    
    for (this.k in this.keys)
    {
      if (this.k > 0 )
      {
        this.columnDefs.push({"field": this.keys[this.k], filter: true});
       }      
    } 
     this.column = this.columnDefs
  });

}
getSelected(){
this.values = this.agGrid.api.getSelectedRows();
console.log(this.values)
}
public editedRow(editedRow): void
{
// this.values = this.agGrid.api.getSelectedRows();
// console.log(this.values)
this.row = editedRow.data;
//console.log(this.keys)
console.log(this.dataa[0])
 for (var i in this.row)
{
 var value = this.row[i]; 
 console.log(typeof(value), value)
 //console.log(value)
 this.rawData.push(value)
}
console.log(this.rawData)
  this.service.postData(this.rawData, this.tablename).subscribe((data)=>{
  this.postData=data; 
})
}
delete(){
  this.row = this.agGrid.api.getSelectedRows();
  //console.log(this.row)
  for (var i in this.row)
{
 var values = this.row[i]; 
 for (var j in values)
 {
   var dt = values[j];
   console.log(typeof(dt))
   this.rawData.push(dt)
 }
}
  this.service.postDel(this.rawData, this.tablename).subscribe((data)=>{
  this.postDel = data;
 })
}
// deleteMyData(){
//   this.service.deleteData(this.id).subscribe((data) =>{
//     this.delData = data;
//     window.alert("User with ID: " + this.id + " has been deleted successfully")
//   })
// }

// putMyData(){
//   this.service.putDData(this.id).subscribe((data)=>{
//   this.putDddata = data;
//   console.log(this.putDddata)
//   })
//}
onCellValueChanged(params)
  {
  }
  // onGridReady(params){
  //   this.gridApi = params.api;
  //   this.gridColumnApi = params.columnApi;
  //  }
 ngOnInit(): void 
 {
    this.display()
    this.defaultColDef = 
    {
      flex: 1,
      minWidth: 110,  
      editable: true,
      resizable: true,
    };
  } 
}
