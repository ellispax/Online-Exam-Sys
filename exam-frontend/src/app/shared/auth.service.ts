import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private loggedInSubject: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  public loggedIn = this.loggedInSubject.asObservable();

  constructor(private http: HttpClient, private router: Router) { }

  login(username: string, password: string) {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<any>('http://localhost:8000/API/login/', { username: username, password: password }, { headers: headers })
      .toPromise()
      .then(data => {
        localStorage.setItem('token', data.token);
        this.loggedInSubject.next(true);
        this.router.navigate(['/user-dash']);
      })
      .catch(error => {
        console.log(error);
        alert('Incorrect User Details');
      });
  }

  logout() {
    localStorage.removeItem('token');
    this.loggedInSubject.next(false);
  }
}



// import { HttpClient, HttpHeaders } from '@angular/common/http';
// import { Injectable } from '@angular/core';
// import { BehaviorSubject, Observable } from 'rxjs';

// @Injectable({
//   providedIn: 'root'
// })
// export class AuthService {
//   private baseUrl = 'http://localhost:8000';
//   private loggedIn = new BehaviorSubject<boolean>(false);

//   constructor(private http: HttpClient) {
//     this.loggedIn.next(this.isAuthenticated());
//   }

//   login(username: string, password: string): Observable<any> {
//     console.log('Sending login request for username:', username, 'password:', password);
//     const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
//     const url = `${this.baseUrl}/API/login/`;
//     console.log('Headers:', headers);

//     return this.http.post<any>(url, { username, password }, { headers });

//   }

//   logout() {
//     localStorage.removeItem('token');
//     this.loggedIn.next(false);
//   }

//   getToken() {
//     return localStorage.getItem('token');
//   }

//   isAuthenticated(): boolean {
//     return !!this.getToken();
//   }

//   isLoggedIn(): Observable<boolean> {
//     return this.loggedIn.asObservable();
//   }
// }



// // import { HttpClient, HttpHeaders } from '@angular/common/http';
// // import { Injectable } from '@angular/core';
// // import { Router } from '@angular/router';
// // import { BehaviorSubject, Observable } from 'rxjs';

// // @Injectable({
// //   providedIn: 'root'
// // })
// // export class AuthService {
// //   private baseUrl = 'http://localhost:8000';
// //   private loggedIn = new BehaviorSubject<boolean>(false);

// //   constructor(private http: HttpClient, private router: Router) {
// //     this.loggedIn.next(this.isAuthenticated());
// //   }

// //   login(username: string, password: string): Observable<any> {
// //     const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
// //     const url = `${this.baseUrl}/API/login/`;
// //     return this.http.post<any>('http://localhost:8000/API/login/', {username: username, password: password}, { headers });

// //   }

// //   logout() {
// //     localStorage.removeItem('token');
// //     this.loggedIn.next(false);
// //   }

// //   getToken() {
// //     return localStorage.getItem('token');
// //   }

// //   isAuthenticated(): boolean {
// //     return !!this.getToken();
// //   }

// //   isLoggedIn(): Observable<boolean> {
// //     return this.loggedIn.asObservable();
// //   }
// // }
