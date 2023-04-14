import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { UserdashboardComponent } from './components/userdashboard/userdashboard.component';
import { HomeComponent } from './components/home/home.component';

const routes: Routes = [
  {path : '', redirectTo:'/login', pathMatch:'full'},
 
  {path: 'login', component:LoginComponent},
  {path: 'signup', component:RegisterComponent},
  {path: 'user-dash', component:UserdashboardComponent},
  {path: 'home', component: HomeComponent},
];




@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
