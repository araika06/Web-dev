import { Component } from '@angular/core';
import { ProductsComponent } from './products/products.component';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-root',
  template: `<app-products></app-products>`,
  styleUrls: ['./app.component.css'],
  imports: [CommonModule, ProductsComponent]
})
export class AppComponent {
  title = 'product-list';
}
