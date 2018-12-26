import { CarDescription } from './car_description';
import { CarImage } from './car_image';

export class Car {
    Kilowatt: number;
    PS: number;
    bookings: number[];
    classificationGroupingId: number;
    classificationManufacturerId: number;
    classificationManufacturerTypeId: number;
    description: CarDescription;
    fuelType: string;
    image: CarImage;
    price: number;
    registrationNumber: string;
    stationId: number;
    watches: number[];
}
