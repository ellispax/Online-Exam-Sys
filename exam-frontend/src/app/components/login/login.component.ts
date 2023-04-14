import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/shared/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent  {

  username: string = '';
  password: string = '';
  error: string = '';

  constructor(private authService: AuthService, private router: Router) { }

  
  login(){
    if (!this.username || !this.password) {
      alert('Please enter username and password');
      return;
    }  
    

    this.authService.login(this.username, this.password);
    this.username = '';
    this.password = '';
  }

  onSubmit() {
   
    // this.authService.login(this.username, this.password).subscribe(
    //   (response) => {
    //     localStorage.setItem('token', response.token);
    //     this.router.navigate(['/user-dash']);
    //   },
    //   (error) => {
    //     this.error = 'Invalid username or password';
    //   }
    // );
  }



  // username: string | undefined;
  // password: string | undefined;
  

  // constructor(private auth: AuthService, private router: Router) { }

  // login() {
  //   if (!this.username || !this.password) {
  //     alert('Please enter username and password');
  //     return;
  //   }
  //   this.auth.login(this.username, this.password);
  //   this.username = '';
  //   this.password = '';
  // }

  forgotPassword(){}

  createAccount(){}


}

