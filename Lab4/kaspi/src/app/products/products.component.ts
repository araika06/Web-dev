import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../product';

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule],
  templateUrl: `./products.component.html`,
  styleUrls: ['./products.component.css']
})

export class ProductsComponent {
  products: Product[] = [
    {
      image: ['assets/img1.jpg'],
      name: 'Клавиатура AULA F75',
      description: 'Клавиатура AULA F75 белый, беспроводная, 323x143x43 мм ',
      rating: 5.0,
      link: 'https://kaspi.kz/shop/p/aula-f75-belyi-117731409/?c=750000000'
    },

    {
      image: ['assets/img2.jpg'],
      name: 'Сумка Portcase 9011 черный',
      description: 'Сумка Portcase 9011 черный 15.6 дюймов плечевой ремень от воды, от пыли',
      rating: 4.8,
      link: 'https://kaspi.kz/shop/p/sumka-portcase-9011-chernyi-108895248/?c=750000000'
    },

    {
      image: ['assets/img3.jpg'],
      name: 'Wi-Fi роутер TP-LINK TD-W8961N',
      description: 'Wi-Fi роутер TP-LINK TD-W8961N, 195x35x130 мм, 250.0 г белый',
      rating: 4.7,
      link: 'https://kaspi.kz/shop/p/wi-fi-router-tp-link-td-w8961n-7600132/?c=750000000'
    },

    {
      image: ['assets/img4.jpg'],
      name: 'Мышь Logitech G102 Lightsync',
      description: 'Мышь Logitech G102 Lightsync черный, оптическая светодиодная, 116х62х38 мм, RGB-подсветка по технологии Lightsync',
      rating: 5.0,
      link: 'https://kaspi.kz/shop/p/logitech-g102-lightsync-chernyi-100956618/?c=750000000'
    },

    {
      image: ['assets/img5.jpg'],
      name: 'Bluetooth адаптер DONGLE USB V5.0',
      description: 'Cкорость: 3.0 Мбит/с, Версия Bluetooth5.0',
      rating: 4.1,
      link: 'https://kaspi.kz/shop/p/dongle-usb-v5-0-chernyi-102562037/?c=750000000'
    },

    {
      image: ['assets/img6.jpg'],
      name: 'Планшет Samsung Galaxy Tab A9+ 11 дюйм 8 Гб/128 Гб',
      description: 'Android 13, 8 ядер, Диагональ: 11.0 дюйм, 2023',
      rating: 5.0,
      link: 'https://kaspi.kz/shop/p/samsung-galaxy-tab-a9-11-djuim-8-gb-128-gb-seryi-113807079/?c=750000000'
    },

    {
      image: ['assets/img7.jpg'],
      name: 'Планшет Apple iPad 2022 10.9 Wi-Fi 10.9 дюйм 4 Гб/64 Гб серебристый',
      description: 'iOS 16, ядер 6 ядер, Частота процессора3100.0 МГц, металл',
      rating: 5.0,
      link: 'https://kaspi.kz/shop/p/apple-ipad-2022-10-9-wi-fi-10-9-djuim-4-gb-64-gb-serebristyi-107264764/?c=750000000'
    },

    {
      image: ['assets/img8.jpg'],
      name: 'Wi-Fi адаптер Kebidu KBT001121',
      description: 'Wi-Fi адаптер, ВИМАНИЕ! Не подойдёт для Телевизора, ТВ приставки.',
      rating: 4.1,
      link: 'https://kaspi.kz/shop/p/wi-fi-adapter-kebidu-kbt001121-105964946/?c=750000000'
    },

    {
      image: ['assets/img9.jpg'],
      name: 'Крепление для монитора North Bayou NB F-80 черный',
      description: 'настольный, наклон, поворот, регулируемая высота, вращение, черный',
      rating: 5.0,
      link: 'https://kaspi.kz/shop/p/north-bayou-nb-f-80-chernyi-101143323/?c=750000000'
    },

    {
      image: ['assets/img10.jpg'],
      name: 'Карта памяти Kingston SDCS2/128GB 128 Гб',
      description: 'Тип microSDXC, Объем памяти 128 Гб, адаптер на SD',
      rating: 4.9,
      link: 'https://kaspi.kz/shop/p/kingston-sdcs2-128gb-128-gb-100081405/?c=750000000'
    },
  ];

  shareOnTelegram(usernameOrGroup: string, link: string): void {
    window.open(`https://t.me/${usernameOrGroup}?text=${encodeURIComponent('📩 Посмотрите: ' + link)}`, '_blank');
  }
}
