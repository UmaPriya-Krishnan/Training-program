import { Component, OnInit, ViewChild } from '@angular/core';
import { FrontComponent } from '../front/front.component'
import { MyserviceService } from '../myservice.service';
import { Router } from '@angular/router';
import { AgGridAngular } from 'ag-grid-angular';

@Component({
  selector: 'app-hidden',
  templateUrl: './hidden.component.html',
  styleUrls: ['./hidden.component.css']
})
export class HiddenComponent implements OnInit {
  @ViewChild('agGrid') agGrid: AgGridAngular;
  public defaultColDef;
  public editType;
  keys: any[] = [];
  values: any[] = [];
  dataa: any;
  tablename: string;
  rowData: any;
  columnDefs: any[] = [];
  column: any;
  k: any;
  val: any;
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
    this.service.getHiddenData(this.tablename).subscribe((data)=>{
    this.dataa = data;
   for(var i in data)
   {
       this.val = data[i];
      for(var j in this.val)
      {
        var sub_val = this.val[j];
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
select(){
  this.router.navigate(['select/:tablename'])
}
  ngOnInit(): void {
    this.display()
  }
}
