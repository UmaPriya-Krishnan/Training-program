import { Component, OnInit } from '@angular/core';
import { MyserviceService } from '../myservice.service';
import { Router } from '@angular/router'

@Component({
  selector: 'app-front',
  templateUrl: './front.component.html',
  styleUrls: ['./front.component.css']
})
export class FrontComponent implements OnInit {

  tableData: any;
  tablename: string;
  dataa: any;
  value: boolean = true;
  
   constructor ( private service:MyserviceService,
                  private router: Router) {
      this.displayTable()
     }
  
    displayTable(){
      this.service.getTable().subscribe((data) => {
      this.tableData = data;
      //console.log(JSON.stringify(this.tableData))
      })
    } 
         submit(tablename){
         this.tablename = tablename
         console.log(tablename)
         //this.router.navigate(['/select']) 
       }
     
    ngOnInit(): void {  }
  }
  
