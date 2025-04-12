import { Component, OnInit } from '@angular/core';
import { VacancyService } from '../../services/vacancy.service';
import { Vacancy } from '../../models/vacancy';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-vacancy-list',
  imports: [CommonModule],
  templateUrl: './vacancy-list.component.html',
  styleUrl: './vacancy-list.component.css'
})
export class VacancyListComponent implements OnInit{
  vacancies: Vacancy[] = [];

  constructor(private vacancyService: VacancyService) {}

  ngOnInit(): void {
    this.vacancyService.getVacancies().subscribe(data => {
      this.vacancies = data;
    });
  }

}
