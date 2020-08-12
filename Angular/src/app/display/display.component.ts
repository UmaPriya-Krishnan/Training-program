import { Component, OnInit, ViewChild } from '@angular/core';
import { FrontComponent } from '../front/front.component'
import { MyserviceService } from '../myservice.service';
import { Router } from '@angular/router';
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
  sendData: any[] = []
  actualDatatype: any[] = [];
  editedDatatype: any[] = [];
  val: any;
  dis: any[] = [];
  updateDis: any[] = [];
  constructor(private service:MyserviceService,
              private table: FrontComponent,
              private router: Router)
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
      if (this.k > 0 && this.k < len-3)
      {
        this.columnDefs.push({"field": this.keys[this.k], filter: true});
      }
    }
     this.column = this.columnDefs
  });
}
updateRow(){
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
  this.service.postData(this.editedData, this.tablename).subscribe((data)=>
  {
    this.postData=data;
  })
  // if (JSON.stringify(this.actualData) == JSON.stringify(this.editedData))
  //   {
  //     window.alert("No changes are made to any data")
  //   }
  const len = this.editedData.length
  const actLen = this.actualData.length
  for (var ed = 0; ed<len-1;)
  {
    this.updateDis.push(this.editedData[ed])
    ed = ed+actLen
  }
    window.alert("Row with " + this.keys[0] + ": " + this.updateDis + " has been edited")
    // this.updateDis = []
    // this.editedData = []
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
for (var ind in this.editedDatatype)
  {
  if (this.editedDatatype[ind] == "undefined")
    {
      this.editedDatatype[ind] = "object"
    }
  }
}
  // if (JSON.stringify(this.editedDatatype) == JSON.stringify(this.actualDatatype))
  //   {
  //   }
  //   else
  //   {
  //     window.alert("Data types doesn't match")
  //   }

delete()
{
  this.row = this.agGrid.api.getSelectedRows();
  for (var i in this.row)
    {
      var values = this.row[i];
      for (var j in values)
      {
        var dt = values[j];
        this.rawData.push(dt)
      }
    }
    const len = this.rawData.length
    const actLen = this.actualData.length
    for (var ed = 0; ed<len-1;)
    {
      this.dis.push(this.rawData[ed])
      ed = ed+actLen
    }
  this.service.postDel(this.rawData, this.tablename).subscribe((data)=>
  {
    this.postDel = data;
  })
  window.alert("Row with " + this.keys[0] + ": " + this.dis + " has been deleted successfully")
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
hidden(){
  this.router.navigate(['/hidden'])
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
