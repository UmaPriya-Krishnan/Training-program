import { Component, OnInit, ViewChild, APP_ID } from '@angular/core';
import { FrontComponent } from '../front/front.component'
import { MyserviceService } from '../myservice.service';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AgGridAngular } from 'ag-grid-angular';
import { CommentStmt } from '@angular/compiler';

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
  actualData: any[] = [];
  editedData: any[] = [];
  actualDatatype: any[] = [];
  editedDatatype: any[] = [];
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
       this.val = data[i];
      for(var j in this.val)
      {
        var sub_val = this.val[j];
        this.actualData.push(sub_val)
        this.actualDatatype.push(typeof(sub_val))
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
this.row = editedRow.data;
 for (var i in this.row)
{
 var value = this.row[i]; 
 this.editedData.push(value);
 this.editedDatatype.push(typeof(value))
}
  console.log(this.editedData)
  console.log(this.actualData)
  //console.log(this.actualDatatype)
  for (var ind in this.editedDatatype)
  {
    if (this.editedDatatype[ind] == "undefined")
    {
      console.log(this.editedDatatype[ind])
      this.editedDatatype[ind] = "object"
    }
  }
  console.log(this.actualDatatype)
  console.log(this.editedDatatype)
  if (JSON.stringify(this.editedDatatype) === JSON.stringify(this.actualDatatype))
   {
    this.service.postData(this.editedData, this.tablename).subscribe((data)=>{
      this.postData=data;  
    })
   }
else
{
  window.alert("Please enter value of correct data type")
}
}
delete(){
  this.row = this.agGrid.api.getSelectedRows();
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
