import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/shared/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  username: string | undefined;
  password: string | undefined;
  

  constructor(private auth: AuthService, private router: Router) { }

  login() {
    if (!this.username || !this.password) {
      alert('Please enter username and password');
      return;
    }
    this.auth.login(this.username, this.password);
    this.username = '';
    this.password = '';
  }

  forgotPassword(){}

  createAccount(){}


}


