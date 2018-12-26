import { CarDescription } from './car_description';

export class Car {
    Kilowatt: number;
    PS: number;
    bookings: number[];
    classificationGroupingId: number;
    classificationManufacturerId: number;
    classificationManufacturerTypeId: number;
    description: CarDescription;
    fuelType: string;
    image: number;
    price: number;
    registrationNumber: string;
    stationId: number;
    watches: number[];
}
