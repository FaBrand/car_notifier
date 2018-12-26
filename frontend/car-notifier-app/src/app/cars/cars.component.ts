import { Component, OnInit } from '@angular/core';
import { Car } from '../car';
import { CarService } from '../car.service';

@Component({
  selector: 'app-cars',
  templateUrl: './cars.component.html',
  styleUrls: ['./cars.component.css']
})
export class CarsComponent implements OnInit {
  cars: Car[];

  constructor(private carService: CarService ) { }

  getCars(): void {
    this.carService.getCars().subscribe(cars => this.cars = cars);
    // this.cars = [
    //   {id: 1 , description: 'Car-description', price: 49.99, name: 'M140i'},
    //   {id: 2 , description: 'Car-description', price: 49.99, name: 'i8'},
    //   {id: 2 , description: 'Car-description', price: 49.99, name: 'i8'},
    //   {id: 2 , description: 'Car-description', price: 49.99, name: 'i8'},
    //   {id: 1 , description: 'Car-description', price: 49.99, name: 'M140i'},
    //   {id: 2 , description: 'Car-description', price: 49.99, name: 'i8'},
    //   {id: 2 , description: 'Car-description', price: 49.99, name: 'i8'},
    //   {id: 2 , description: 'Car-description', price: 49.99, name: 'i8'},
    //   {id: 1 , description: 'Car-description', price: 49.99, name: 'M140i'},
    //   {id: 2 , description: 'Car-description', price: 49.99, name: 'i8'},
    //   {id: 2 , description: 'Car-description', price: 49.99, name: 'i8'},
    //   {id: 2 , description: 'Car-description', price: 49.99, name: 'i8'},
    // ];
  }

  ngOnInit() {
      this.getCars();
  }

}
