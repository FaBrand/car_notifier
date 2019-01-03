import { Component, OnInit } from '@angular/core';
import { CarService } from '../car.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  public navbarCollapsed = false;

  constructor(private carService: CarService ) { }

  updateList() {
    console.log('Updating!');
    this.carService.update();
  }

  ngOnInit() {
  }

}
