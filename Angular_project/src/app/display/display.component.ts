import { Component, OnInit, ViewChild } from '@angular/core';
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
  public defaultColDef;
  public editType;
  keys: any[] = [];
  values: any[] = [];
  dataa: any;
  len: any;
  tablename: string;
  rowData: any;
  columnDefs: any[] = [];
  column: any;
  k: any;
  postData: any;
  row: any;
  postDel: any;
  rawData: any[] = [];
  id: any;
  actualData: any[] = [];
  editedData: any[] = [];
  actualDatatype: any[] = [];
  editedDatatype: any[] = [];
  // putDddata: any;
  // delData: any;
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
    this.service.getData(this.tablename).subscribe((data)=>{  
    this.dataa = data; 
   for(var i in data)
   {
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
    var len = this.keys.length
    this.columnDefs.push({"field": this.keys[0], checkboxSelection: true, filter: true,  sortable: true})    
    for (this.k in this.keys)
    {
      if (this.k > 0 && this.k < len-2)
      {
        this.columnDefs.push({"field": this.keys[this.k], filter: true});
      }      
    } 
     this.column = this.columnDefs
  });
}

// getSelected(){
// this.values = this.agGrid.api.getSelectedRows();
// console.log(this.values)
// }
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
for (var ind in this.editedDatatype)
  {
  if (this.editedDatatype[ind] == "undefined")
    {
      console.log(this.editedDatatype[ind])
      this.editedDatatype[ind] = "object"
    }
  }
for(var dt in this.editedData)
  {
  if (typeof(this.editedData[dt]) == 'string')
    {
    if (this.editedData[dt].indexOf("GMT") > -1)
      {
        this.editedData[dt] = this.dateConversion(this.editedData[dt])
      }
    }
  }
  if (JSON.stringify(this.actualData) == JSON.stringify(this.editedData))
    {
      window.alert("No changes are made to any data")
    }
  // if (JSON.stringify(this.editedDatatype) == JSON.stringify(this.actualDatatype))
  else
    {
      this.service.postData(this.editedData, this.tablename).subscribe((data)=>
      {
        this.postData=data;  
        //console.log(this.postData)
      })
    window.alert("Row with " + this.keys[0] + ": " + this.editedData[0] + " has been updated")
  }
}
 
delete()
{
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
  this.service.postDel(this.rawData, this.tablename).subscribe((data)=>
  {
    this.postDel = data;
  })
  window.alert("Row with " + this.keys[0] + ": " + this.rawData[0] + " is deleted")
 }

dateConversion(str) 
{
  var mnths = 
  {
    Jan: "01", Feb: "02", Mar: "03", Apr: "04", May: "05", Jun: "06", Jul: "07", Aug: "08", Sep: "09", Oct: "10", Nov: "11", Dec: "12"
  },
    date = str.split(" ");
    return [date[3], mnths[date[2]], date[1]].join("-");
}
ngOnInit(): void 
 {
    this.display()
    this.defaultColDef = 
    {
      flex: 1,
      minWidth: 110,  
      editable: true,
      resizable: true,
      sortable: true
    };
  } 
}
