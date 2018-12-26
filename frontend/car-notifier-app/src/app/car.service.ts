import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable, of } from "rxjs";
import { catchError, map, tap } from "rxjs/operators";
import { Car } from './car';

const httpOptions = {
  headers: new HttpHeaders({ "Content-Type": "application/json" })
};

@Injectable({
  providedIn: 'root'
})
export class CarService {

  private carsUrl = "http://127.0.0.1:5000/api/v1/cars"; // URL to web api

  getCars(): Observable<Car[]> {
    return this.http.get<Car[]>(this.carsUrl).pipe(
      tap(_ => this.log("fetched heroes")),
      tap(cars => console.log(cars)),
      catchError(this.handleError("getHeroes", []))
    );
  }

  private handleError<T>(operation = "operation", result?: T) {
    return (error: any): Observable<T> => {
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  /** Log a HeroService message with the MessageService */
  private log(message: string) {
    console.log(message);
  }

  constructor(
    private http: HttpClient,
  ) {}
}
