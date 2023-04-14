import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private loggedInSubject: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  public loggedIn = this.loggedInSubject.asObservable();

  constructor() { }

  login(username: string, password: string) {}

  logout() {
    localStorage.removeItem('token');
    this.loggedInSubject.next(false);
  }

}
