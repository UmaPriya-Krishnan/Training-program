// import { Component } from '@angular/core';


// @Component({
//   selector: 'app-root',
//   templateUrl: './app.component.html',
//   styleUrls: ['./app.component.css']
// })
// export class AppComponent {
//    columnDefs = [
//         {field: 'make' },
//         {field: 'model' },
//         {field: 'price'}
//     ];
//     rowData = [
//         { make: 'Toyota', model: 'Celica', price: 35000 },
//         { make: 'Ford', model: 'Mondeo', price: 32000 },
//         { make: 'Porsche', model: 'Boxter', price: 72000 }
//     ];
//     tableData: any;
      
//     constructor ( ){} 

// }

import { Component, OnInit, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AgGridAngular } from 'ag-grid-angular';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  @ViewChild('agGrid') agGrid: AgGridAngular;
  private gridApi;
  private gridColumnApi;
  public defaultColDef;
    title = 'app';

    // columnDefs = [
    //     {field: 'make', sortable: true, filter: true, checkboxSelection: true },
    //     {field: 'model', sortable: true, filter: true },
    //     {field: 'price', sortable: true, filter: true }
    // ];
    columnDefs = [
      {field: 'COMPANY_ID', checkboxSelection: true},
      {field: 'COMPANY_NAME' },
      {field: 'PLACEMENT_END_DATE'},
      {field: 'PLACEMENT_START_DATE' },
      {field: 'PLACEMENT_DATE'},
      {field: 'PLACEMENT_VENUE'}
    ];

    rowData: any;
    constructor(private http: HttpClient) {

    }

    ngOnInit() {
      this.rowData = this.http.get('http://localhost:5000/dimension_placement_details');
      this.defaultColDef = {
        flex: 1,
        minWidth: 110,
        editable: true,
        resizable: true,
      };
    }
    onGridReady(params) {
      this.gridApi = params.api;
      this.gridColumnApi = params.columnApi;
  }
  // getSelectedRows() {
  //   const selectedRow = this.gridApi.getSelectedRows();
    // console.log(selectedRow);
    getSelectedRows() {
      const selectedRow = this.agGrid.api.getSelectedRows();
      console.log(selectedRow)
  }
}
