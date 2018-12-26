import { Component, OnInit } from '@angular/core';
import { Car } from '../car';

@Component({
  selector: 'app-cars',
  templateUrl: './cars.component.html',
  styleUrls: ['./cars.component.css']
})
export class CarsComponent implements OnInit {
  cars: Car[];

  getCars(): void {
    this.cars = [
      {id: 1 , name: '118'},
      {id: 2 , name: 'i8'},
      {id: 2 , name: 'i8'},
      {id: 2 , name: 'i8'},
      {id: 1 , name: '118'},
      {id: 2 , name: 'i8'},
      {id: 2 , name: 'i8'},
      {id: 2 , name: 'i8'},
      {id: 1 , name: '118'},
      {id: 2 , name: 'i8'},
      {id: 2 , name: 'i8'},
      {id: 2 , name: 'i8'},
    ];
  }

  constructor() { }

  ngOnInit() {
      this.getCars();
  }

}
