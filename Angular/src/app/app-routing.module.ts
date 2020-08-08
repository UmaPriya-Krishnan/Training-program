import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DisplayComponent } from './display/display.component'
import { TestingComponent } from './testing/testing.component'
const routes: Routes = [
  {path:'select/:tablename', component: DisplayComponent},
  {path: 'test', component: TestingComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes,{onSameUrlNavigation:'reload'})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
