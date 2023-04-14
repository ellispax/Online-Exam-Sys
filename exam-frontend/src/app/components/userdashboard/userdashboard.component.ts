import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/shared/auth.service';

@Component({
  selector: 'app-userdashboard',
  templateUrl: './userdashboard.component.html',
  styleUrls: ['./userdashboard.component.css']
})
export class UserdashboardComponent {

  isLoggedIn: boolean = false;

    constructor(private authService: AuthService, private router: Router) {
      this.authService.loggedIn.subscribe((loggedIn: boolean) => {
        this.isLoggedIn = loggedIn;
      });
    }
  
    logout() {
      this.authService.logout();
      this.router.navigate(['/login']);
    }
}
