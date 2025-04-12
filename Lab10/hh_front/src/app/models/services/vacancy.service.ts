import { Injectable } from '@angular/core';
import { Vacancy } from '../models/vacancy';
import { Company } from '../models/company';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'platform'
})
export class VacancyService {

  private apiUrl = 'http://127.0.0.1:8000/api/vacancies/';

  constructor(private http: HttpClient) { }

  getVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.apiUrl}/`);
  }

  getTopTen(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.apiUrl}/top-ten/`);
  }
}
