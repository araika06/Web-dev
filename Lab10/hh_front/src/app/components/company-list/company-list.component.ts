import { Component, OnInit } from '@angular/core';
import { CompanyService } from '../../services/company.service';
import { CommonModule } from '@angular/common';
import { Company } from '../../models/company';
import { Vacancy } from '../../models/vacancy';

@Component({
  selector: 'app-company-list',
  imports: [CommonModule],
  templateUrl: './company-list.component.html',
  styleUrl: './company-list.component.css'
})
export class CompanyListComponent implements OnInit{
  companies: Company[] = [];
  selectedCompanyVacancies: Vacancy[] = [];

  constructor(private companyService: CompanyService) { }

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe(data => {
      this.companies = data;
    });
  }

  showVacancies(companyId: number): void {
    this.companyService.getCompanyVacancies(companyId).subscribe(data => {
      this.selectedCompanyVacancies = data;
    });
  }




}
