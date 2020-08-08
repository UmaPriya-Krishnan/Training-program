import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AgGridModule } from 'ag-grid-angular'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FrontComponent } from './front/front.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { DisplayComponent } from './display/display.component';
import { TestingComponent } from './testing/testing.component';


@NgModule({
  declarations: [
    AppComponent,
    FrontComponent,
    DisplayComponent,
    TestingComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AgGridModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [FrontComponent]
})
export class AppModule { }
