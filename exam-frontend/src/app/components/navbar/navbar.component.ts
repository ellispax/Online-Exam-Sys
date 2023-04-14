import { Component } from '@angular/core';
import { AuthService } from 'src/app/shared/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})

  export class NavbarComponent {
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
    // isLoggedIn: boolean = false;
  
    // constructor(private authService: AuthService, private router: Router) {
    //   this.authService.isLoggedIn().subscribe((loggedIn: boolean) => {
    //     this.isLoggedIn = loggedIn;
    //   });
    // }
  
    // logout() {
    //   this.authService.logout();
    //   this.router.navigate(['/login']);
    // }
  
}
