import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Company } from '../models/company';
import { Vacancy } from '../models/vacancy';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'platform'
})
export class CompanyService {

  private url = 'http://127.0.0.1:8000/api/companies/';

  constructor(private http: HttpClient) { }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(this.url);
  }

  getCompanyVacancies(companyId: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.url}${companyId}/vacancies/`);
  }
}
